#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Plays a sound clip after every sentence you say.
Currently only supports .wav files.
"""


# In[ ]:


from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave
import numpy

import argparse


# In[ ]:


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024


# In[ ]:


def args_parse():
    # Parses arguments
    parser = argparse.ArgumentParser(description='Pekofy arguments.')
    parser.add_argument('--clip', type=str,
                        help='Wav sound clip path.')
    parser.add_argument('--threshold', type=int,
                        help='Sound volume threshold to count as talking.')
    parser.add_argument('--delay', type=int,
                        help='Delay before peko is played after speech.')
    parser.add_argument('--talk_duration', type=int,
                        help='How long you need to talk for peko to be played.')

    parser.set_defaults(clip="./soundboard/peko.wav",
                        threshold = 750,
                        delay = 10,
                        talk_duration = 20)
    return parser.parse_args()

def check_threshold(data, THRESHOLD):
    # Checks if the sound volume is below the threshold
    return max(data) <= THRESHOLD

def pekoify(wav_file, PEKO_DELAY, TALK_DURATION, THRESHOLD):
    
    p = pyaudio.PyAudio()
    
    stream_in = p.open(format=FORMAT, 
                       channels=CHANNELS, 
                       rate=RATE,
                       input=True,
                       frames_per_buffer=CHUNK)
    
    stream_out = p.open(format=FORMAT, 
                        channels=CHANNELS, 
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)

    num_silent = 0
    num_talk = 0
    talking_started = False

    while True:
        mic_data = stream_in.read(CHUNK, exception_on_overflow=False)
        stream_out.write(mic_data)
        data_array = array('h', mic_data)
        if byteorder == 'big':
            # If big endian, swap bytes to little endian
            data_array.byteswap()

        silent = check_threshold(data_array, THRESHOLD)

        if silent and talking_started:
            # Increment silent counter when talking has started and is silent
            num_silent += 1
            if (num_silent > PEKO_DELAY and num_talk <= TALK_DURATION):
                # Reset counters and talking_started if the talk duration wasn't long enough
                # and the sound clip delay has been passed
                num_talk = 0
                num_silent = 0
                talking_started = False
            
        elif not silent and not talking_started:
            # Talking has started
            talking_started = True
            num_talk += 1
        
        elif not silent and talking_started:
            # Talking is happening
            num_silent = 0
            # Increment talking time
            num_talk += 1

        if talking_started and num_silent > PEKO_DELAY and num_talk > TALK_DURATION:
            # Start the sound clip
            print("Peko Started")
            peko_wav = wave.open(wav_file, 'rb')
            peko_data = peko_wav.readframes(CHUNK)

            stream_out_file = p.open(format=p.get_format_from_width(peko_wav.getsampwidth()),
                                     channels=peko_wav.getnchannels(),
                                     rate=peko_wav.getframerate(),
                                     output=True)

            while peko_data != b'':
                # Only play the sound clip and throw out any mic data
                stream_out_file.write(peko_data)
                peko_data = peko_wav.readframes(CHUNK)
                mic_data = stream_in.read(CHUNK, exception_on_overflow=False)

            print("Peko Ended\n")   
            peko_wav.close()
            talking_started = False
            num_silent = 0
            num_talk = 0

    stream_in.stop_stream()
    stream_in.close()
    stream_out.stop_stream()
    stream_out.close()
    p.terminate()


# In[ ]:


if __name__ == '__main__':
    args = args_parse()
    print("Pekofying Initiated")
    pekoify(args.clip, args.delay, args.talk_duration, args.threshold)
    print("Pekofying Completed")


# In[ ]:





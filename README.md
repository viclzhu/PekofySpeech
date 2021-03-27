# Pekofy your speech!
Haven't you ever wanted your own 'gobi' or 'ending particle' like your favorite Vtuber Pekora? This program plays a sound clip after every sentence you say! You can then route this audio to a software of your choice (ie. Discord) to share it with your friends!
You can also customize it to play any sound clip of your choice, defaulting to "peko". Currently it only supports .wav files. 
The `soundboard` folder contains a few different pre-selected soundclips for your use!

Note: While the sound clip is playing, your mic audio is ignored so you generally don't want to use a too long sound clip.

# Requirements
1. You need a 'virtual cable' program installed to route your computer output audio.
    - You can use VB-Cable, Blackhole, Loopback, etc.

# Installation
Clone this repo to the directory of your choice.
1. Open terminal and navigate to your chosen directory.
- Run `cd PATH/TO/REPO`.
2. Clone the repository.
- Run `git clone https://github.com/viclzhu/PekofySpeech.git`.

# How To Use
1. Enter the `PekofySpeech` directory.
    - Run `cd PATH/TO/REPO/PekofySpeech`.
2. Run `python pekofy.py`.
    - You can use the following flags to customize your Pekofying.
        - `--clip="CLIP_PATH"` lets you specify which sound clip to use. Default is `./soundboard/peko.wav`.
        - `--threshold=THRESHOLD` lets you specify the volume threshold for sound to count as talking. Default is 750.
        - `--delay=DELAY` lets you specify the time it takes after you stop talking to play the sound clip. Default is 10.
        - `--talk_duration=TALK_DURATION` lets you specify how long you need to talk for the sound clip to be played. Default is 20.
3. Now when you talk into your microphone, you should be able to hear yourself along with the sound clip played after you speak!

# Route your Pekofy'd Mic Audio to Discord Input
## Set Computer Audio Output as Discord Input
1. Set computer audio output to the 'virtual cable'.
- You need to set this before you run `python pekofy.py` so that the program finds the correct audio output.
2. Set Discord input to the 'virtual cable'.

## Cleanup
1. Set computer output to regular computer output.
2. Set discord input to regular computer input.

Note: This method routes all sound going through your audio out, so if you don't want that you'll have to set up multiple outputs and fiddle with it.

Note-Peko: The Jupyter notebook (.ipynb) does not directly work anymore with the addition of the argument parser! So you have to use the .py file unless you want to remove the argument parser from the ipynb.

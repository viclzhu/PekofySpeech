# Pekofy your speech!
Haven't you ever wanted your own 'gobi' or 'ending particle' like your favorite Vtuber Pekora? This program adds plays "peko" after every sentence you say. You can then route this audio to a software of your choice (ie. Discord) to share it with your friends!
You can also customize it to play any sound clip of your choice. Currently it only supports .wav files. 
The `soundboard` folder contains a few different pre-selected soundclips for your use!

Note: While the sound clip is playing, your mic audio is ignored so you generally don't want to use a too long sound clip.

# Requirements
1. You need a 'virtual cable' program installed to route your computer output audio.
    - You can use VB-Cable, Blackhole, Loopback, etc.

# How To Use
1. Run `python pekofy.py`
    - You can use the `--clip="CLIP_PATH"` flag to specify which sound clip to use. Default is `./soundboard/peko.wav`.

# Route your Pekofy'd Mic Audio to Discord Input
## Set Computer Audio Output as Discord Input
1. Set computer audio output to the 'virtual cable'.
2. Set Discord input to the 'virtual cable'.

## Cleanup
1. Set computer output to regular computer output.
2. Set discord input to regular computer input.

Note: This method routes all sound going through your audio out, so if you don't want that you'll have to set up multiple outputs and fiddle with it.
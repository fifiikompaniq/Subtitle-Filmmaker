"""

    Takes an audio file -> returns a file with the timestamps of the speech detection
    Using a moving frame-checker, we loop through the audio file (PCM WAV FORMAT)
    and we check each 30ms whether the VAD returns True or False. 
    If True, if there's no timestamp on the vector(index 1, index 2)
    we collect it on index 1. 
    If False, we collect the timestamp on index 2 and we export the tuple.  

"""
from webrtcvad import *
import wave

vad = Vad(1)
frame_duration = 30
sample_rate = 16000

"""

    Using silero-vad we can easily collect the timestamps.

"""
import torch

torch.set_num_threads(1)

from IPython.display import Audio
from pprint import pprint
# download example

model, utils = torch.hub.load(repo_or_dir='snakers4/silero-vad',
                              model='silero_vad',
                              force_reload=True)

(get_speech_timestamps,_, read_audio,*_) = utils

sampling_rate = 16000 # also accepts 8000
wav = read_audio('test.wav', sampling_rate=sampling_rate)
# get speech timestamps from full audio file
speech_timestamps = get_speech_timestamps(wav, model, sampling_rate=sampling_rate)
with open("timestamps.txt", "w") as vad: 
    vad.write(speech_timestamps)
pprint(speech_timestamps)


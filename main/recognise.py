import speech_recognition as sr
from moviepy.editor import *
from os import path
from pydub import AudioSegment

video_clip = VideoFileClip("E:\Subtitle-Filmmaker\main\\test.mp4")
audio_clip = video_clip.audio
dst = "test.wav"

audio_clip.write_audiofile("audio_file.mp3", 44100, 2, 2000)
recognizer = sr.Recognizer()
audio_src = "audio_file.mp3"
sound = AudioSegment.from_mp3(audio_src)
sound.export(dst, format="wav")


with sr.AudioFile("test.wav") as source: 
    audio = recognizer.record(source)

try: 
    with open("transcribe.txt", "w+") as transcript: 
        transcript.write("{}".format(recognizer.recognize_google_cloud(audio)))
except sr.UnknownValueError: 
    print("Could not understand audio.")
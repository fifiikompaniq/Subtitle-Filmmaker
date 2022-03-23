import speech_recognition as sr
from moviepy.editor import *
from os import path
from pydub import AudioSegment

video_clip = VideoFileClip("E:\Subtitle-Filmmaker\main\\test.mp4")
audio_clip = video_clip.audio


audio_clip.write_audiofile("audio_file.wav", 44100, 2, 2000)
recognizer = sr.Recognizer()
 


with sr.AudioFile("audio_file.wav") as source: 
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio = recognizer.record(source)

try: 
    with open("transcribe.txt", "w+") as transcript: 
        transcript.write("{}".format(recognizer.recognize_sphinx(audio)))
except sr.UnknownValueError: 
    print("Could not understand audio.")
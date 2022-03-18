import speech_recognition as sr
import moviepy as mp

video_clip = mp.VideoFileClip("E:\Subtitle-Filmmaker\\tests\\test.mp4")
audio_clip = video_clip.audio

recognizer = sr.Recognizer()

with sr.AudioFile(audio_clip) as source: 
    audio = recognizer.record(source)
    
try: 
    with fopen("transcribe.txt", "w+") as transcript: 
        transcript.write("{}".format(recognizer.recognize_sphinx(audio)))
except sr.UnknownValueError: 
    print("Could not understand audio.")

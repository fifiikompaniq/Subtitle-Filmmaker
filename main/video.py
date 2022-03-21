from moviepy.editor import VideoFileClip

with open("subtitles.srt", "r") as file: 
    for line in file: 
        timestamp = tuple(line)
        


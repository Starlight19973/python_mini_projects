import moviepy
from moviepy import editor
from pathlib import Path

video_file = Path('guf2.mp4')

video = moviepy.editor.VideoFileClip(f'{video_file}')

audio = video.audio

audio.write_audiofile(f'{video_file.stem}.mp3')
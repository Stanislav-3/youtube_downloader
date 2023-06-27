import pytube
from pytube import YouTube
import os

link = input("Enter the link of YouTube video you want to download:  ")

yt = YouTube(link)

# Showing details
print(yt.title)
title = yt.title
print("Title: ", title)

title = title.replace('/', '\\')

video = yt.streams.filter(adaptive=True).first()
audio = yt.streams.get_audio_only(subtype='')

print('\nAvailable streams:')
print('\nVideo:')
for stream in yt.streams.filter(adaptive=True).filter(type='video'):
    print(stream.resolution, stream.fps)

print('\nAudio:')
for stream in yt.streams.filter(adaptive=True).filter(type='audio'):
    print(stream.abr)

print('\nDownloading streams:')
print(video.resolution, video.fps, audio.abr)

print("\nDownloading separate streams...")

# video_path = f'video.{video.subtype}'
# audio_path = f'audio.{audio.subtype}'
video_path = 'video.{0}'.format(video.subtype)
audio_path = 'audio.{0}'.format(audio.subtype)

video.download()
os.rename(video.default_filename, video_path)
audio.download()
os.rename(audio.default_filename, audio_path)

print("\nCombining separate streams...")

# os.system(f'ffmpeg -hide_banner -loglevel error -i {video_path} -i {audio_path} -c:v copy -c:a aac out.mov')
# os.rename('out.mov', f'{title}.mov')

os.system('ffmpeg -hide_banner -loglevel error -i {0} -i {1} -c:v copy -c:a aac out.mov'.format(video_path, audio_path))
os.rename('out.mov', '{0}.mov'.format(title))

os.remove(audio_path)
os.remove(video_path)

print("\nDownload completed!")

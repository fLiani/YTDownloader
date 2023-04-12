from pytube import YouTube
from sys import argv

link = argv[1]

video = YouTube(link)

stream = video.streams.get_highest_resolution()

stream.download(argv[2])
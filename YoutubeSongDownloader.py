import youtube_dl
import sys

print("Enter the URL of the video of which you want the song")
video_url = input()

# Part of Youtube-dl Library.
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print("Done Downloading")


def DownloadSong(url):
    ydl_opts = {
        'format': '140',
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None)
        print("Downloading => " + video_title)
        ydl.download([url])


DownloadSong(video_url)

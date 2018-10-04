from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    print(d)
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'mp4',
    'logger': MyLogger(),
    'progress_hooks': [my_hook]
}
ydl=youtube_dl.YoutubeDL(ydl_opts)
url=input('Enter Video URL : ')
ydl.download([url])


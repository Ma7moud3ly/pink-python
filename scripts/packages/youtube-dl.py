import youtube_dl

ydl_opts = {}
ydl=youtube_dl.YoutubeDL(ydl_opts)

url=input('Paste Video URL : ')
ydl.download([url])

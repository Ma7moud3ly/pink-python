import ffmpeg
input = ffmpeg.input('https://ma7moud3ly.github.io/video.mp4')
hflip=input.hflip()
vflip=input.vflip()
ffmpeg.run(ffmpeg.output(hflip, 'hflip.mp4'))
ffmpeg.run(ffmpeg.output(vflip, 'vflip.mp4'))


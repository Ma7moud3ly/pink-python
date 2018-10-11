import ffmpeg
input = ffmpeg.input('https://ma7moud3ly.github.io/video.mp4')
output = ffmpeg.output(input, 'image.gif')
ffmpeg.run(output)

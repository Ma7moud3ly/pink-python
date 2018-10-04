import ffmpeg
input = ffmpeg.input('https://ma7moud3ly.github.io/video.mp4')

text=input.drawtext(text='Pink Python ^_^',
fontcolor='red',
fontsize=30,
box=1,
boxcolor='black@0.5',
x='(w-text_w)/2',
y='(h-text_h)/2'
)

text=text.drawtext(text='By Mahmoud Aly',
fontcolor='white',
fontsize=15,
x='(w-text_w)/2',
y='((h-text_h)/2)+30'
)

output=ffmpeg.output(text, 'text.mp4')
ffmpeg.run(output,overwrite_output=True)


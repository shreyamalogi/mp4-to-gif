# import the necessary module
from moviepy.editor import *

# load the video
clip = VideoFileClip("movie.mp4")

# getting only 3 first seconds from video
clip = clip.subclip(0, 3)

# save the video clip as gif
clip.write_gif("movie.gif")
from moviepy.editor import *
import pygame

pygame.display.set_caption('My video!')

clip = VideoFileClip('Videos/sample.mpg')
clip.ipython_display(width = 280)
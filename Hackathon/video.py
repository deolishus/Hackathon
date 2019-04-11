import pygame
import sys

FPS = 60

size = width, height = 1080, 720
screen = pygame.display.set_mode(size)

pygame.init()
pygame.mixer.init()

video = "Videos/sample.mpg"
clock = pygame.time.Clock()

####screen = pygame.display.set_mode((800, 600))
video = pygame.movie.Movie(video)
w,h = video.get_size()
#screen = pygame.display.set_mode((w,h))
video.set_display(screen,(0,0,500,500))
video.play()

while True:
    event=pygame.event.wait()
    if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

import pygame, sys
import pygame.event as keyboard
from time import sleep

pygame.init()

size = width, height = 1080, 720
screen = pygame.display.set_mode(size)

#picture locations
car = "Photos/car.jpg"
food = "Photos/food.jpg"
stanford = "Photos/stanford.jpg"
events = "Photos/events.jpg"


#variables to load pictures with resize function to scale to window
firstpic = pygame.transform.scale(pygame.image.load(car), size)
secondpic = pygame.transform.scale(pygame.image.load(food), size)
thirdpic = pygame.transform.scale(pygame.image.load(stanford), size)
fourthpic = pygame.transform.scale(pygame.image.load(events), size)


def quit_screen():
    pygame.quit()
    sys.exit()
    quit()

def fourth_screen():
    while True:
        screen.blit(fourthpic, (0,0))
        pygame.display.update()
        for event in keyboard.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    third_screen()
                if event.key == pygame.K_ESCAPE:
                    quit_screen()

def third_screen():
    while True:
        screen.blit(thirdpic, (0,0))
        pygame.display.update()
        for event in keyboard.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    second_screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    fourth_screen()
            if event.key == pygame.K_ESCAPE:
                quit_screen()

def second_screen():
    while True:
        screen.blit(secondpic, (0,0))
        pygame.display.update()
        for event in keyboard.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    first_screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    third_screen()
            if event.key == pygame.K_ESCAPE:
                quit_screen()

def first_screen():
    while True:
        screen.blit(firstpic, (0,0))
        pygame.display.update()
        for event in keyboard.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    second_screen()
                if event.key == pygame.K_ESCAPE:
                    quit_screen()

while True:
    for event in keyboard.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit_screen()

    first_screen()

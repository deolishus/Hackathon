import pygame
import sys
import subprocess
from time import sleep

file = 'Videos/sample.mp4'
omxprocess = subprocess.Popen(['omxplayer', file], stdin = subprocess.PIPE, stdout = None, stderr = None, bufsize = 0)
sleep(3)

#omxprocess.stdin.write('q')

sleep(3)
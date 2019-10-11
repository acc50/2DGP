from pico2d import *
import os
import math

open_canvas()

os.chdir('D:/2018182024 LeeDongHyun/2DGP/Labs/Lecture04')

grass = load_image('grass.png')
character = load_image('character.png')

angle = 0
x = 0
y = 0

while(angle < (360 * 4)):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    angle = angle + 1
    x = 400 + (200 * math.sin(angle / 360 * 2 * math.pi))
    y = 300 + (200 * math.cos(angle / 360 * 2 * math.pi))
    delay(0.005)

close_canvas()

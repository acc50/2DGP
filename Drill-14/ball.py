import random
from pico2d import *
import game_world
import game_framework

DISTANCE = 100
WIDTH, HEIGHT = 1837, 1109


class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(DISTANCE, WIDTH - DISTANCE), random.randint(DISTANCE, HEIGHT - DISTANCE - 1)

    def get_bb(self):
        # return self.x - 10, self.y - 10, self.x + 10, self.y + 10
        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        return cx - 10, cy - 10, cx + 10, cy + 10

    def draw(self):
        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.clip_draw(0, 0, 21, 21, cx, cy)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def set_background(self, bg):
        self.bg = bg
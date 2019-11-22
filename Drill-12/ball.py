import random
from pico2d import *
import game_world
import game_framework

DISTANCE = 100
WIDTH, HEIGHT = 1280, 1024


class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(DISTANCE, WIDTH - DISTANCE), random.randint(DISTANCE, HEIGHT - DISTANCE - 1)

        self.hp = 50

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass


class BigBall(Ball):  # Ball 을 상속받음
    image = None

    def __init__(self):
        if BigBall.image is None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(DISTANCE, WIDTH - DISTANCE), random.randint(DISTANCE, HEIGHT - DISTANCE - 1)

        self.hp = 100

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

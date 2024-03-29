import random
from pico2d import *
import game_world
import game_framework

MIN_FALL_SPEED = 200  # 200 pps = 6 meter per sec
MAX_FALL_SPEED = 400  # 400 pps = 12 meter per sec


class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 60, 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

    def fall_stop(self):
        self.fall_speed = 0

    def move(self, speed, brick_dir):
        self.x += speed * brick_dir * game_framework.frame_time

    def fall(self):
        self.fall_speed = random.randint(MIN_FALL_SPEED, MAX_FALL_SPEED)


class BigBall(Ball):    # Ball 을 상속받음
    image = None

    def __init__(self):
        if BigBall.image is None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1600 - 1), 500
        self.fall_speed = random.randint(MIN_FALL_SPEED, MAX_FALL_SPEED)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

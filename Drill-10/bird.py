import game_framework
from pico2d import *

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0   # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')       # ~ 183 * 168
        self.x, self.y = 400, 300
        self.velocity = RUN_SPEED_PPS
        self.dir = 1
        self.frame_x = 0
        self.frame_y = 2

    def draw(self):
        # self.image.clip_draw(int(self.frame_x) * 183.6, self.frame_y * 168.7, 183.6, 168.7, self.x, self.y)
        self.image.clip_draw(int(self.frame_x) * 183, self.frame_y * 168, 183, 168, self.x, self.y, 100, 100)
        # 사이즈 100 * 100

    def update(self):
        self.frame_x = (self.frame_x + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
        if self.frame_y == 0 and self.frame_x >= 4:     # 애니메이션 마지막줄
            self.frame_x = 0
            self.frame_y = 2
        elif self.frame_x >= 5:
            self.frame_x = 0
            self.frame_y -= 1

        self.x += self.velocity * game_framework.frame_time
        self.x = clamp(20, self.x, 1600 - 20)

        if self.x >= (1600 - 20):
            self.velocity = -RUN_SPEED_PPS
        elif self.x <= 20:
            self.velocity = RUN_SPEED_PPS

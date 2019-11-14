from pico2d import *
import game_framework


class Brick:
    def __init__(self):
        self.x, self.y = 600, 160
        self.move_speed = 500
        self.dir = 1
        self.image = load_image('brick180x40.png')

    def update(self):
        self.x += self.dir * self.move_speed * game_framework.frame_time
        if self.x >= 1600 - 90:
            self.dir = -1
        elif self.x <= 90:
            self.dir = 1
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def get_velocity(self):
        return self.move_speed, self.dir

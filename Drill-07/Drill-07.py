from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)
    pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
    pass


class LargeBall:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599
        self.image = load_image('ball41x41.png')

    def update(self):
        self.y -= random.randint(1, 5) / random.randint(1, 7)

    def physics_update(self):
        if self.y < 41 + 31:        # 공의 크기 + 잔디 크기
            self.y = 41 + 31

    def draw(self):
        self.image.draw(self.x, self.y)
    pass


class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(30, 770), 599
        self.image = load_image('ball21x21.png')

    def update(self):
        self.y -= random.randint(1, 5) / random.randint(1, 7)

    def physics_update(self):
        if self.y < 21 + 40:
            self.y = 21 + 40

    def draw(self):
        self.image.draw(self.x, self.y)
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()
grass = Grass()
team = [Boy() for i in range(11)]

largeBall_count = random.randint(7, 13)
smallBall_count = 20 - largeBall_count

LargeGroup = [LargeBall() for l in range(largeBall_count)]
SmallGroup = [SmallBall() for s in range(smallBall_count)]

running = True

while running:
    handle_events()  # 사용자 움직임

    for boy in team:     # 스스로 움직임, 물리 작용
        boy.update()

    for L_ball in LargeGroup:
        L_ball.update()
        L_ball.physics_update()

    for S_ball in SmallGroup:
        S_ball.update()
        S_ball.physics_update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for L_ball in LargeGroup:
        L_ball.draw()
    for S_ball in SmallGroup:
        S_ball.draw()
    update_canvas()

close_canvas()

from pico2d import *
import random

Width, Height = 1280, 1024


def handle_events():
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    pass


def move_curve_4points(p1, p2, p3, p4, distance, speed):
    global x, y

    # move p1-p2
    t = distance / speed
    x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
            -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
    y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
            -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2

    pass


open_canvas(Width, Height)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
random_points = [(random.randint(1, 1200), random.randint(1, 1000)) for n in range(10)]
x, y = random_points[0][0], random_points[0][1]
frame = 0
i = 0
n = 0
ratio = 1000
character_dir = 1
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(Width // 2, Height // 2)
    character.clip_draw(frame * 100, character_dir * 100, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    move_curve_4points(random_points[n % 10], random_points[(n+1) % 10],
                       random_points[(n+2) % 10], random_points[(n+3) % 10], i, ratio)
    i += 1
    if i > ratio:
        i = 0
        n += 1


close_canvas()

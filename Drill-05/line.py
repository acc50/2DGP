from pico2d import *
import random

Width, Height = 800, 600


def handle_events():
    global running
    global character_x, character_y
    global hand_x, hand_y
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            hand_x, hand_y = event.x, Height - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    pass


def draw_line(p1, p2):
    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]

    pass


open_canvas()
kpu_ground = load_image('KPU_GROUND.png')
hand_arrow = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
character_x, character_y = Width // 2, Height // 2
hand_x, hand_y = Width // 2, Height // 2
frame_x = 0
frame_y = 1
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(Width // 2, Height // 2)
    character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, character_x, character_y)
    hand_arrow.draw(hand_x, hand_y)
    update_canvas()
    frame_x = (frame_x + 1) % 8

    handle_events()

close_canvas()
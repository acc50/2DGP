from pico2d import *
import random

Width, Height = 800, 600


def draw_background():
    clear_canvas()
    kpu_ground.draw(Width // 2, Height // 2)
    character.clip_draw(frame_x * 100, dir * 100, 100, 100, character_x, character_y)
    hand_arrow.draw(hand_x, hand_y)
    update_canvas()


def move_character(p1, p2):
    global character_x, character_y
    global dir
    global temp, click_count

    if p1[0] <= p2[0]:
        dir = 1
    elif p1[0] > p2[0]:
        dir = 0

    ratio = 300
    for i in range(0, ratio + 1, 1):
        draw_background()

        handle_events()
        if temp != click_count:
            temp = click_count
            break

        t = i / ratio
        character_x = (1 - t) * p1[0] + t * p2[0]
        character_y = (1 - t) * p1[1] + t * p2[1]

    pass


def handle_events():
    global running
    global hand_x, hand_y
    events = get_events()
    global temp
    global click_count

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            hand_x, hand_y = event.x, Height - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            move_character((character_x, character_y), (hand_x, hand_y))
            click_count += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    pass


open_canvas()
kpu_ground = load_image('KPU_GROUND.png')
hand_arrow = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
character_x, character_y = Width // 2, Height // 2
hand_x, hand_y = Width // 2, Height // 2
frame_x = 0
dir = 1                     # 캐릭터의 방향
temp, click_count = 0, 0
hide_cursor()

while running:
    draw_background()

    handle_events()
    frame_x = (frame_x + 1) % 8
    temp = 0
    click_count = 0

close_canvas()
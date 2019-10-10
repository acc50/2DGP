from pico2d import *

Width, Height = 800, 600


def handle_events():
    global running
    global hand_x, hand_y
    global mouse_x, mouse_y
    global character_x
    global Move
    global i
    global dir
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, Height - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            hand_x, hand_y = event.x, Height - 1 - event.y
            Move = True
            i = 0
            if hand_x > character_x:
                dir = 1
            elif hand_x <= character_x:
                dir = 0
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
mouse_x, mouse_y = Width // 2, Height // 2
frame_x = 0
dir = 1                     # 캐릭터의 방향
Move = False
t, i, ratio = 0, 0, 800     # t, 이동변수, 비율
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(Width // 2, Height // 2)
    character.clip_draw(frame_x * 100, dir * 100, 100, 100, character_x, character_y)
    hand_arrow.draw(mouse_x, mouse_y)
    update_canvas()

    handle_events()
    frame_x = (frame_x + 1) % 8

    if Move:
        t = i / ratio
        character_x = (1 - t) * character_x + t * hand_x
        character_y = (1 - t) * character_y + t * hand_y
        i += 1

    if i >= ratio:
        Move = False
        i = 0
        t = 0


close_canvas()

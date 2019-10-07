from pico2d import *


def handle_events():
    global running
    global frame_y
    global dir


    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir = dir + 1
                frame_y = 1
            elif event.key == SDLK_LEFT:
                dir = dir - 1
                frame_y = 0
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir = dir - 1
                frame_y = 3
            elif event.key == SDLK_LEFT:
                dir = dir + 1
                frame_y = 2
    pass


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame_x = 0
frame_y = 3
dir = 0

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame_x * 100, 100 * frame_y, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame_x = (frame_x + 1) % 8
    if x < 20:
        x += 1
    elif x > 780:
        x -= 1
    x = x + dir

close_canvas()


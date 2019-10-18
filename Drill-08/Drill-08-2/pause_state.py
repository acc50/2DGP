import game_framework
import main_state
from pico2d import *


name = "PauseState"
image = None
pause_timer = None


def enter():
    global image, pause_timer
    image = load_image('Pause.png')
    pause_timer = 0
    pass


def exit():
    global image
    del image
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
    pass


def draw():
    clear_canvas()
    if pause_timer > 100:
        image.clip_draw(200, 200, 500, 500, 400, 300, 200, 200)
        # 200,200 부터 500,500 만큼을 400,300 위치에 200,200 사이즈로 그려라
    main_state.grass.draw()
    main_state.boy.draw()
    update_canvas()
    pass


def update():
    global pause_timer
    pause_timer = (pause_timer + 1) % 1000
    pass


def pause():
    pass


def resume():
    pass







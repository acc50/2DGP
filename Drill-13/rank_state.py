import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import world_build_state

name = "RankState"


font = None
zombies = []
ranking = []

def enter():
    global font
    font = load_font('ENCR10B.TTF', 20)
    ranking.sort()
    ranking.reverse()

    while len(ranking) > 10:
        ranking.pop(10)

    pass

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)


def update():

        pass


def draw():
    clear_canvas()

    rx = 10
    ry = 500
    for rank in ranking:
        font.draw(rx, ry, '%2.2f' %rank, (0, 0, 0))
        ry -= 20

    update_canvas()


def get_ranking():
    return ranking

def set_ranking(ranking_list):
    global ranking
    ranking = ranking_list







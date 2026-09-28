from math import cos, pi, sin
from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_DELAY = 0.01

running = True
character = None


def handle_events():
    """창 닫기 버튼이나 Esc 키가 눌렸는지 확인한다."""
    global running

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def draw_character(x, y):
    """캐릭터를 새 위치에 그리고 다음 프레임까지 잠시 기다린다."""
    handle_events()
    if not running:
        return False

    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(FRAME_DELAY)
    return True


def move_line(start, end, frames):
    """start에서 end까지 직선으로 이동한다."""
    start_x, start_y = start
    end_x, end_y = end

    for frame in range(frames):
        ratio = frame / frames
        x = start_x + (end_x - start_x) * ratio
        y = start_y + (end_y - start_y) * ratio
        if not draw_character(x, y):
            return False

    return running


def move_circle():
    """화면 중앙을 기준으로 원을 한 바퀴 돈다."""
    center_x, center_y = 400, 300
    radius = 200

    for degree in range(360):
        angle = degree * pi / 180
        x = center_x + radius * cos(angle)
        y = center_y + radius * sin(angle)
        if not draw_character(x, y):
            return False

    return running


def move_rectangle():
    """사각형의 네 변을 따라 한 바퀴 돈다."""
    points = [
        (200, 150),
        (600, 150),
        (600, 450),
        (200, 450),
        (200, 150),
    ]

    for start, end in zip(points, points[1:]):
        distance = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
        if not move_line(start, end, distance):
            return False

    return running


def move_triangle():
    """삼각형의 세 변을 따라 한 바퀴 돈다."""
    points = [
        (400, 500),
        (200, 150),
        (600, 150),
        (400, 500),
    ]

    for start, end in zip(points, points[1:]):
        distance = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
        if not move_line(start, end, distance):
            return False

    return running


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
character_path = Path(__file__).with_name('character.png')
character = load_image(str(character_path))

while running:
    if not move_circle():
        break
    if not move_rectangle():
        break
    if not move_triangle():
        break

close_canvas()

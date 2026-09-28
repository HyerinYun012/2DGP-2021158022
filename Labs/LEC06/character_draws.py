# 실습 과제 진행
# 함수를 호출 후 실제 내용을 채워간다. 
from pico2d import *

open_canvas(800, 600)
character = load_image('character.png')



def move_circle():
    print("Circle")
    r = 300

    # 1/4 원 그리기
    for b in range(0,r):
        clear_canvas()
        character.draw(int(400+(r*r-b*b)**0.5), int(300 + b)) 
        update_canvas()
        delay(0.01)
    # 1/4 원 그리기
    for b in range(r, 0, -1):
        clear_canvas()
        character.draw(int(400-(r*r-b*b)**0.5), int(300 + b)) 
        update_canvas()
        delay(0.01)
    # 1/4 원 그리기
    for b in range(0,r):
        clear_canvas()
        character.draw(int(400-(r*r-b*b)**0.5), int(300 - b)) 
        update_canvas()
        delay(0.01)
    # 1/4 원 그리기
    for b in range(r, 0, -1):
        clear_canvas()
        character.draw(int(400+(r*r-b*b)**0.5), int(300 - b)) 
        update_canvas()
        delay(0.01)
    
    pass    


def move_rectangle():
    print("Rectangle")

    # 사각형 가로 그리기
    x =300
    # 사각형 세로 길이
    y = 300
    while x < 700: # 가로 길이는 300, 중심 (400,300)
        clear_canvas()
        character.draw(x, 300)
        update_canvas()
        x += 1
        delay(0.01)
    while y < 500:
        clear_canvas()
        character.draw(700, y)
        update_canvas()
        y += 1
        delay(0.01)
    while x > 300:
        clear_canvas()
        character.draw(x, 500)
        update_canvas()
        x -= 1
        delay(0.01)
    pass

def move_triangle():
    clear_canvas()
    character.draw(400, 300)
    update_canvas()
    print("Triangle")

    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass


close_canvas()
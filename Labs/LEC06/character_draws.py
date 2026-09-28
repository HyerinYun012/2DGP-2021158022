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
    pass    

def move_rectangle():
    print("Rectangle")
    clear_canvas()
    character.draw(400, 300)
    update_canvas()
    
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
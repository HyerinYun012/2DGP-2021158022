# 실습 과제 진행
# 함수를 호출 후 실제 내용을 채워간다. 
# 테스트 리드 타임을 줄여야 한다. 
import math
from pico2d import *

open_canvas(800, 600)
character = load_image('character.png')

def draw_top():
    print('top')
    pass

def draw_left():
    print('left')
    pass

def draw_right():
     print('right')
     pass

def draw_bottom():
     print('bottom')
     pass

def move_circle():
    print("Circle")
    for deg in range(0,360,1):
        rad = math.radians(deg)
        x=400+200*math.cos(rad)
        y=300+200*math.sin(rad)
        clear_canvas()
        character.draw(x,y)
        update_canvas()
        delay(0.01)
    pass    


def move_rectangle():
    print("Rectangle")
    # 최대한 잘게 쪼갠다. 
    draw_top()
    draw_right()
    draw_bottom()
    draw_left()
    
    pass

def move_triangle():
    print("Triangle")
    pass

while True:
    # move_circle()
    move_rectangle()
    move_triangle()
    break
    pass


close_canvas()
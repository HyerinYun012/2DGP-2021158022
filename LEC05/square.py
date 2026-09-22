from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')

start_x = 300
start_y = 200

rect_width = 200
rect_height = 150

x = 0
while x< rect_width:
    
    x += 0.5

    clear_canvas()
    character.draw(start_x + x, start_y)
    update_canvas()

y = 0
while y < rect_height:
    y += 0.5

    clear_canvas()
    character.draw(start_x+rect_width, start_y+y)
    update_canvas()

while x>0:
    x -= 0.5

    clear_canvas()
    character.draw(start_x + x, start_y+rect_height)
    update_canvas()

while y>0:
    y -= 0.5

    clear_canvas()
    character.draw(start_x, start_y+y)
    update_canvas()
    


delay(3)

close_canvas()
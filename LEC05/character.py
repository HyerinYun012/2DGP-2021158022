from pico2d import *


open_canvas(800, 600)

# 여기를 채우시오.
character = load_image('character.png')

grass = load_image('grass.png')

x = 0
while x< 800:
    
    x += 2

    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 90)
    update_canvas()

    delay(0.01)

delay(5)

close_canvas()


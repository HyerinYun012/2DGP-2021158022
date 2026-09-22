from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')

center_x = 400
center_y = 300
radius = 150

degree = 0

running = True

while(running):
    degree = 0;
    while degree < 360:

        clear_canvas()
    
        radian = math.radians(degree)

        x = center_x + radius * math.cos(radian)
        y = center_y + radius * math.sin(radian)
    
        character.draw(x, y)
    
        update_canvas()
        delay(0.01)
    
        degree += 2

        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False

    
close_canvas()
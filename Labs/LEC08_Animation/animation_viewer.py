from pico2d import *


open_canvas()

sprite_sheet = load_image('sprite_sheet.png')
frame = 0
scale = 2
idle_frames = [
    (121, 685, 200, 222, 200),
    (322, 685, 208, 222, 408),
    (526, 685, 199, 222, 611),
    (724, 685, 226, 222, 814)
]
idle_frame_order = [0, 1, 2, 3, 2, 1]

for _ in range(5):
    for frame in idle_frame_order:
        left, bottom, width, height, feet_center_x = idle_frames[frame]
        draw_x = 400 - (feet_center_x - (left + width / 2)) * scale

        clear_canvas()
        sprite_sheet.clip_draw(
            left, bottom,
            width, height,
            draw_x, 300,
            width * scale, height * scale
        )
        update_canvas()
        delay(0.2)

delay(1)

close_canvas()

from pico2d import *


open_canvas()

sprite_sheet = load_image('sprite_sheet.png')
frame = 0
idle_frames = [
    (0, 681, 320, 260),
    (320, 681, 220, 260),
    (526, 681, 200, 260)
]

for frame in range(len(idle_frames)):
    left, bottom, width, height = idle_frames[frame]

    clear_canvas()
    sprite_sheet.clip_draw(
        left, bottom,
        width, height,
        400, 300
    )
    update_canvas()
    delay(0.2)

close_canvas()

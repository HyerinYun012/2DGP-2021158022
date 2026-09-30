from pico2d import *


open_canvas()

sprite_sheet = load_image('sprite_sheet.png')
frame = 0
idle_frames = [
    (0, 681, 320, 260)
]
left, bottom, width, height = idle_frames[frame]

clear_canvas()
sprite_sheet.clip_draw(
    left, bottom,
    width, height,
    400, 300
)
update_canvas()
delay(3)

close_canvas()

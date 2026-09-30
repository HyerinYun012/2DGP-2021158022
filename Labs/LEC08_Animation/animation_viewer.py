from pico2d import *


open_canvas()

sprite_sheet = load_image('sprite_sheet.png')
frame = 0
idle_frames = [
    # (left, bottom, width, height)
]

clear_canvas()
sprite_sheet.clip_draw(
    frame * 320, 681,
    320, 260,
    400, 300
)
update_canvas()
delay(3)

close_canvas()

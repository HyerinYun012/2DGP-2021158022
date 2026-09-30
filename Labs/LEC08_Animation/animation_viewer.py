from pico2d import *


open_canvas()

sprite_sheet = load_image('sprite_sheet.png')
scale = 2
idle_frames = [
    (121, 685, 200, 222, 200),
    (322, 685, 208, 222, 408),
    (526, 685, 199, 222, 611),
    (724, 685, 226, 222, 814)
]
idle_frame_order = [0, 1, 2, 3, 2, 1]
walk_frames = [
    (134, 449, 235, 215, 266),
    (363, 449, 236, 215, 482),
    (595, 449, 224, 215, 715),
    (812, 449, 229, 215, 936),
    (1034, 449, 226, 215, 1152),
    (1256, 449, 199, 215, 1344)
]
walk_frame_order = [0, 1, 2, 3, 4, 5]
run_frames = [
    (36, 236, 208, 202, 150),
    (244, 236, 189, 202, 339),
    (433, 236, 214, 202, 550),
    (647, 236, 265, 202, 808),
    (912, 236, 210, 202, 1019),
    (1122, 236, 264, 202, 1276),
    (1386, 236, 266, 202, 1548)
]
run_frame_order = [0, 1, 2, 3, 4, 5, 6]
attack_frames = [
    (55, 19, 193, 227, 126),
    (305, 19, 282, 227, 390),
    (587, 19, 449, 227, 796),
    (1036, 19, 330, 227, 1227),
    (1366, 19, 299, 227, 1517)
]
attack_frame_order = [0, 1, 2, 3, 4]

def play_animation(frames, frame_order):
    for _ in range(5):
        for frame in frame_order:
            left, bottom, width, height, anchor_x = frames[frame]
            draw_x = 400 - (anchor_x - (left + width / 2)) * scale

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


play_animation(idle_frames, idle_frame_order)
play_animation(walk_frames, walk_frame_order)
play_animation(run_frames, run_frame_order)
play_animation(attack_frames, attack_frame_order)

close_canvas()

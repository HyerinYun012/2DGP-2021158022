from pico2d import *


open_canvas()

sprite_sheet = load_image('sprite_sheet_clean.png')
scale = 2
frame_width = 480
frame_height = 240


def make_frames(bottom, frame_count):
    return [
        (frame * frame_width, bottom, frame_width, frame_height)
        for frame in range(frame_count)
    ]


idle_frames = make_frames(720, 4)
walk_frames = make_frames(480, 6)
run_frames = make_frames(240, 7)
attack_frames = make_frames(0, 5)

idle_frame_order = list(range(len(idle_frames)))
idle_frame_order += list(range(len(idle_frames) - 2, 0, -1))
walk_frame_order = list(range(len(walk_frames)))
run_frame_order = list(range(len(run_frames)))
attack_frame_order = list(range(len(attack_frames)))
animations = [
    (idle_frames, idle_frame_order),
    (walk_frames, walk_frame_order),
    (run_frames, run_frame_order),
    (attack_frames, attack_frame_order)
]

def quit_requested():
    for event in get_events():
        if event.type == SDL_QUIT:
            return True
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            return True

    return False


def play_animation(frames, frame_order):
    for _ in range(5):
        for frame in frame_order:
            if quit_requested():
                return False

            left, bottom, width, height = frames[frame]

            clear_canvas()
            sprite_sheet.clip_draw(
                left, bottom,
                width, height,
                400, 300,
                width * scale, height * scale
            )
            update_canvas()
            delay(0.2)

    for _ in range(10):
        if quit_requested():
            return False
        delay(0.1)

    return True


running = True
while running:
    for frames, frame_order in animations:
        running = play_animation(frames, frame_order)
        if not running:
            break

close_canvas()

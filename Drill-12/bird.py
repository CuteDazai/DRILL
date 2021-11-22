from pico2d import *
import game_world
import game_framework

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class flyState:
    def enter(bird):
        bird.frame = 0;

    def exit(bird):
        pass

    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        print(bird.frame)

    def draw(bird):
        bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)


class Bird:
    def __init__(self):
        self.x, self.y = 90, 400
        self.image = load_image('bird100x100x14.png')
        self.dir = 1
        self.frame = 0
        self.cur_state = flyState
        self.cur_state.enter(self)

    def update(self):
        pass

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return 0, 0, 0, 0
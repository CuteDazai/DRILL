from pico2d import *
import random

# Game object class here
class Grass:
    #속성정의 >> 생성자 함수
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 100), 90
        self.image = load_image(("run_animation.png"))
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.x += 5
        delay(0.005)
        self.frame = (self.frame+1)%8

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599
        self.image = load_image(("ball41x41.png"))
        self.frame = 0
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y >= 80:
            self.y -= random.randint(10, 100)
            delay(0.001)
        else:
            self.y = 80

class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599
        self.image = load_image(("ball21x21.png"))
        self.frame = 0
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y- >= 70:
            self.y -= random.randint(10, 100)
            delay(0.001)
        else:
            self.y = 70
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
grass = Grass()
big_ball = []
small_ball = []
team = []   #team = [i for i in range(1, 11+1)]
for i in range(1, 11+1):
    team.append(Boy())
for i in range(1, 10+1):
    big_ball.append(BigBall())
for i in range(1, 10+1):
    small_ball.append(SmallBall())
running = True
# game main loop code
while running:
    handle_events()


    #gmae logic
    for boy in team:
        boy.update()
    for bb in big_ball:
        bb.update()
    for sb in small_ball:
        sb.update()
    #game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for bb in big_ball:
        bb.draw()
    for sb in small_ball:
        sb.draw()
    update_canvas()

# finalization code
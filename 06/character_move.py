from pico2d import *
import math
open_canvas()

grass =  load_image('grass.png')
character = load_image('character.png')
speed = 10

def rendering(x,y):
    clear_canvas()
    grass.draw(400,30)
    character.draw(x,y)
    update_canvas()
    delay(0.05)

def move_square(width=800, hight=600):
    x=20
    y=90
    while x<width-20:
        rendering(x,y)
        x+=speed
    while y<hight-40:
        rendering(x,y)
        y+=speed
    while x>20:
        rendering(x,y)
        x-=speed
    while y>90:
        rendering(x,y)
        y-=speed

def move_circle():
    ang=-90;
    while ang<270:
        x=math.cos(math.pi*(ang/180))*240+400
        y=math.sin(math.pi*(ang/180))*240+330
        rendering(x,y)
        ang+=speed
        #print(ang)
        
while True:
    move_circle()
    move_square()

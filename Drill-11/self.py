class Star:
    type = 'Star'   # 클래스 변수
    x = 100 # 클래스 변수

    def change():
        x = 200
        print('x is', x)

print('x IS ', Star.x)  # OK
Star.change()   # OK    클래스 변수x가 아니라 지역변수 x를 바꿈
print('x IS ', Star.x)

star = Star()   # OK
print('x Is ', star.x)  # OK
#star.change()   # Error


#파이썬의 클래스는 생성자가 없어도 된다.
#Star.change() ==> Star.change(Star)    자기 자신을 첫번째 매개변수로 넘겨줌


class Player:
    type = 'Player'

    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)

player = Player()
player.where()

#클래스 변수 사용
print(Player.type)

#클래스 함수 호출
Player.where() # Error
Player.where(player)    # OK, player.where() 과 같은 의미.
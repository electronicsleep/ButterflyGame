butterfly = Actor('butterfly')
butterfly.pos = 100, 100

WIDTH = 800
HEIGHT = 600


def draw():
    screen.clear()
    butterfly.draw()


def update():
    butterfly.left += 2
    if butterfly.left > WIDTH:
        butterfly.right = 0

from rich import print

background = Actor('background')
background.pos = 600,400

butterfly = Actor('butterfly')
butterfly.pos = 100, 100

flower = Actor('flower')
flower.pos = 200, 200

flower2 = Actor('flower')
flower2.pos = 600, 300

flower3 = Actor('flower')
flower3.pos = 700, 500

flower4 = Actor('flower')
flower4.pos = 400, 150

WIDTH = 800
HEIGHT = 600

print(f"INFO: Starting [red]ButterflyGame[/red]")
print(f"INFO: Starting [green]Use arrow keys to move butterfly[/green]")


def draw():
    screen.fill((128, 0, 0))
    print(f"[yellow]INFO: draw[/yellow]")
    screen.clear()
    background.draw()
    flower.draw()
    flower2.draw()
    flower3.draw()
    flower4.draw()
    butterfly.draw()


def update():
    print(f"[yellow]INFO: update[/yellow]")
    if keyboard.up:
        print(f"[green]INFO: up[/green]")
        butterfly.top -= 1
        background.top += 1
    elif keyboard.down:
        print(f"[green]INFO: down[/green]")
        butterfly.top += 1
        background.top -= 1
    elif keyboard.right:
        print(f"[green]INFO: right[/green]")
        butterfly.right += 1
        background.right -= 1
    elif keyboard.left:
        print(f"[green]INFO: left[/green]")
        butterfly.left -= 1
        background.right += 1
    else:
        butterfly.left += .5
    if butterfly.left > WIDTH:
        butterfly.right = 0

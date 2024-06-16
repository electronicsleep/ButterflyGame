from rich import print

background = Actor('background')
background.pos = 0,0


butterfly = Actor('butterfly')
butterfly.pos = 100, 100

flower = Actor('flower')
flower.pos = 300, 200

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
    butterfly.draw()


def update():
    print(f"[yellow]INFO: update[/yellow]")
    if keyboard.up:
        print(f"[green]INFO: up[/green]")
        butterfly.top -= .5
    elif keyboard.down:
        print(f"[green]INFO: down[/green]")
        butterfly.top += .5
    elif keyboard.right:
        print(f"[green]INFO: right[/green]")
        butterfly.right += 1
    elif keyboard.left:
        print(f"[green]INFO: left[/green]")
        butterfly.left -= .5
    else:
        butterfly.left += .5

    if butterfly.left > WIDTH:
        butterfly.right = 0

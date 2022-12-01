from rich import print
butterfly = Actor('butterfly')
butterfly.pos = 100, 100

WIDTH = 800
HEIGHT = 600

print(f"INFO: Starting [red]ButterflyGame[/red]")
print(f"INFO: Starting [green]Use arrow keys to move butterfly[/green]")


def draw():
    print(f"[yellow]INFO: draw[/yellow]")
    screen.clear()
    butterfly.draw()


def update():
    print(f"[yellow]INFO: update[/yellow]")
    if keyboard.up:
        print(f"[green]INFO: up[/green]")
        butterfly.top -= 1
    elif keyboard.down:
        print(f"[green]INFO: down[/green]")
        butterfly.top += 1
    elif keyboard.right:
        print(f"[green]INFO: right[/green]")
        butterfly.right += 2
    elif keyboard.left:
        print(f"[green]INFO: left[/green]")
        butterfly.left -= 1
    else:
        butterfly.left += 1

    if butterfly.left > WIDTH:
        butterfly.right = 0

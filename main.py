from rich import print
butterfly = Actor('butterfly')
butterfly.pos = 100, 100

WIDTH = 800
HEIGHT = 600

print(f"Starting [red]ButterflyGame[/red]")
print(f"Starting [green]Use Right/Left arrow keys[/green]")

def draw():
    screen.clear()
    butterfly.draw()


def update():
    if keyboard.right:
        print(f"[green]right[/green]")
        butterfly.right += 1
    if keyboard.left:
        print(f"[green]left[/green]")
        butterfly.left -= 1
    butterfly.left += 1
    if butterfly.left > WIDTH:
        butterfly.right = 0

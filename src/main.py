from rich import print
import time


WIDTH = 800
HEIGHT = 600

MAIN_COLOR = 'yellow'
CYAN = (0, 255, 255)

background = Actor('background')
background.pos = 600, 400

butterfly = Actor('butterfly')
butterfly.pos = 100, 100

# DEBUG BOX
GREEN = (0, 255, 0)
BOX = Rect((20, 20), (100, 100))

level = 0

flower_pos = ()
flower2_pos = ()
flower3_pos = ()
flower4_pos = ()
flowers_pos = {}
flower_score = {}


def level_reset(level):
    global flower_pos
    global flower2_pos
    global flower3_pos
    global flower4_pos
    global flowers_pos
    global flower_score
    global butterfly

    butterfly.pos = 100, 100

    if level == 1:
        flower_pos = (200, 200)
        flower2_pos = (300, 300)
        flower3_pos = (900, 900)
        flower4_pos = (900, 900)
        flowers_pos = {'flower': flower_pos, 'flower2': flower2_pos}
        flower_score = {"flower": 0, "flower2": 0}

    if level == 2:
        flower_pos = (250, 200)
        flower2_pos = (300, 350)
        flower3_pos = (900, 900)
        flower4_pos = (900, 900)
        flowers_pos = {'flower': flower_pos, 'flower2': flower2_pos}
        flower_score = {"flower": 0, "flower2": 0}

    elif level == 2:
        flower_pos = (200, 200)
        flower2_pos = (300, 300)
        flower3_pos = (400, 400)
        flower4_pos = (100, 100)
        flowers_pos = {'flower': flower_pos, 'flower2': flower2_pos, 'flower3': flower3_pos}
        flower_score = {"flower": 0, "flower2": 0, "flower3": 0}

    elif level == 3:
        flower_pos = (200, 200)
        flower2_pos = (300, 300)
        flower3_pos = (400, 400)
        flower4_pos = (400, 200)
        flowers_pos = {'flower': flower_pos, 'flower2': flower2_pos, 'flower3': flower3_pos, 'flower4': flower4_pos}
        flower_score = {"flower": 0, "flower2": 0, "flower3": 0, "flower4": 0}

    elif level == 4:
        flower_pos = (450, 400)
        flower2_pos = (350, 350)
        flower3_pos = (250, 250)
        flower4_pos = (500, 550)
        flowers_pos = {'flower': flower_pos, 'flower2': flower2_pos, 'flower3': flower3_pos, 'flower4': flower4_pos}
        flower_score = {"flower": 0, "flower2": 0, "flower3": 0, "flower4": 0}

    elif level == 5:
        flower_pos = (400, 400)
        flower2_pos = (300, 300)
        flower3_pos = (200, 200)
        flower4_pos = (500, 500)
        flowers_pos = {'flower': flower_pos, 'flower2': flower2_pos, 'flower3': flower3_pos, 'flower4': flower4_pos}
        flower_score = {"flower": 0, "flower2": 0, "flower3": 0, "flower4": 0}

    elif level == 6:
        flower_pos = (500, 200)
        flower2_pos = (300, 500)
        flower3_pos = (400, 300)
        flower4_pos = (300, 200)
        flowers_pos = {'flower': flower_pos, 'flower2': flower2_pos, 'flower3': flower3_pos, 'flower4': flower4_pos}
        flower_score = {"flower": 0, "flower2": 0, "flower3": 0, "flower4": 0}

    flower.pos = flower_pos[0], flower_pos[1]
    flower2.pos = flower2_pos[0], flower2_pos[1]
    flower3.pos = flower3_pos[0], flower3_pos[1]
    flower4.pos = flower4_pos[0], flower4_pos[1]


def draw():
    global flower_score
    global level
    total_score = 0
    screen.fill((128, 0, 0))
    print("[yellow]INFO: draw[/yellow]")
    screen.clear()
    background.draw()
    if level == 1:
        flower.draw()
        flower2.draw()
    elif level == 2:
        flower.draw()
        flower2.draw()
        flower3.draw()
    else:
        flower.draw()
        flower2.draw()
        flower3.draw()
        flower4.draw()
    butterfly.draw()
    print(butterfly.pos)
    print(flower_pos)
    score_y = False

    # Check each flower position against the butterfly
    for flower_key, flower_pos_val in flowers_pos.items():
        print(f"flower_key: {flower_key} flower_pos_val: {flower_pos_val}")
        # DEBUG: Box flower pos
        # BOX = Rect((flower_pos_val[0], flower_pos_val[1]), (25, 25))
        # screen.draw.rect(BOX, GREEN)
        score_x = False
        score_y = False
        print("flower_pos_val_0", flower_pos_val[0])
        print("butterfly_pos_0", butterfly.pos[0])
        if butterfly.pos[0] >= flower_pos_val[0] - 50 and butterfly.pos[0] <= flower_pos_val[0] - 10:
            score_x = True
            print("score_x", score_x)
        if butterfly.pos[1] >= flower_pos_val[1] - 50 and butterfly.pos[1] <= flower_pos_val[1] + 0:
            score_y = True
            print("score_y", score_y)
        if score_x and score_y:
            add_score(flower_score, flower_key)
            print("add score")

    total_score = get_score(flower_score)

    result = check_level(flower_score, total_score)

    if result:
        screen.draw.text(
            'Game Completed',
            center=(WIDTH // 2, 20),
            color=CYAN,
            fontsize=40,
            fontname="lcd_solid"
        )
    else:
        screen.draw.text(
            'Level: ' + str(level) + ' Score: ' + str(total_score) + ' Butterfly_pos  ' + str(butterfly.pos),
            center=(WIDTH // 2, 20),
            color=CYAN,
            fontsize=20,
            fontname="lcd_solid"
        )


def add_score(flower_score, flower_key):
    flower_score[flower_key] = 1


def get_score(flower_score):
    total_score = 0
    for key, value in flower_score.items():
        total_score += value
    # print(f"DEBUG: check level {flower_score} {total_score}")
    return total_score


def check_level(flower_score, total_score):
    total_flowers = len(flower_score)
    if total_flowers == total_score:
        print("Level Finished")
        global level
        if (level < 6):
            level += 1
            time.sleep(1)
            level_reset(level)
            return False
        else:
            print("Game Finished")
            time.sleep(1)
            return True
        

def pause():
    print("POS", butterfly.pos)
    for i in range(0, 5):
        print("pause: ", i)
        if keyboard.u:
            break


def update():
    print(f"[yellow]INFO: update[/yellow]")
    if keyboard.up:
        butterfly.top -= 2
    elif keyboard.down:
        butterfly.top += 2
    elif keyboard.right:
        butterfly.right += 2
    elif keyboard.left:
        butterfly.left -= 2
    elif keyboard.p:
        pause()
    else:
        butterfly.left += .5
    if butterfly.left > WIDTH:
        butterfly.right = 0


flower = Actor('flower')
flower2 = Actor('flower')
flower3 = Actor('flower')
flower4 = Actor('flower')

level += 1
level_reset(level)

total_score = 0

print("INFO: Starting [red]ButterflyGame[/red]")
print("INFO: Starting [green]Use arrow keys to move butterfly[/green]")

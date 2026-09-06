import pgzrun
import random 

WIDTH = 800
HEIGHT = 600
CENTRE_X = 400
CENTRE_Y = 300
CENTRE = (CENTRE_X,CENTRE_Y)
TITLE = "Recycle world"
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["bottle","battery","plastic","chips"]

game_over = False 
game_complete = False
current_level = 1

items = []
animations = []

def draw():
    screen.clear()
    screen.blit("bg", (0,0))

def update():
    pass

def get_option(extra_items):
    items_to_create = ["paper"]
    for i in range (extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
       item = Actor(option + "img")  
       new_items.append(item)
    return new_items

pgzrun.go()



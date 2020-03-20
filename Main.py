""" In this file, our main program"""

# importing those modules relates this file to Classes.py file
from Structure import maze_structure
from Classes import *

pygame.init()

# our game screen will have those pixels measures
resolution = (600, 600)
# game's title
pygame.display.set_caption("MacGyver's Maze")
screen = pygame.display.set_mode(resolution)

# variables containing some images of our maze
wall = pygame.image.load("ressource/wall.png")
floor = pygame.image.load("ressource/floor.png")


# function creating the maze
def maze():
    coord_y = 0
    for element in maze_structure:
        coord_x = 0
        for letter in element:
            if letter == "X":
                coord_list_x.append((coord_x, coord_y))
                screen.blit(wall, (coord_x, coord_y))
                coord_x += 40
            elif letter == " ":
                coord_list_s.append((coord_x, coord_y))
                screen.blit(floor, (coord_x, coord_y))
                coord_x += 40
            elif letter == "D":
                screen.blit(floor, (coord_x, coord_y))
                coord_x += 40
            elif letter == "A":
                screen.blit(floor, (coord_x, coord_y))
                coord_x += 40
        coord_y += 40


maze()

# removes some coordinates we do not want in our list
coord_list_s.pop(-1)
coord_list_s.pop(-2)

# WE generates all our sprites at once
game = Game()

# we ensure that the 3 items will have different coordinates
while game.tube.pos == game.ether.pos:
    game.tube.pos = coord_list_s[randrange(0, len(coord_list_s))]
while game.sting.pos == game.ether.pos or game.sting.pos == game.tube.pos:
    game.sting.pos = coord_list_s[randrange(0, len(coord_list_s))]

# some statements in order to make appear these items in the maze
ether = True
tube = True
sting = True
syringe = False
warden = True

# variable for our while loop
run = True

while run:
    maze()

    # MacGyver appears in the maze
    screen.blit(game.player.image, game.player.rect)

    if ether is True:
        screen.blit(game.ether.image, game.ether.pos)

    if tube is True:
        screen.blit(game.tube.image, game.tube.pos)

    if sting is True:
        screen.blit(game.sting.image, game.sting.pos)

    if syringe is True:
        screen.blit(game.syringe.image, game.syringe.rect)

    if warden is True:
        screen.blit(game.warden.image, game.warden.rect)

    # for and if statements to detect instructions from keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            # MacGyver can move in all path but not further up from departure position
            if event.key == pygame.K_UP and (game.player.rect.x, game.player.rect.y - 40) not in coord_list_x and \
                    game.player.rect.y - 40 > -40:
                game.player.move("up")
            elif event.key == pygame.K_DOWN and (game.player.rect.x, game.player.rect.y + 40) not in coord_list_x:
                game.player.move("down")
            elif event.key == pygame.K_RIGHT and (game.player.rect.x + 40, game.player.rect.y) not in coord_list_x:
                game.player.move("right")
            elif event.key == pygame.K_LEFT and (game.player.rect.x - 40, game.player.rect.y) not in coord_list_x:
                game.player.move("left")

    # disappearance of items when MacGyver is on the same spot
    if game.player.rect == game.ether.rect:
        ether = False
    elif game.player.rect == game.tube.rect:
        tube = False
    elif game.player.rect == game.sting.rect:
        sting = False
    elif game.player.rect == game.syringe.rect:
        game.player.items = "full"

    # Syringe will appear when all other items will disappear
    if ether is False and tube is False and sting is False:
        syringe = True

    # Syringe will disappear again
    if ether is False and tube is False and sting is False and game.player.items == "full":
        syringe = False

    # warden will disappear
    if game.player.items == "full" and game.player.rect == game.warden.rect:
        warden = False

    # refresh our screen
    pygame.display.flip()

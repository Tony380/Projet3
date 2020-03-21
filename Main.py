import pygame
from Structure import maze_structure
from Classes import *

pygame.init()

resolution = (600, 600)
pygame.display.set_caption("Mac Gyver's Maze")
screen = pygame.display.set_mode(resolution)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

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
    coord_list_s.pop(-1)
    coord_list_s.pop(-2)

    game = Game()

    while game.tube.pos == game.ether.pos:
        game.tube.pos = coord_list_s[randrange(0, len(coord_list_s))]
    while game.sting.pos == game.ether.pos or game.sting.pos == game.tube.pos:
        game.sting.pos = coord_list_s[randrange(0, len(coord_list_s))]


    screen.blit(play, (0, 0))
    menu = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    menu = "p"
                elif event.key == pygame.K_e:
                    menu = "e"
                elif event.key == pygame.K_m:
                    menu = "m"
                elif event.key == pygame.K_UP and (
                        game.player.rect.x, game.player.rect.y - 40) not in coord_list_x and \
                        game.player.rect.y - 40 > -40:
                    game.player.move("up")
                elif event.key == pygame.K_DOWN and (
                        game.player.rect.x, game.player.rect.y + 40) not in coord_list_x:
                    game.player.move("down")
                elif event.key == pygame.K_RIGHT and (
                        game.player.rect.x + 40, game.player.rect.y) not in coord_list_x:
                    game.player.move("right")
                elif event.key == pygame.K_LEFT and (
                        game.player.rect.x - 40, game.player.rect.y) not in coord_list_x:
                    game.player.move("left")

        if menu == "p":
            maze()
            screen.blit(game.player.image, game.player.rect)

            if game.ether.show:
                screen.blit(game.ether.image, game.ether.pos)

            if game.tube.show:
                screen.blit(game.tube.image, game.tube.pos)

            if game.sting.show:
                screen.blit(game.sting.image, game.sting.pos)

            if game.syringe.show:
                screen.blit(game.syringe.image, game.syringe.rect)

            if game.warden.show:
                screen.blit(game.warden.image, game.warden.rect)

            if game.player.rect == game.ether.rect:
                game.ether.show = False
            elif game.player.rect == game.tube.rect:
                game.tube.show = False
            elif game.player.rect == game.sting.rect:
                game.sting.show = False
            elif game.player.rect == game.syringe.rect:
                if game.ether.show is False and game.tube.show is False and game.sting.show is False:
                    game.player.items = "full"

            if game.ether.show is False and game.tube.show is False and game.sting.show is False:
                game.syringe.show = True

            if game.ether.show is False and game.tube.show is False and game.sting.show\
                    is False and game.player.items == "full":
                game.syringe.show = False


            if game.player.items == "full" and game.player.rect == game.warden.rect:
                game.warden.show = False
                screen.blit(win, (0, 0))
            elif game.player.items == "empty" and game.player.rect == game.warden.rect:
                screen.blit(lose, (0, 0))


        elif menu == "m":
            break
        elif menu == "e":
            quit()

        pygame.display.flip()

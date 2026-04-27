import pygame
import random

class SomeClass():

    def method_1():
        ...

    def method_2():
        ...

    def method_n():
        ...




def main():
    pygame.init()


    pygame.display.set_caption("Dungeon & Cards")
    resolution = pygame.display.get_desktop_sizes()[0]
    screen = pygame.display.set_mode(resolution)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        

        black = pygame.Color(0,0,0)
        screen.fill(black)
        pygame.display.flip()





    pygame.quit()




if __name__ == "__main__":
    main()

import pygame
import random

class SomeClass():

    def method_1():
        ...

    def method_2():
        ...

    def method_n():
        ...

def text_font(font, text, color, x, y, screen):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def main_menu(font, screen):
    play_button = pygame.Rect(300, 200, 200, 50)
    quit_button = pygame.Rect(300, 300, 200, 50)

    pygame.draw.ellipse(screen, (0, 200, 0), play_button)
    pygame.draw.ellipse(screen, (200, 0, 0), quit_button)
    
    text_font(font, "DUNGEONS & CARDS!", (255,255,255), 215, 100, screen)
    text_font(font, "PLAY!", (255, 255, 255), 353, 208, screen)
    text_font(font, "QUIT!", (255, 255, 255), 353, 308, screen)
    

def main():
    pygame.init()
    pygame.font.init()


    pygame.display.set_caption("Dungeon & Cards")
    resolution = pygame.display.get_desktop_sizes()[0]
    screen = pygame.display.set_mode(resolution)


    text_font = pygame.font.SysFont(None, 50)


    
    running = True
    while running:
        screen_color = pygame.Color(68,105,254)
        screen.fill(screen_color)

        main_menu(text_font, screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()







    pygame.font.quit()
    pygame.quit()




if __name__ == "__main__":
    main()

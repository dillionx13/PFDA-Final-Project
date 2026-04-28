import pygame
import random

class SomeClass():

    def method_1():
        ...

    def method_2():
        ...

    def method_n():
        ...

class Button():
    def __init__(self, text, rect_size):
        self.text=text
        self.rect_size=rect_size
        self.left, self.top, self.width, self.height = rect_size
        self.rect = pygame.Rect(rect_size)
        font_size = int((self.width)*(self.height)/2)
        print(font_size)
        self.font= pygame.font.SysFont(None, 15)

    def setColor(self, color):
        self.color=color

    def setTextColor(self, textColor):
        self.textColor=textColor
    
    def collidepoint(self,point):
        return self.rect.collidepoint(point)

    def draw(self, screen):
        img = self.font.render(self.text, True, self.textColor)
        pygame.draw.ellipse(screen, self.color, self.rect)
        text_rect = img.get_rect(center=self.rect.center)
        screen.blit(img, text_rect)

def title(screen):
    title_font = pygame.font.SysFont(None, 150)
    img = title_font.render("DUNGEONS & CARDS!", True, (255,255,255))
    screen.blit(img, (215, 100))

def main():
    pygame.init()
    pygame.font.init()


    pygame.display.set_caption("Dungeon & Cards")
    resolution = pygame.display.get_desktop_sizes()[0]
    screen = pygame.display.set_mode(resolution)


    


    play_button = Button("PLAY!", (300, 1200, 600, 150))
    play_button.setColor((0, 200, 0))
    play_button.setTextColor((255, 255, 255))

    quit_button = Button("QUIT", (300, 300, 200, 50))
    quit_button.setColor((200, 0, 0))
    quit_button.setTextColor((255, 255, 255))

    return_button = Button("RETURN", (300, 1000, 200, 50))
    return_button.setColor((200, 0, 200))
    return_button.setTextColor((255, 255, 255))



    running = True
    playing = False

    while running:
        screen_color = pygame.Color(68,105,254)
        screen.fill(screen_color)

        if playing == False:
            title(screen)
            play_button.draw(screen)
            quit_button.draw(screen)
        else:
            return_button.draw(screen)
        
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and playing == False:
                if quit_button.collidepoint(mouse_pos):
                    running = False
                if play_button.collidepoint(mouse_pos):
                    playing = True
            elif event.type == pygame.MOUSEBUTTONDOWN and playing == True:
                if return_button.collidepoint(mouse_pos):
                    playing = False
        pygame.display.update()







    pygame.font.quit()
    pygame.quit()




if __name__ == "__main__":
    main()

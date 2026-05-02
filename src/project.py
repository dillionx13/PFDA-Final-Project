import pygame
import random

class SomeClass():

    def __init__(self):
        ...

    def method_2():
        ...

    def method_n():
        ...

class Cards():

    def __init__(self, pos, text, description, color):
        self.text = text
        self.pos = pos
        self.description = description
        self.text_color = color
        self.card_background = pygame.transform.scale_by(pygame.image.load("card_template.png"), 1)
        
        self.font = pygame.font.SysFont(None, 49)
        self.description_font = pygame.font.SysFont(None, 35)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(midtop=self.card_background.get_rect().midtop)
        text_rect.y += 5
        self.card_background.blit(text_surface, text_rect)

        desc_surface = self.description_font.render(self.description, True, self.text_color)
        desc_rect = desc_surface.get_rect(midbottom=self.card_background.get_rect().midbottom)
        desc_rect.y += -25        
        self.card_background.blit(desc_surface,desc_rect)

        number_font = pygame.font.SysFont(None, 45)
        circle_rect = pygame.Rect(0, 0, 50 * 2, 50 * 2)
        circle_rect.x += -28
        circle_rect.y += -6
        number_surf = number_font.render("5", True, (255, 255, 255))
        number_rect = number_surf.get_rect(center=circle_rect.center)
        self.card_background.blit(number_surf,number_rect)
        

        self.rect = self.card_background.get_rect(topleft=pos)


    def draw(self, screen):
        screen.blit(self.card_background, self.rect)

class Button():
    def __init__(self, text, rect_size, font_size =125):
        self.text= text
        self.rect_size= rect_size
        self.rect = pygame.Rect(rect_size)
        self.font= pygame.font.SysFont(None, font_size)

    def set_color(self, color):
        self.color=color

    def set_text_color(self, textColor):
        self.textColor=textColor
    
    def collidepoint(self,point):
        return self.rect.collidepoint(point)

    def draw(self, screen):
        text_render = self.font.render(self.text, True, self.textColor)
        pygame.draw.ellipse(screen, self.color, self.rect)
        text_rect = text_render.get_rect(center=self.rect.center)
        screen.blit(text_render, text_rect)

def game_screen(screen):
    hand_rect = pygame.Rect((550, 1200, 600, 150))

def title(screen):
    title_font = pygame.font.SysFont(None, 200)
    text_render = title_font.render("DUNGEONS & CARDS!", True, (255,255,255))
    screen.blit(text_render, (215, 100))

def main():
    pygame.init()
    pygame.font.init()


    pygame.display.set_caption("Dungeon & Cards")
    resolution = pygame.display.get_desktop_sizes()[0]
    screen = pygame.display.set_mode(resolution)


    


    play_button = Button("PLAY!", (550, 1200, 600, 150), 125)
    play_button.set_color((0, 200, 0))
    play_button.set_text_color((255, 255, 255))

    quit_button = Button("QUIT", (1550, 1200, 600, 150), 125)
    quit_button.set_color((200, 0, 0))
    quit_button.set_text_color((255, 255, 255))

    return_button = Button("RETURN", (25, 25, 200, 50), 35)
    return_button.set_color((200, 0, 200))
    return_button.set_text_color((255, 255, 255))

    card = Cards((160,160), "Fireball", "Deal 60 Damage", (255,255,255))
    card.rect.x += 1000
    card.rect.y += 900

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
            card.draw(screen)
            
        
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

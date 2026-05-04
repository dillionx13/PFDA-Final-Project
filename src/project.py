import pygame
import random

class GameArea():
    def __init__(self, text):
        self.message = text

    
    def draw(self, screen):
        rect = pygame.Rect((300,300,2000,500))
        font = pygame.font.SysFont(None, 100)
        text_render = font.render(self.message, True, (255,255,255))
        pygame.draw.rect(screen, (0,25,255), rect, 10)
        text_rect = text_render.get_rect(center=rect.center)
        screen.blit(text_render, text_rect)

class Opponent():
    def __init__(self):
        self.max_health = 100
        self.health = self.max_health

class Player():
    def __init__(self):
        self.max_health = 100
        self.health = self.max_health
        self.max_energy = 9
        self.energy = 5
        self.hand_max = 3
        self.hand = []
        self.card_deck = CardDeck()

    def fill_hand(self):
        if len(self.hand) < 3:
            for _ in range(0, self.hand_max):
                self.hand.append(self.card_deck.pick_card_from_deck())

class Card():

    def __init__(self, dictionary, color):
        self.text = dictionary["name"]
        self.description = dictionary["description"]
        self.cost = dictionary["cost"]
        self.text_color = color    
        self.card_background = pygame.transform.scale_by(pygame.image.load("card_template.png"), 1) 
        self.face = self.card_background.copy()
        self.rect = self.face.get_rect()  
        self.build_card()
        self.selected = False

    def collidepoint(self,point):
        return self.rect.collidepoint(point)
    
    def build_card(self):
        self.face = self.card_background.copy()

        self.font = pygame.font.SysFont(None, 49)
        self.description_font = pygame.font.SysFont(None, 35)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(midtop=self.card_background.get_rect().midtop)
        text_rect.y += 5
        self.face.blit(text_surface, text_rect)

        desc_surface = self.description_font.render(self.description, True, self.text_color)
        desc_rect = desc_surface.get_rect(midbottom=self.card_background.get_rect().midbottom)
        desc_rect.y += -25        
        self.face.blit(desc_surface, desc_rect)

        number_font = pygame.font.SysFont(None, 45)
        circle_rect = pygame.Rect(0, 0, 50 * 2, 50 * 2)
        circle_rect.x += -28
        circle_rect.y += -6
        number_surf = number_font.render(str(self.cost), True, self.text_color)
        number_rect = number_surf.get_rect(center=circle_rect.center)
        self.face.blit(number_surf,number_rect)
        


    def draw(self, pos, screen):
        self.rect.topleft = pos
        screen.blit(self.face, self.rect)

class CardDictionary():
    dictionary = {
        "Fireball": {"name": "Fireball", "cost": 3, "description": "Deal 8d6 Damage"},
        "Call Lightning": {"name": "Call Lightning", "cost": 3, "description": "Deal 3d10 Damage"},
        "Eldritch Blast": {"name": "Eldritch Blast", "cost": 1, "description": "Deal 1d8 Damage"},
        "Mind Spike": {"name": "Mind Spike", "cost": 2, "description": "Deal 3d8 Damage"}
    }
    def get_item(self, name):
        return self.dictionary[name]
    
    def get_dictionary(self):
        return self.dictionary

class CardDeck():
    def __init__(self): 
        self.card_in_hand = [] 
        self.card_deck = self.build_deck()
        
    def build_deck(self):
        card_list = [] 
        card_dictionary = CardDictionary()
        num_card_max = 3
        for _ in range(1, num_card_max + 1):
            for index in range(0, len(card_dictionary.get_dictionary())):
                dictionary = list(card_dictionary.get_dictionary().values())[index]
                self.create_card(dictionary, card_list)

        random.shuffle(card_list)
        return card_list

    def create_card(self, dictionary, card_list):
        card = Card(dictionary, (255,255,255))
        card_list.append(card)

    def pick_card_from_deck(self):
        if (len(self.card_deck) > 0):
            card = self.card_deck.pop(0)
            self.card_in_hand.append(card)
            return card
        else:
            return None

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
    
    def set_text(self, text):
        self.text = text

    def draw(self, shape, screen):
        text_render = self.font.render(self.text, True, self.textColor)
        if shape == "rect":
            pygame.draw.rect(screen, self.color, self.rect)
        else:
            pygame.draw.ellipse(screen, self.color, self.rect)
        text_rect = text_render.get_rect(center=self.rect.center)
        screen.blit(text_render, text_rect)

def game_screen(player, opponent, screen):
    hand_rect = pygame.Rect((800, 1100, 1000, 340))
    pygame.draw.rect(screen, (0,155,0), hand_rect)

    card_spacing = 350
    for index, card in enumerate(player.hand):
        card_x = hand_rect.x + (index * card_spacing) + 38
        card_y = hand_rect.y + 10
        card.rect.topleft = (card_x, card_y)
        screen.blit(card.face, card.rect)
    
    energy_font = pygame.font.SysFont(None, 125)
    energy_render = energy_font.render(f"Energy:\n      {player.energy}", True, (255,255,255))
    energy_rect = pygame.Rect((150, 1065, 375, 375))
    pygame.draw.ellipse(screen, (18,76,255), energy_rect)
    text_rect = energy_render.get_rect(center=energy_rect.center)
    screen.blit(energy_render, text_rect)

    health_font = pygame.font.SysFont(None, 75)
    health_render = health_font.render(f"Your HP: {player.health}", True, (255,255,255))
    health_rect = pygame.Rect((800, 1000, 500, 100))
    text_rect = health_render.get_rect(center=health_rect.center)
    pygame.draw.rect(screen, (200,0,0), health_rect)
    screen.blit(health_render, text_rect)

    opponent_font = pygame.font.SysFont(None, 125)
    opponent_health_render = opponent_font.render(f"Opponent HP: {opponent.health}", True, (255,255,255))
    opponent_rect = pygame.Rect((880, 50, 800, 100))
    pygame.draw.rect(screen, (255,0,0), opponent_rect)
    text_rect = opponent_health_render.get_rect(center=opponent_rect.center)
    screen.blit(opponent_health_render, text_rect)

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

    deck_button = Button("Deck", ((2000, 1065, 375, 375)), 125)
    deck_button.set_color((155,155,155))
    deck_button.set_text_color((255, 255, 255))

    turn_button = Button("Play Turn", ((1300, 1000, 500, 100)), 125)
    turn_button.set_color((155,155,155))
    turn_button.set_text_color((255, 255, 255))

    game_area = GameArea("")
    

    running = True
    playing = False
    

    while running:
        screen_color = pygame.Color(68,105,254)
        screen.fill(screen_color)

        if playing == False:
            title(screen)
            play_button.draw("ellipse", screen)
            quit_button.draw("ellipse",screen)
        else:
            game_screen(player,opponent, screen)
            return_button.draw("ellipse",screen)
            deck_button.draw("rect",screen)
            turn_button.draw("rect", screen)
            game_area.draw(screen)

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and playing == False:
                if quit_button.collidepoint(mouse_pos):
                    running = False
                if play_button.collidepoint(mouse_pos):
                    player = Player()
                    deck_button.set_text(f"Deck: {len(player.card_deck.card_deck)}")
                    opponent = Opponent()
                    game_area.message = "Click Deck to Start Game!"
                    playing = True
            elif event.type == pygame.MOUSEBUTTONDOWN and playing == True:
                if return_button.collidepoint(mouse_pos):
                    playing = False
                if deck_button.collidepoint(mouse_pos):
                    player.fill_hand()
                    deck_button.set_text(f"Deck: {len(player.card_deck.card_deck)}")
                    game_area.message = "Select Cards to Play Turn"
                for card in player.hand:
                    if card.collidepoint(mouse_pos):
                        if card.selected:
                            card.build_card()
                            card.selected = False
                            player.energy = player.energy + card.cost
                            game_area.message = "Select Cards to Play Turn"
                        else:
                            total_energy_left = player.energy - card.cost
                            if total_energy_left < 0:
                                game_area.message = "Not Enough Energy to Select"
                            else:
                                player.energy = player.energy - card.cost
                                check_mark = pygame.transform.scale_by(pygame.image.load("check_mark.png"), 0.5)
                                check_mark_rect = check_mark.get_rect(center=card.face.get_rect().center)
                                check_mark_rect.y -= 20
                                card.face.blit(check_mark,check_mark_rect)
                                game_area.message = "Select Cards to Play Turn"
                                card.selected = True
                    


        pygame.display.update()

    pygame.font.quit()
    pygame.quit()

if __name__ == "__main__":
    main()

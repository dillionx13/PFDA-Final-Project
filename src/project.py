import pygame
import random


class GameArea():
    def __init__(self, text):
        self.message = text

    
    def draw(self, screen):
        rect = pygame.Rect((300,175,2000,800))
        font = pygame.font.SysFont(None, 100)
        text_render = font.render(self.message, True, (255,255,255))
        pygame.draw.rect(screen, (0,25,255), rect, 10)
        text_rect = text_render.get_rect(center=rect.center)
        screen.blit(text_render, text_rect)

class Opponent():
    def __init__(self):
        self.max_health = 100
        self.health = self.max_health
        self.turn = False
        self.dictionary = CardDictionary()
        self.energy = 4
        
    def select_move(self):
        self.attack_key = random.choice(list(self.dictionary.get_dictionary().keys()))
        self.cost = (self.dictionary.get_dictionary()[self.attack_key]["cost"])

    def play_turn(self):
        self.select_move()
        while self.energy < self.cost:
            self.select_move()
        self.card_type = (self.dictionary.get_dictionary()[self.attack_key]["card_type"])
        
        points = roll_damage(self.dictionary.get_dictionary()[self.attack_key]["dice_amount"], self.dictionary.get_dictionary()[self.attack_key]["dice_type"])
        if self.card_type == "defense":
            self.health += points
            if self.health > self.max_health:
                self.health = self.max_health
        self.energy -= self.cost
        self.energy += 3
        return points
        
class Player():
    def __init__(self):
        self.max_health = 100
        self.health = self.max_health
        self.energy = 5
        self.hand_max = 3
        self.hand = []
        self.card_deck = CardDeck()
        self.turn = True
        self.selected_cards = []
        self.start = True
        self.played_cards = []

    def fill_hand(self):
        self.refill_deck = False
        if len(self.hand) < 3:
            for _ in range(0, self.hand_max-len(self.hand)):
                if len(self.card_deck.deck) == 0:
                    random.shuffle(self.played_cards)
                    self.card_deck.deck.extend(self.played_cards)
                    self.played_cards.clear()
                    self.refill_deck = True
                self.hand.append(self.card_deck.pick_card_from_deck())
                

    def play_turn(self):
        for card in self.selected_cards:
            self.hand.remove(card)
            self.played_cards.append(card)

        self.energy += 2

class Card():

    def __init__(self, dictionary, color):
        self.text = dictionary["name"]
        self.description = dictionary["description"]
        self.cost = dictionary["cost"]
        self.damage = roll_damage(dictionary["dice_amount"], dictionary["dice_type"])
        self.card_type = dictionary["card_type"]
        self.text_color = color
     
        if self.card_type == "attack":
            self.card_background = pygame.transform.scale_by(pygame.image.load("card_attack_template.png"), 1)
        else:
            self.card_background = pygame.transform.scale_by(pygame.image.load("card_defense_template.png"), 1)
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

        number_font = pygame.font.SysFont(None, 100)
        circle_rect = pygame.Rect(0, 0, 50 * 2, 50 * 2)
        circle_rect.x += 63
        circle_rect.y += 80
        number_surf = number_font.render(str(self.cost), True, self.text_color)
        number_rect = number_surf.get_rect(center=circle_rect.center)
        self.face.blit(number_surf,number_rect)
        
    def select_me(self):
        check_mark = pygame.transform.scale_by(pygame.image.load("check_mark.png"), 0.5)
        check_mark_rect = check_mark.get_rect(center=self.face.get_rect().center)
        check_mark_rect.y -= 20
        self.face.blit(check_mark,check_mark_rect)
        self.selected = True
    
    def unselect_me(self):
        self.build_card()
        self.selected = False

    def draw(self, pos, screen):
        self.rect.topleft = pos
        screen.blit(self.face, self.rect)

class CardDictionary():
    dictionary = {
        "Eldritch Blast": {"name": "Eldritch Blast", "cost": 0, "description": "Deal 1d8 Damage\n    (1-8 damage)", "dice_amount": 1, "dice_type": 8, "card_type": "attack"},
        "Inflict Wounds": {"name": "Inflict Wounds", "cost": 1, "description": "Deal 2d10 Damage\n    (2-20 damage)", "dice_amount": 2, "dice_type": 10, "card_type": "attack"},
        "Lesser Cure": {"name": " Lesser Cure", "cost": 1, "description": "Heal 2d8 HP\n    (2-16 HP)", "dice_amount": 2, "dice_type": 8, "card_type": "defense"},
        "Mind Spike": {"name": "Mind Spike", "cost": 2, "description": "Deal 3d8 Damage\n    (3-24 damage)", "dice_amount": 3, "dice_type": 8, "card_type": "attack"},
        "Fireball": {"name": "Fireball", "cost": 3, "description": "Deal 8d6 Damage\n    (8-48 damage)", "dice_amount": 8, "dice_type": 6, "card_type": "attack"},
        "Call Lightning": {"name": "Call Lightning", "cost": 3, "description": "Deal 11d4 Damage\n    (11-44 damage)", "dice_amount": 11, "dice_type": 4, "card_type": "attack"},
        "Cure Wounds": {"name": "Cure Wounds", "cost": 3, "description": "Heal 4d8 HP\n    (4-32 HP)", "dice_amount": 4, "dice_type": 8, "card_type": "defense"},
        "Blight": {"name": "Blight", "cost": 4, "description": "Deal 9d6 Damage\n    (9-54 damage)", "dice_amount": 9, "dice_type": 6, "card_type": "attack"},
        "Greater Cure": {"name": "Greater Cure", "cost": 5, "description": "Heal 6d8 HP\n    (6-48 HP)", "dice_amount": 6, "dice_type": 8, "card_type": "defense"},
        "Disintergrate": {"name": "Disintergrate", "cost": 6, "description": "Deal 10d6 Damage\n    (10-60 damage)", "dice_amount": 10, "dice_type": 6, "card_type": "attack"},
    }
    def get_item(self, name):
        return self.dictionary[name]
    
    def get_dictionary(self):
        return self.dictionary

class CardDeck():
    def __init__(self): 
        self.card_in_hand = [] 
        self.deck = self.build_deck()
        
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
        if (len(self.deck) > 0):
            card = self.deck.pop(0)
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

def roll_damage(dice_amount, dice_type):
    damage = random.randrange(dice_amount, ((dice_amount * dice_type) + 1))
    return damage 

def is_game_over(player, opponent):
    return player.health <= 0 or opponent.health <= 0

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

    # Sets display sizes
    pygame.display.set_caption("Dungeon & Cards")
    resolution = pygame.display.get_desktop_sizes()[0]
    screen = pygame.display.set_mode(resolution)

    # Buttons on main screen
    play_button = Button("PLAY!", (550, 1200, 600, 150), 125)
    play_button.set_color((0, 200, 0))
    play_button.set_text_color((255, 255, 255))

    quit_button = Button("QUIT", (1550, 1200, 600, 150), 125)
    quit_button.set_color((200, 0, 0))
    quit_button.set_text_color((255, 255, 255))

    # Buttons on game screen
    return_button = Button("RETURN", (25, 25, 200, 50), 35)
    return_button.set_color((200, 0, 200))
    return_button.set_text_color((255, 255, 255))

    deck_button = Button("Deck", ((2000, 1065, 375, 375)), 125)
    deck_button.set_color((155,155,155))
    deck_button.set_text_color((255, 255, 255))

    turn_button = Button("Play Turn", ((1300, 1000, 500, 100)), 125)
    turn_button.set_color((155,155,155))
    turn_button.set_text_color((255, 255, 255))

    # Message Screen in game
    game_area = GameArea("")
    
    # Game Flags
    running = True
    playing = False

    # Game Players 
    opponent = None
    player = None

    # Prevents adding mutliple "Click to Draw"
    draw_reminder = 0
    main_music = 0
    losing_music = 0
    winning_music = 0
    
    # Game Starts
    while running:
        # Background
        screen_color = pygame.Color(68,105,254)
        screen.fill(screen_color)
        if main_music == 0:
            pygame.mixer.music.load("main_menu.mp3")
            pygame.mixer.music.play(loops=-1)
            main_music += 1

        
        # Draws menu screens
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
            

        # Keeps track of mouse position
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playing == False:
                    if quit_button.collidepoint(mouse_pos):
                        running = False
                    if play_button.collidepoint(mouse_pos):
                        losing_music = 0
                        winning_music = 0
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        pygame.mixer.music.load("battle.mp3")
                        pygame.mixer.music.play(loops=-1)
                        player = Player()
                        deck_button.set_text(f"Deck: {len(player.card_deck.deck)}")
                        opponent = Opponent()
                        game_area.message = "Click Deck to Start Game!"
                        playing = True
                elif playing == True:
                    if return_button.collidepoint(mouse_pos):
                        playing = False
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        main_music = 0
                        
                        
                    if is_game_over(player, opponent) == False:
                        if player.turn == True:
                            if len(player.hand) < player.hand_max:
                                if deck_button.collidepoint(mouse_pos):
                                    player.fill_hand()
                                    player.start = False
                                    deck_button.set_text(f"Deck: {len(player.card_deck.deck)}")
                                    game_area.message = "Select Cards and/or Click Play Turn When Ready"
                                    if player.refill_deck:
                                        game_area.message += "\n\nDeck Refilled!"
                                    draw_reminder = 0
                                elif draw_reminder == 0:
                                    game_area.message += ("\n\nClick Deck to Draw")
                                    draw_reminder += 1

                                
                            else:
                                for card in player.hand:
                                    if card.collidepoint(mouse_pos):
                                        if card.selected:
                                            card.unselect_me()
                                            player.energy = player.energy + card.cost
                                            game_area.message = "Select Cards and/or Click Play Turn When Ready"
                                            player.selected_cards.remove(card)
                                        else:
                                            total_energy_left = player.energy - card.cost
                                            if total_energy_left < 0:
                                                game_area.message = "Not Enough Energy.\n Select a Different Card or Play Turn"
                                            else:
                                                player.energy = player.energy - card.cost
                                                card.select_me()
                                                game_area.message = "Select Cards and/or Click Play Turn When Ready"
                                                player.selected_cards.append(card)
                                if player.start == False and turn_button.collidepoint(mouse_pos):
                                    game_area.message = ""
                                    player.play_turn()
                                    if len(player.selected_cards) > 0:
                                        for card in player.selected_cards:
                                            if card.card_type == "attack":
                                                game_area.message += f"You casted {card.text}, dealing {card.damage} damage\n"
                                                opponent.health -= card.damage
                                            elif card.card_type == "defense":
                                                game_area.message += f"You casted {card.text}, healing {card.damage} HP\n"
                                                player.health += card.damage
                                                if player.health > player.max_health:
                                                    player.health = player.max_health
                                            card.unselect_me()
                                        player.selected_cards.clear()
                                    opponent.turn = True

        if opponent and opponent.turn and opponent.health > 0: 
            opponent_damage = opponent.play_turn()
            if opponent.card_type == "attack":
                player.health -= opponent_damage
                game_area.message += f"\nOpponent casted with {opponent.attack_key}, dealing {opponent_damage} damage\n"
            else:
                game_area.message += f"\nOpponent casted with {opponent.attack_key}, healing {opponent_damage} HP\n"
            opponent.turn = False
            player.turn = True
            game_area.message += "\nGained +2 Energy. Your Turn!"

        if player and player.health <= 0:
            game_area.message = "\nGame Over. You Died...\n Press Return to Start New Game"
            if losing_music == 0:
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                pygame.mixer.music.load("lost.mp3")
                pygame.mixer.music.play(loops=-1)
                losing_music += 1
        if opponent and opponent.health <= 0:
            game_area.message = "\nGame Over. Victory!\n Press Return to Start New Game"
            if winning_music == 0:
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                pygame.mixer.music.load("victory.mp3")
                pygame.mixer.music.play(loops=-1)
                winning_music += 1

        
                    


        pygame.display.update()

    pygame.font.quit()
    pygame.quit()

if __name__ == "__main__":
    main()

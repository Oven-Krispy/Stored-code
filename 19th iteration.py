import random
# allows the use of random integers when dealing and shuffling cards 
import pygame
# allows use of the display
import time
# allows the use of time.sleep in order to make play more realistic

# Card class
class Card:
    suits = {'Hearts': 'H', 'Diamonds': 'D', 'Clubs': 'C', 'Spades': 'S'}
    # a dictionary containing ties between the suits and the letter to represent them
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    # an array which contains the possible card values

    def __init__(self, suit, value):
        self.suit = suit
        # initiates the suit attribute
        self.value = value
        # initiates the value attribute


# Deck class
import random

class Deck:
    def __init__(self):
        self.reset_deck()

    def reset_deck(self):
        self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]
        # Create a card for every possible suit and value combination
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
        # Shuffle the deck

    def draw(self):
        if not self.cards:
            self.reset_deck()
        return self.cards.pop()
        # Remove and return the top card from the deck, and reset if empty


# Player class
class Player:
    def __init__(self, name):
        self.name = name
        # initiates the attribute 'name' e.g. human or AI
        self.hand = []
        # makes the player's hand an empty array

    def draw(self, deck):
        self.hand.append(deck.draw())
        # adds the drawn card to the player's hand array

    def reset_hand(self):
        self.hand = []
        # removes all cards from the player's hand

# Main menu class  
class MainMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.font = pygame.font.Font(None, 64)
        self.small_font = pygame.font.Font(None, 24)
        self.start_button_rect = pygame.Rect(290, 350, 220, 90)
        self.title_rect = pygame.Rect(160, 100, 480, 90)
        self.button_colour = (140, 27, 3)
        self.text_colour = (255, 255, 255)
        self.cross_colour = (0, 0, 0)
        self.mode_text = "Tournament (1)"
        self.rules_text = ["Antes (0)", "Jackpots (9)", "6 and 9 (8)", "Purposeful pre-flop (7)", "Top and tails (6)"]
        self.titles_text = ["Rules", "Mode"]
        self.checklist_back_left = pygame.Rect(20, 220, 240, 340)
        self.checklist_back_right = pygame.Rect(540, 250, 240, 300)
        self.crosses_displayed = [False] * 6

    def run(self):
        clock = pygame.time.Clock()
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.handle_keydown(event.key)

            self.screen.fill((0, 128, 0))
            self.draw_fixed_elements()
            self.draw_crosses()
            clock.tick(60)  
            pygame.display.flip()

    def handle_keydown(self, key):
        if key == pygame.K_s:
            self.running = False
        elif pygame.K_0 <= key <= pygame.K_1 or pygame.K_6 <= key <= pygame.K_9:
            index = [pygame.K_0, pygame.K_9, pygame.K_8, pygame.K_7, pygame.K_6, pygame.K_1].index(key)
            self.crosses_displayed[index] = not self.crosses_displayed[index]

    def draw_fixed_elements(self):
        pygame.draw.rect(self.screen, self.button_colour, self.checklist_back_left)
        pygame.draw.rect(self.screen, self.button_colour, self.checklist_back_right)

        for count in range(5):
            pygame.draw.rect(self.screen, self.text_colour, (40, 275 + count * 60, 20, 20))

        pygame.draw.rect(self.screen, self.text_colour, (560, 395, 20, 20))
        pygame.draw.rect(self.screen, self.button_colour, self.title_rect)
        pygame.draw.rect(self.screen, self.button_colour, self.start_button_rect)
        
        self.draw_text_elements()

    def draw_crosses(self):
        positions = [(60, 295), (60, 355), (60, 415), (60, 475), (60, 535), (580, 415)]
        for i, pos in enumerate(positions):
            if self.crosses_displayed[i]:
                pygame.draw.line(self.screen, self.cross_colour, pos, (pos[0] - 20, pos[1] - 20), 3)
                pygame.draw.line(self.screen, self.cross_colour, (pos[0] - 20, pos[1]), (pos[0], pos[1] - 20), 3)

    def draw_text_elements(self):
        for count in range(2):
            titles_text = self.font.render(self.titles_text[count], True, self.text_colour)
            self.screen.blit(titles_text, (self.checklist_back_left.x + 50 + count * 520, self.checklist_back_left.y + 10 + count * 40))
        
        for count in range(5):
            checkbox_text = self.small_font.render(self.rules_text[count], True, self.text_colour)
            self.screen.blit(checkbox_text, (self.checklist_back_left.x + 50, self.checklist_back_left.y + 58 + (count * 60)))

        checkbox_text = self.small_font.render(self.mode_text, True, self.text_colour)
        self.screen.blit(checkbox_text, (self.checklist_back_right.x + 50, self.checklist_back_right.y + 148))

        text = self.font.render('Texas Hold\'em poker', True, self.text_colour)
        self.screen.blit(text, (self.title_rect.x + 25, self.title_rect.y + 25))
        
        text = self.font.render('Start (S)', True, self.text_colour)
        self.screen.blit(text, (self.start_button_rect.x + 25, self.start_button_rect.y + 25))



# Texas Hold'em game
class TexasHoldem:
    def __init__(self):
        self.setup_game_variables()
        self.setup_pygame()

    def setup_game_variables(self):
        self.deck = Deck()
        self.players = [Player('Human'), Player('AI')]
        self.community_cards = []
        self.back_colour = (140, 27, 3)
        self.button_text = ["Rules (R)", "Exit (E)"]
        self.font = pygame.font.Font(None, 45)
        self.small_font = pygame.font.Font(None, 30)
        self.large_font = pygame.font.Font(None, 150)
        self.top_buttons = pygame.Rect(20, 40, 140, 60)
        self.initial_funds = 1000
        self.pot_total = 0
        self.funds_box = pygame.Rect(560, 480, 220, 50)
        self.available_options = ["Call (C)", "Check (K)", "Bet (B)"]
        self.white_text = (255, 255, 255)
        self.yellow_text = (226, 178, 8)
        self.bet = 0
        self.funds = 1000

    def setup_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

    def deal(self):
        for player in self.players:
            player.draw(self.deck)
            player.draw(self.deck)

    def deal_community_card(self, count):
        self.community_cards += [self.deck.draw() for _ in range(count)]
        self.display_community_cards()

    def draw_card(self, card, x, y, face_up=True):
        if not self.screen:
            return
        card_width, card_height = 70, 110
        font = pygame.font.Font(None, 36)
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, card_width, card_height))
        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, card_width, card_height), 2)

        if face_up:
            color = (255, 0, 0) if card.suit in ['Hearts', 'Diamonds'] else (0, 0, 0)
            value_text = font.render(card.value, True, color)
            suit_text = font.render(Card.suits[card.suit], True, color)

            value_x = x + (1 if card.value == '10' else 6)
            bottom_value_x = x + (43 if card.value == '10' else 48)

            self.screen.blit(value_text, (value_x, y + 8))
            self.screen.blit(suit_text, (x + 24, y + 45))
            self.screen.blit(value_text, (bottom_value_x, y + 85))
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), (x, y, card_width, card_height), 0)

    def display_community_cards(self):
        start_x = ((800 - 70 * len(self.community_cards)) // 2) - 10
        for idx, card in enumerate(self.community_cards):
            self.draw_card(card, start_x + 90 * idx, 230)

    def reset_all(self):
        self.community_cards = []
        self.display_community_cards()
        for player in self.players:
            player.reset_hand()
        self.deal()

    def display_fixed_drawings(self):
        self.screen.fill((0, 128, 0))
        pygame.draw.rect(self.screen, self.back_colour, self.funds_box)

        for count in range(2):
            pygame.draw.rect(self.screen, self.back_colour, (350 + count * 80, 30, 70, 110))
            pygame.draw.rect(self.screen, self.back_colour, (20 + count * 620, 40, 155, 60))

        for count in range(3):
            pygame.draw.rect(self.screen, self.back_colour, (50, 400 + count * 60, 170, 50))

        for j in range(2):
            self.draw_card(self.players[0].hand[j], 350 + j * 80, 450, face_up=True)

    def display_fixed_text(self):
        bet_text = self.small_font.render(f"Bet: {self.bet}", True, self.yellow_text)
        self.screen.blit(bet_text, (640, 450))
        self.screen.blit(bet_text, (400, 180))

        funds_text = self.small_font.render(f"Funds: {self.funds}", True, self.yellow_text)
        self.screen.blit(funds_text, (360, 150))

        pot_text = self.small_font.render(f"Pot: {self.pot_total}", True, self.yellow_text)
        self.screen.blit(pot_text, (400, 390))

        funds_text = self.font.render(f"Funds: {self.initial_funds}", True, self.white_text)
        self.screen.blit(funds_text, (self.funds_box.x + 10, self.funds_box.y + 10))

        for count, option in enumerate(self.available_options):
            option_text = self.font.render(option, True, self.white_text)
            self.screen.blit(option_text, (60, 410 + count * 60))

        for count, button in enumerate(self.button_text):
            button_text = self.font.render(button, True, self.white_text)
            self.screen.blit(button_text, (self.top_buttons.x + 10 + count * 630, self.top_buttons.y + 15))

    def play(self):
        self.deal()
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.deal_community_card(3)  # flop
                    elif event.key == pygame.K_t:
                        self.deal_community_card(1)  # turn
                    elif event.key == pygame.K_r:
                        self.deal_community_card(1)  # river
                    elif event.key == pygame.K_y:
                        self.reset_all()
                    elif event.key == pygame.K_e:
                        if input("Are you sure? (y/n): ").lower() == 'y':
                            running = False

            self.display_fixed_drawings()
            self.display_community_cards()
            self.display_fixed_text()
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


# Main function to play the game
def main():
    pygame.init()
    menu = MainMenu()
    menu.run()
    # loads the main menu loop and makes it callable
    
    game = TexasHoldem()
    game.play()
    # imports the game loop and makes it callable


if __name__ == '__main__':
    main()
    # calls the game loop

import random
# allows the use of random integers when dealing and shuffling cards 
import pygame
# allows use of the display

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
class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]
        # this makes a card of every possible value 
        random.shuffle(self.cards)
        # this randomises the card order in the deck

    def draw(self):
        return self.cards.pop()
        # this removes the dealt / drawn card from the deck 


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
        # sets the count to 0
        self.screen = pygame.display.set_mode((800, 600))
        # creates the size of the display
        self.running = True
        self.font = pygame.font.Font(None, 64)
        self.small_font = pygame.font.Font(None, 24)
        # sets the font of the writing on the buttons
        self.start_button_rect = pygame.Rect(290, 350, 220, 90)
        # sets the size and position of the start button
        self.title_rect = pygame.Rect(160, 100, 480, 90)
        # sets the size and position of the title banner
        self.button_colour = (140, 27, 3)
        # sets the background colour of the buttons
        self.text_colour = (255, 255, 255)
        # sets the colour of the text required
        self.cross_colour = (0, 0, 0)
        # sets the colour of the crosses
        self.modes_text = ["Basic (1)", "Tournament (2)",
        "One-on-one (3)"]
        # sets the text for the mode checkboxes
        self.rules_text = ["Antes (0)", "Jackpots (9)",
        "6 and 9 (8)", "Purposeful pre-flop (7)", "Top and tails (6)"]
        # sets the text for the rule checkboxes
        self.titles_text = ["Rules", "Modes"]
        # sets the text for the titles
        self.checklist_back_left = pygame.Rect(20, 220, 240, 340)
        self.checklist_back_right = pygame.Rect(540, 220, 240, 340)
        # sets the drawing size and position of the checkbox
        # backs
        self.checkbox = pygame.Rect(40, 240, 20, 20)
        # sets the size of the checkboxes

    def run(self):
        cross_one_displayed = False
        cross_two_displayed = False
        while self.running:
          for event in pygame.event.get():
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_s:
                      self.running = False
                  # checks if the s button has been pressed
                  # if so, main game loop is opened
                  if event.key == pygame.K_0:
                      cross_one_displayed = not cross_one_displayed
                      depth = 0
                  if event.key == pygame.K_9:
                      cross_two_displayed = not cross_two_displayed
                      depth = 60
                  # checks if any rules + modes have been 
                  # selected

                

          self.screen.fill((0, 128, 0))
          self.draw_start_button()
          self.draw_title()
          self.draw_checklists()
          self.draw_checkboxes()
          self.draw_checkbox_titles()
          # makes the background green and draws the start
          # button
          
          if cross_one_displayed:
            pygame.draw.line(self.screen, self.cross_colour,
            (60, 295 + depth), (40, 275 + depth), 3)
            pygame.draw.line(self.screen, self.cross_colour,
            (40, 295 + depth), (60, 275 + depth), 3)
            
          if cross_two_displayed:
            pygame.draw.line(self.screen, self.cross_colour,
            (60, 295 + depth), (40, 275 + depth), 3)
            pygame.draw.line(self.screen, self.cross_colour,
            (40, 295 + depth), (60, 275 + depth), 3)
            
            
          pygame.display.flip()

    def draw_start_button(self):
        pygame.draw.rect(self.screen, self.button_colour,
        self.start_button_rect)
        # displays the start button
        text = self.font.render('Start (S)', True, 
        self.text_colour)
        # sets the colour and font of the writing
        self.screen.blit(text, (self.start_button_rect.x + 25,
        self.start_button_rect.y + 25))
        # puts the text onto the start button
        
    def draw_title(self):
        pygame.draw.rect(self.screen, self.button_colour,
        self.title_rect)
        # displays the title
        text = self.font.render('Texas Holdem poker', True,
        self.text_colour)
        # sets the colour and font of the writing
        self.screen.blit(text, (self.title_rect.x + 25,
        self.title_rect.y + 25))
        # puts text into the title box
        
    def draw_checklists(self):
      pygame.draw.rect(self.screen, self.button_colour,
      self.checklist_back_left)
      # draws the back of the left checklist
      pygame.draw.rect(self.screen, self.button_colour,
      self.checklist_back_right)
      # draws the back of the right checklist
    
    def draw_checkboxes(self):
      rule_box_down = 275
      mode_box_down = 295
      # sets the initial y position of the first checkbox
      for count in range(5):
        pygame.draw.rect(self.screen, self.text_colour, 
        (40, rule_box_down, 20, 20))
        rule_box_down += 60
        # draws five rules checkboxes evenly spaced down
        # the page
        checkbox_text = self.small_font.render(self.rules_text[count],
        True, self.text_colour)
        # sets the text to be printed as rules
        self.screen.blit(checkbox_text,
        (self.checklist_back_left.x + 50,
        self.checklist_back_left.y + 58 + (count * 60)))
        # displays the rule text
      for count in range(3):
        pygame.draw.rect(self.screen, self.text_colour,
        (560, mode_box_down, 20, 20))
        mode_box_down += 100
        # draws three mode checkboxes down the right side
        checkbox_text = self.small_font.render(self.modes_text[count],
        True, self.text_colour)
        # sets the text to be printed as modes
        self.screen.blit(checkbox_text,
        (self.checklist_back_right.x + 50,
        self.checklist_back_right.y + 78 + (count * 100)))
        # displays the modes as checkboxes
        
    def draw_checkbox_titles(self):
      for count in range(2):
        titles_text = self.font.render(self.titles_text[count],
        True, self.text_colour)
        # sets the text to be printed as modes
        self.screen.blit(titles_text, 
        (self.checklist_back_left.x + 50 + (count * 520),
        self.checklist_back_left.y + 10))
        # displays the modes as checkboxes


# Texas Hold'em game
class TexasHoldem:
    def __init__(self):
        self.deck = Deck()
        # creates the deck of 52 cards
        self.players = [Player('Human'), Player('AI 1'), 
        Player('AI 2'), Player('AI 3'), Player('AI 4')]
        # makes the five players present in the game
        self.community_cards = []
        # makes an empty array to add the dealt cards to
        self.screen = None
        # sets up the pygame screen

    def setup_pygame(self):
        pygame.init()
        # initiates the pygame display
        self.screen = pygame.display.set_mode((800, 600))
        # sets the size of the display screen

    def deal(self):
        for player in self.players:
        # runs as many times as there are players
            player.draw(self.deck)
            player.draw(self.deck)
            # player adds two cards to their hand

    def flop(self):
        self.community_cards += [self.deck.draw() for _ in range(3)]
        # adds three cards to the community card array
        self.display_community_cards()
        # displays the three cards

    def turn(self):
        self.community_cards.append(self.deck.draw())
        # adds one card to the community card array
        self.display_community_cards()
        # displays all cards in the community card array

    def river(self):
        self.community_cards.append(self.deck.draw())
        # adds one card to the community card array
        self.display_community_cards()
        # displays all cards in the community card array

    def reset_community_cards(self):
        self.community_cards = []
        # resets the community card array to empty
        self.display_community_cards()
        # displays the blank screen since no community 
        # cards are present

    def reset_player_hands(self):
        for player in self.players:
            player.reset_hand()
            # empties each player's hand array
        self.deal()
        # deals a new set of two cards

    def draw_card(self, card, x, y, face_up=True):
        if self.screen:
            card_width = 70
            card_height = 110
            # initiates the lengths of the sides of the
            # cards
            font = pygame.font.Font(None, 36)
            # sets the font and font size of the text
            pygame.draw.rect(self.screen, (255, 255, 255),
            (x, y, card_width, card_height))
            # draws the card border 
            pygame.draw.rect(self.screen, (0, 0, 0),
            (x, y, card_width, card_height), 2)
            # draws the card face

            if face_up:
                color = (255, 0, 0) if card.suit in ['Hearts', 'Diamonds'] else (0, 0, 0)
                # makes the charachter colour red if hearts
                # or diamonds and black otherwise
                value_text = font.render(card.value, True,
                color)
                # sets the value text to be printed
                suit_text = font.render(Card.suits[card.suit],
                True, color)
                # sets the suit text to be printed

                if card.value == '10':
                    value_x = x + 1
                    bottom_value_x = x + 43
                    # makes the vale '10' in a slightly more
                    # left position on the card
                else:
                    value_x = x + 6
                    bottom_value_x = x + 48
                    # places the value in the card corners

                self.screen.blit(value_text, (value_x, y + 8))
                self.screen.blit(suit_text, (x + 24, y + 45))  
                self.screen.blit(value_text, (bottom_value_x,
                y + 85))
                # displays the suit and value on the card
            else:
                pygame.draw.rect(self.screen, (0, 0, 0),
                (x, y, card_width, card_height), 0)
                # displays the back of the card

    def display_community_cards(self):
        start_x = ((800 - 70 * len(self.community_cards)) 
        // 2) - 10  
        for idx, card in enumerate(self.community_cards):
            self.draw_card(card, start_x + 90 * idx, 230)  
        # prints the community cards and makes sure they are 
        # centered

    def display_player_cards(self):
        for j in range(2):
            self.draw_card(self.players[0].hand[j], 
            350 + j * 80, 450, face_up=True)
            # draws the player's two face up cards at the 
            # bottom of the screen facing the user
            

    def play(self):
        self.setup_pygame()
        self.deal()
        # calls the deal and setup functions to start
        # the game
        running = True
        clock = pygame.time.Clock()
        # makes the game run and sets the framerate

        while running:
          # keybinds in order to test display events 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.flop()
                    elif event.key == pygame.K_t:
                        self.turn()
                    elif event.key == pygame.K_r:
                        self.river()
                    elif event.key == pygame.K_e:
                        self.reset_community_cards()
                        self.reset_player_hands()

            self.screen.fill((0, 128, 0))  
            # green background for the table
            self.display_community_cards()
            self.display_player_cards()
            # displays the face up cards onto the 
            # table
            pygame.display.flip()
            clock.tick(60),
            # runs the display
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

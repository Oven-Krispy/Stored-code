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
        self.modes_text = ["Tournament (1)",
        "One-on-one (2)"]
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
        clock = pygame.time.Clock()
        cross_one_displayed = False
        cross_two_displayed = False
        cross_three_displayed = False
        cross_four_displayed = False
        cross_five_displayed = False
        cross_six_displayed = False
        cross_seven_displayed = False
        
        while self.running:
          for event in pygame.event.get():
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_s:
                      self.running = False
                  # checks if the s button has been pressed
                  # if so, main game loop is opened
                  if event.key == pygame.K_0:
                      cross_one_displayed = not cross_one_displayed
                  if event.key == pygame.K_9:
                      cross_two_displayed = not cross_two_displayed
                  if event.key == pygame.K_8:
                      cross_three_displayed = not cross_three_displayed
                  if event.key == pygame.K_7:
                      cross_four_displayed = not cross_four_displayed
                  if event.key == pygame.K_6:
                      cross_five_displayed = not cross_five_displayed
                  if event.key == pygame.K_1:
                      cross_six_displayed = not cross_six_displayed
                      depth = 0
                  if event.key == pygame.K_2:
                      cross_seven_displayed = not cross_seven_displayed
                      depth = 100
                  # checks if any rules + modes have been 
                  # selected and therefore removes or adds a cross

                

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
            (60, 295), (40, 275), 3)
            pygame.draw.line(self.screen, self.cross_colour,
            (40, 295), (60, 275 ), 3)
            # this draws the checkmark in the checkbox
            
          if cross_two_displayed:
            pygame.draw.line(self.screen, self.cross_colour,
            (60, 355), (40, 335), 3)
            pygame.draw.line(self.screen, self.cross_colour,
            (40, 355), (60, 335), 3)
          
          if cross_three_displayed:
            pygame.draw.line(self.screen, self.cross_colour,
            (60, 415), (40, 395), 3)
            pygame.draw.line(self.screen, self.cross_colour,
            (40, 415), (60, 395), 3)
            
          if cross_four_displayed:
            pygame.draw.line(self.screen, self.cross_colour,
            (60, 475), (40, 455), 3)
            pygame.draw.line(self.screen, self.cross_colour,
            (40, 475), (60, 455), 3)
            
          if cross_five_displayed:
            pygame.draw.line(self.screen, self.cross_colour,
            (60, 535), (40, 515), 3)
            pygame.draw.line(self.screen, self.cross_colour,
            (40, 535), (60, 515), 3)
          
          if cross_six_displayed:
            pygame.draw.line(self.screen, self.cross_colour,
            (580, 365 + depth), (560, 345 + depth), 3)
            pygame.draw.line(self.screen, self.cross_colour,
            (580, 345 + depth), (560, 365 + depth), 3)
            
          if cross_seven_displayed:
            pygame.draw.line(self.screen, self.cross_colour,
            (580, 365 + depth), (560, 345 + depth), 3)
            pygame.draw.line(self.screen, self.cross_colour,
            (580, 345 + depth), (560, 365 + depth), 3)
          
            
          
          clock.tick(120)  
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
        text = self.font.render('Texas Hold\'em poker', True,
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
      mode_box_down = 345
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
      for count in range(2):
        pygame.draw.rect(self.screen, self.text_colour,
        (560, mode_box_down, 20, 20))
        mode_box_down += 100
        # draws three mode checkboxes down the right side
        checkbox_text = self.small_font.render(self.modes_text[count],
        True, self.text_colour)
        # sets the text to be printed as modes
        self.screen.blit(checkbox_text,
        (self.checklist_back_right.x + 50,
        self.checklist_back_right.y + 128 + (count * 100)))
        # displays the modes names
        
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
        self.back_colour = (140, 27, 3)
        # sets the colour of the back of the cards
        self.button_text = ["Rules (r)", "Exit (e)"]
        # sets the text for the rules and exit buttons
        self.font = pygame.font.Font(None, 45)
        # sets the font to be used for the buttons
        self.top_buttons = pygame.Rect(20, 40 , 140, 60)
        # sets the positon of the top buttons
        self.initial_funds = 1000
        # sets the initial funds available to players
        self.funds_box = pygame.Rect(560, 480, 220, 50)
        # sets the sixe of the box to display the funds in
        self.available_options = ["h", "j", "k"]
        # creates an array for the available play options

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
    
    def display_AI_hands(self):
      for count in range(2):
        pygame.draw.rect(self.screen, self.back_colour, 
        (50, 200 + count * 80, 110, 70), 0)
        # draws the hand on the left
      for count in range(2):
        pygame.draw.rect(self.screen, self.back_colour, 
        (680, 220 + count * 80, 110, 70), 0)
        # draws the hand on the right
      for count in range (2):
        pygame.draw.rect(self.screen, self.back_colour, 
        (200 + count * 80, 20, 70, 110), 0)
        # draws the top left hand
      for count in range (2):
        pygame.draw.rect(self.screen, self.back_colour, 
        (440 + count * 80, 20, 70, 110), 0)
        # draws the top right card
    
    def display_exit_and_rules_buttons(self):
      for count in range(2):
        button_text = self.font.render(self.button_text[count],
        True, (0, 0, 0))
        # sets the text to be displayed on the buttons
        pygame.draw.rect(self.screen, (255, 255, 255),
        (20 + count * 620, 40 , 140, 60))
        # draws the back of the buttons
        self.screen.blit(button_text,
        (self.top_buttons.x + 10 + count * 630,
        self.top_buttons.y + 15))
        # displays the letters on the buttons
    
    def display_available_options(self):
      for count in range(3):
        pygame.draw.rect(self.screen, (255, 255, 255),
        (50, 400 + count * 60, 120, 50))
        # displays the back of the buttons 
        option_text = self.font.render(
        self.available_options[count],
        True, (0, 0, 0))
        # sets the text of the buttons
        self.screen.blit(option_text, 
        (60, 410 + count * 60))
        # puts the text onto the buttons
    
    def display_available_funds(self):
      funds_text = self.font.render("Funds: ",
      True, (0, 0, 0))
      # sets the text for the funds button
      pygame.draw.rect(self.screen, (255, 255, 255),
      self.funds_box)
      # draws the back of the funds button
      self.screen.blit(funds_text, (self.funds_box.x + 10,
      self.funds_box.y + 10))
      # displays the text onto the button
            

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
            self.display_AI_hands()
            # displays the face down AI hands
            self.display_available_funds()
            # displays the player's available funds
            self.display_available_options()
            # displays the options avaiable to the player
            self.display_exit_and_rules_buttons()
            # displays the exit and rules buttons
            pygame.display.flip()
            clock.tick(120),
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

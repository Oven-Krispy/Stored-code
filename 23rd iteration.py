import random
# allows the use of random integers when dealing and shuffling cards 
import pygame
# allows use of the display
import time
# allows the use of time.sleep in order to make play more realistic
from collections import Counter
# imports the counter which will be used when comparing hands

# function which is used to evaluate the value of the player's hands
def evaluate_hand(hand):
    values = '23456789TJQKA'
    value_count = Counter(card[0] for card in hand)
    suits = [card[1] for card in hand]

    is_flush = len(set(suits)) == 1
    is_straight = ''.join(sorted(value_count.keys(), key=values.index)) in values

    counts = sorted(value_count.values(), reverse=True)
    hand_rank = {
        (4, 1): ('Four of a Kind', 8),
        (3, 2): ('Full House', 7),
        (3, 1, 1): ('Three of a Kind', 4),
        (2, 2, 1): ('Two Pair', 3),
        (2, 1, 1, 1): ('One Pair', 2),
        (1, 1, 1, 1, 1): ('High Card', 1)
    }

    if is_straight and is_flush:
        return ('Straight Flush', 9 if 'T' not in value_count else 10)
    elif is_flush:
        return ('Flush', 6)
    elif is_straight:
        return ('Straight', 5)
    else:
        return hand_rank.get(tuple(counts), ('High Card', 0))
        
# function used to actually compare the two hands 
def compare_hands(hand1, hand2):
    rank1, value1 = evaluate_hand(hand1)
    rank2, value2 = evaluate_hand(hand2)

    if value1 > value2:
        return "Hand 1 wins with " + rank1
    elif value2 > value1:
        return "Hand 2 wins with " + rank2
    else:
        return "It's a tie with " + rank1

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
    self.reset_deck()
    # sets the deck to empty to start a round

  def reset_deck(self):
    self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]
    # Create a card for every possible suit and value combination
    self.shuffle()
    # randomises the order of the cards in the deck

  def shuffle(self):
    random.shuffle(self.cards)
    # shuffles the deck for the first time

  def draw(self):
    if not self.cards:
      self.reset_deck()
      # checks if the deck is empty and if so, resets it
    return self.cards.pop()
    # Remove and return the top card from the deck, and reset if empty

# Player class
class Player:
  def __init__(self, name):
    self.name = name
    # initiates the attribute 'name' e.g. human or bot
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
    # sets up the display and its size
    self.running = True
    # sets the menu loop to run
    self.font = pygame.font.Font(None, 64)
    self.small_font = pygame.font.Font(None, 24)
    # sets the two sizes of font needed
    self.start_button_rect = pygame.Rect(290, 350, 220, 90)
    self.title_rect = pygame.Rect(160, 100, 480, 90)
    self.checklist_back_left = pygame.Rect(20, 220, 240, 340)
    self.checklist_back_right = pygame.Rect(540, 250, 240, 300)
    # sets the size and bounds of the rectangles needed
    self.button_colour = (140, 27, 3)
    self.text_colour = (255, 255, 255)
    self.cross_colour = (0, 0, 0)
    # sets the three colours needed for text and drawings
    self.mode_text = "Tournament (1)"
    self.rules_text = ["Antes (0)", "Jackpots (9)",
    "6 and 9 (8)", "Purposeful pre-flop (7)", "Top and tails (6)"]
    self.titles_text = ["Rules", "Mode"]
    # sets all of the text which will be displayed
    self.crosses_displayed = [False] * 6
    # sets all of the crosses to not be displayed

  def run(self):
    clock = pygame.time.Clock()
    # allows the change of the clock speed
    
    while self.running:
      # runs until loop is false
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          self.handle_keydown(event.key)
          # sends the key input to a function 
          # which responds with what it triggers

      self.screen.fill((0, 128, 0))
      # sets the background
      self.draw_fixed_elements()
      # draws and writes all of the text boxes needed
      self.draw_crosses()
      # draws any crosses which are now true
      clock.tick(60)  
      pygame.display.flip()
      # sets the clock speed and authorises the display

  def handle_keydown(self, key):
    if key == pygame.K_s:
      self.running = False
      # starts the game if the s key is pressed
    elif pygame.K_0 <= key <= pygame.K_1 or pygame.K_6 <= key <= pygame.K_9:
      # checks if any of the mode or rule keys have been toggled
      index = [pygame.K_0, pygame.K_9, pygame.K_8, pygame.K_7,
      pygame.K_6, pygame.K_1].index(key)
      # makes the keys their corresponding position within
      # an array based off their position on the checklist
      self.crosses_displayed[index] = not self.crosses_displayed[index]
      # makes any not displayed crosses remain false and 
      # any newly triggered true

  def draw_fixed_elements(self):
    pygame.draw.rect(self.screen, self.button_colour,
    self.checklist_back_left)
    pygame.draw.rect(self.screen, self.button_colour,
    self.checklist_back_right)
    # draws the backgrounds for the two checklists 

    for count in range(5):
      pygame.draw.rect(self.screen, self.text_colour,
      (40, 275 + count * 60, 20, 20))
      # draws the five checkboxes for the rules

    pygame.draw.rect(self.screen, self.text_colour,
    (560, 395, 20, 20))
    # draws the mode checkbox
    pygame.draw.rect(self.screen, self.button_colour,
    self.title_rect)
    # draws the background for the title
    pygame.draw.rect(self.screen, self.button_colour,
    self.start_button_rect)
    # draws the background for the start button
    
    self.draw_text_elements()
    # calls the function to write the text onto the
    # drawings

  def draw_crosses(self):
    positions = [(60, 295), (60, 355), (60, 415),
    (60, 475), (60, 535), (580, 415)]
    # sets the positions of all six possible cross positions
    for i, pos in enumerate(positions):
      # uses the position index to link the cross position
      # to their order
      if self.crosses_displayed[i]:
        pygame.draw.line(self.screen, self.cross_colour,
        pos, (pos[0] - 20, pos[1] - 20), 3)
        pygame.draw.line(self.screen, self.cross_colour,
        (pos[0] - 20, pos[1]), (pos[0], pos[1] - 20), 3)
        # draws the two lines which make up the cross

  def draw_text_elements(self):
    for count in range(2):
      titles_text = self.font.render(self.titles_text[count],
      True, self.text_colour)
      # sets the text for the checklist titles
      self.screen.blit(titles_text,
      (self.checklist_back_left.x + 50 + count * 520,
      self.checklist_back_left.y + 10 + count * 40))
      # writes the two checklist box titles
    
    for count in range(5):
      checkbox_text = self.small_font.render(self.rules_text[count], True, self.text_colour)
      # sets the text for the rules to be added
      self.screen.blit(checkbox_text,
      (self.checklist_back_left.x + 50,
      self.checklist_back_left.y + 58 + (count * 60)))
      # writes the possible rules that can be added

    checkbox_text = self.small_font.render(self.mode_text,
    True, self.text_colour)
    # sets the text for the mode checkbox
    self.screen.blit(checkbox_text,
    (self.checklist_back_right.x + 50, 
    self.checklist_back_right.y + 148))
    # writes the text for the mode which can be added

    text = self.font.render('Texas Hold\'em poker',
    True, self.text_colour)
    # sets the text to write for the title
    self.screen.blit(text, (self.title_rect.x + 25,
    self.title_rect.y + 25))
    # writes the title text
    
    text = self.font.render('Start (S)', True,
    self.text_colour)
    # sets the text to write for the start button
    self.screen.blit(text, (self.start_button_rect.x + 25,
    self.start_button_rect.y + 25))
    # writes the text for the start button



# Texas Hold'em game
class TexasHoldem:
  def __init__(self):
    self.setup_game_variables()
    # initiates all of the variables at once
    self.setup_pygame()
    # initialises the display

  def setup_game_variables(self):
    self.deck = Deck()
    # calls the deck of cards which is used
    self.players = [Player('Human'), Player('Bot')]
    # sets the players in the game
    self.community_cards = []
    # makes the empty community card array
    self.back_colour = (140, 27, 3)
    self.white_text = (255, 255, 255)
    self.yellow_text = (226, 178, 8)
    # sets the colours needed within the display
    self.button_text = ["Rules (Q)", "Exit (E)"]
    self.available_options = ["Bet (B)", "Fold (F)"]
    # sets some of the text to be used in the display
    self.font = pygame.font.Font(None, 45)
    self.small_font = pygame.font.Font(None, 30)
    self.large_font = pygame.font.Font(None, 150)
    # sets the three font sizes needed for the game
    self.top_buttons = pygame.Rect(20, 40, 140, 60)
    self.funds_box = pygame.Rect(560, 480, 220, 50)
    # sets the sizes and the parameters of the rectangles needed

  def setup_pygame(self):
    pygame.init()
    # allows the use of the display
    self.screen = pygame.display.set_mode((800, 600))
    # sets the size of the display

  def deal(self):
    for player in self.players:
    # iterates over both players
      player.draw(self.deck)
      player.draw(self.deck)
      # adds two cards to the player's hand

  def deal_community_card(self, count):
    self.community_cards += [self.deck.draw() for _ in range(count)]
    # adds community cards to the community card array
    # based off of an integer input of how many to add
    self.display_community_cards()
    # draws the community cards onto the screen

  def draw_card(self, card, x, y, face_up=True):
    card_width, card_height = 70, 110
    # sets the dimensions of the cards
    font = pygame.font.Font(None, 36)
    # sets the font for the value and suit
    pygame.draw.rect(self.screen, (255, 255, 255),
    (x, y, card_width, card_height))
    # draws the card face
    pygame.draw.rect(self.screen, (0, 0, 0),
    (x, y, card_width, card_height), 2)
    # draws the card border

    if face_up:
      color = (255, 0, 0) if card.suit in ['Hearts',
      'Diamonds'] else (0, 0, 0)
      # sets the colour of the text based off the suit
      value_text = font.render(card.value, True, color)
      suit_text = font.render(Card.suits[card.suit], True, color)
      # writes the suit and the value onto the card

      value_x = x + (1 if card.value == '10' else 6)
      bottom_value_x = x + (43 if card.value == '10' else 48)
      # shifts the position of the value on the 10 card since
      # it is a larger value than the others

      self.screen.blit(value_text, (value_x, y + 8))
      self.screen.blit(suit_text, (x + 24, y + 45))
      self.screen.blit(value_text, (bottom_value_x, y + 85))
      # writes the value in the top right and bottom left corners
      # and the suit in the centre of the card
      
  def display_community_cards(self):
    start_x = ((800 - 70 * len(self.community_cards)) // 2) - 10
    # sets the positon of the initial community card based 
    # off of how many have been already dealt
    for idx, card in enumerate(self.community_cards):
      self.draw_card(card, start_x + 90 * idx, 230)
      # draws as many community cards as have been dealt

  def reset_all(self):
      self.community_cards = []
      # empties the community card array
      self.display_community_cards()
      # displays the blank community card space
      for player in self.players:
          player.reset_hand()
          # empties both player's hands
      self.deal()
      # deals both players new cards

  def display_fixed_drawings(self):
    self.screen.fill((0, 128, 0))
    pygame.draw.rect(self.screen, self.back_colour, self.funds_box)
    # draws the box for the user's funds to be displayed in

    for count in range(2):
      pygame.draw.rect(self.screen, self.back_colour,
      (350 + count * 80, 30, 70, 110))
      pygame.draw.rect(self.screen, self.back_colour,
      (20 + count * 620, 40, 155, 60))
      # draws the rules and exit button backgrounds

    for count in range(2):
      pygame.draw.rect(self.screen, self.back_colour,
      (50, 400 + count * 60, 170, 50))
      # draws the back of the option buttons

    for j in range(2):
      self.draw_card(self.players[0].hand[j],
      350 + j * 80, 450, face_up = True)
      # draws the user's two cards
          
  def play(self):
    self.deal()
    # draws cards for the players
    running = True
    betting = True
    # sets the two game loops to run
    clock = pygame.time.Clock()
    # allows influence of the clock speed
    blinds = 100
    user_funds = 1000 - blinds
    bot_funds = 1000 - blinds
    user_bet = blinds
    bot_bet = blinds
    pot_total = user_bet + bot_bet
    game_round = 1
    
    while running:

      
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_y:
            self.reset_all()
            # placeholder for resetting the cards
          elif event.key == pygame.K_e:
            if input("Are you sure? (y/n): ").lower() == 'y':
              running = False
            # if the user hits the exit key they will be asked
            # if they are certain and if so the game loop will 
            # close
          elif event.key == pygame.K_f:
            bot_funds += pot_total
            # the user toggles f which causes them to fold thus
            # adding the pot total to the other user's funds
            
            if user_funds == 0:
              print("game over!")
              running = False
            
            self.reset_all()
            # resets the community cards and hands
            user_bet = blinds
            bot_bet = blinds
            pot_total = user_bet + bot_bet
            user_funds -= blinds
            # sets all of the bets and funds again
            
            
          elif event.key == pygame.K_b:
            user_bet = int(input("enter your bet: "))
            # allows the user to place their bet
            user_funds -= user_bet
            # removes their bet from their funds
            bot_bet = 300
            if user_bet > bot_bet:
              bot_bet = user_bet
            bot_funds -= bot_bet
            # sets the bot player's bet and takes it from their 
            # funds
            pot_total += bot_bet + user_bet
            # adds both bets to the pot
            
            if game_round == 1:
              self.deal_community_card(3)
              # draws the turn card and places it on the table
              game_round += 1
            
            elif game_round == 2:
              self.deal_community_card(1)
              game_round += 1
            elif game_round == 3:
              self.deal_community_card(1)
              game_round += 1
            
   
   

      self.display_fixed_drawings()
      self.display_fixed_text(user_funds, user_bet, bot_funds,
      bot_bet, pot_total)
      # draws the items and text onto the screen
      self.display_community_cards()
      pygame.display.flip()
      clock.tick(60)
      # loads the display
    
        
      
    
    
    pygame.quit()
    # ends the game loop

  def display_fixed_text(self, user_funds, user_bet, bot_funds, bot_bet,
  pot_total):
      player_bet_text = self.small_font.render(f"Bet: {user_bet}",
      True, self.yellow_text)
      self.screen.blit(player_bet_text, (640, 450))
      # displays the users current bet in the bottom right
      # corner
      
      AI_bet_text = self.small_font.render(f"Bet: {bot_bet}",
      True, self.yellow_text)
      self.screen.blit(AI_bet_text, (400, 180))
      # displays the bot player's bet in the top middle 

      funds_text = self.small_font.render(f"Funds: {bot_funds}", 
      True, self.yellow_text)
      self.screen.blit(funds_text, (360, 150))
      # displys the bot player's funds above their bet

      pot_text = self.small_font.render(f"Pot: {pot_total}",
      True, self.yellow_text)
      self.screen.blit(pot_text, (400, 390))
      # displays the money in the pot in the centre

      funds_text = self.font.render(f"Funds: {user_funds}",
      True, self.white_text)
      self.screen.blit(funds_text, 
      (self.funds_box.x + 10, self.funds_box.y + 10))
      # displays the user's funds in the box at the bottom
      # right corner

      for count, option in enumerate(self.available_options):
          option_text = self.font.render(option, True, self.white_text)
          self.screen.blit(option_text, (60, 410 + count * 60))

      for count, button in enumerate(self.button_text):
          button_text = self.font.render(button, True, self.white_text)
          self.screen.blit(button_text, 
          (self.top_buttons.x + 10 + count * 630,
          self.top_buttons.y + 15))

      


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

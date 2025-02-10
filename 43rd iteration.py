import random
# allows the use of random integers when dealing and shuffling cards 
import pygame
# allows use of the display
import time
# allows the use of time.sleep in order to make play more realistic
from collections import Counter
# imports the counter which will be used when comparing hands

# definition of way to compare the hands
def compare_hands(players, community_cards):
  # takes in all the required variables
  ranked_hands = [(Hand(player.hand + community_cards).rank_hand(),
  player) for player in players]
  # sets what cards are being compared
  ranked_hands.sort(reverse = True, key = lambda x: x[0])
  # sorts the hand into order
  winner = ranked_hands[0][1]
  # sets who the winner is
  win_type = ranked_hands[0][0][2]
  # sets the type of win achieved
  high_card = ranked_hands[0][0][1]
  # sets the high card of the hand
  return winner.name, win_type, high_card
  # outputs who has won and how
  

# definition of way to round bets
def round_to_nearest_100(number):
  if number <= 100:
    return 100
    # makes sure 0 cannot be chosen
  else:
    return round(number / 100) * 100
    # otherwise rounds to the nearest hundred


# way to check if the user input is an integer
def is_integer(input_string):
    try:
        int(input_string)
        return True
    except ValueError:
        return False
  

# Hand class and Hand ranking logic
class Hand:
    def __init__(self, cards):
        self.cards = cards
        # sets the cards which will be used
    
    def rank_hand(self):
        ranks = [card.value for card in self.cards]
        suits = [card.suit for card in self.cards]
        # sets what corresponds to the card values and suits 
        # with the cards used
        
        rank_counts = Counter(ranks).most_common()
        suit_counts = Counter(suits).most_common()
        # counts how many of each suit and rank there are
        # for determining sets and flushes
        
        straight = self.is_straight(ranks)
        # checks if the cards contain a straight
        flush = suit_counts[0][1] == 5
        # checks if there are five cards of the same suit

        if straight and flush:
            return (8, self.high_card(ranks), "Straight Flush")  
            # determines if the hand is a straight flush
        if rank_counts[0][1] == 4:
            return (7, rank_counts[0][0], "Four of a Kind")  
            # determines if the hand has four of a kind
        if rank_counts[0][1] == 3 and rank_counts[1][1] == 2:
            return (6, rank_counts[0][0], "Full House")  
            # determines if the hand has a full house
        if flush:
            return (5, self.high_card(ranks), "Flush")  
            # determines if the hand is a flush
        if straight:
            return (4, self.high_card(ranks), "Straight")  
            # determines if the hand is a straight
        if rank_counts[0][1] == 3:
            return (3, rank_counts[0][0], "Three of a Kind")  
            # determines if the hand has three of a kind
        if rank_counts[0][1] == 2 and rank_counts[1][1] == 2:
            return (2, rank_counts[0][0], "Two Pair")  
            # determines if the hand has a two pair
        if rank_counts[0][1] == 2:
            return (1, rank_counts[0][0], "One Pair")  
            # determines if the hand has a pair
        return (0, self.high_card(ranks), "High Card")  
        # determines if the hand only has a high card
    
    def is_straight(self, ranks):
      rank_values = sorted([Card.values.index(rank) for rank in ranks])
      # sorts the cards into rank order
      for i in range(4):
          if rank_values[i] + 1 != rank_values[i + 1]:
              return False
              # iterates throught the list to check its components
              # are consecutive
      return True

    def high_card(self, ranks):
        return Card.values[max([Card.values.index(rank) for rank in ranks])]
        # returns the highest card within the hand

 
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
    
  def __repr__(self):
    return f"{self.value}{self.suit}"


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
    self.players = [Player('User'), Player('Bot')]
    # sets the players in the game
    self.community_cards = []
    # makes the empty community card array
    self.back_colour = (140, 27, 3)
    self.white_text = (255, 255, 255)
    self.yellow_text = (226, 178, 8)
    # sets the colours needed within the display
    self.button_text = ["Rules (Q)", "Exit (E)"]
    self.available_options = ["Bet (B)", "Check (C)", "Fold (F)"]
    # sets some of the text to be used in the display
    self.font = pygame.font.Font(None, 45)
    self.small_font = pygame.font.Font(None, 30)
    self.large_font = pygame.font.Font(None, 150)
    # sets the three font sizes needed for the game
    self.top_buttons = pygame.Rect(20, 40, 140, 60)
    self.funds_box = pygame.Rect(560, 480, 220, 50)
    # sets the sizes and the parameters of the rectangles needed
    self.running = True
    # allows use of the game loop

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

  def draw_card(self, card, x, y, face_up = True):
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

    for count in range(3):
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
    game_round = 0
    community_cards_total = 0
    
    user_max_bet = user_funds
    bot_max_bet = bot_funds
    
    while self.running:
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_e:
              if input("Are you sure? (y/n): ").lower() == 'y':
                self.running = False
                main()
              # if the user hits the exit key they will be asked
              # if they are certain and if so the game loop will 
              # close
              
            elif event.key == pygame.K_c:
              game_round += 1
              self.iterate_round(user_funds, game_round, bot_funds, pot_total, user_bet, bot_bet, community_cards_total, blinds)
              
            
            elif event.key == pygame.K_f:
              bot_funds += pot_total
              # the user toggles f which causes them to fold thus
              # adding the pot total to the other user's funds
              self.reset_round_variables(blinds, user_bet, bot_bet, pot_total, user_funds, bot_funds, game_round)
              
            elif event.key == pygame.K_b:
              user_input = ""
              # clears the user input
              bet_input_active = True
              # allows input of text
              
              while bet_input_active:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            
                            user_bet = round_to_nearest_100(int(user_input))

                            user_funds -= user_bet
                            bot_funds -= int(bot_bet)
                            # updates the funds and bet counters
                            bet_input_active = False
                            # stops the loop when reurn is hit
                            game_round += 1
                        
                        elif event.key == pygame.K_BACKSPACE:
                            user_input = user_input[:-1]
                            # removes the end character
                            
                            self.match_bot_bet(user_input, user_max_bet, bot_bet, user_bet, user_funds, bot_funds, pot_total)
                            
                        else:
                          user_input += event.unicode
                          # adds the next typed character
                          if is_integer(user_input):
                            user_bet = 0 if user_input == "" else int(user_input)
                            # removes the error when checking an 
                            # empty input
                            if user_bet > user_funds:
                              
                              self.update_display_to_clear(user_funds, bot_funds, pot_total)
                              # reloads and clears the display
                              
                              user_input = str(user_funds)
                              user_bet = user_input
                              # sets any exceeding value to the user's 
                              # maximum value
                              
                            if int(user_input) > 100:
                              bot_bet = round_to_nearest_100(int(user_bet))
                              # switches the bot's bet to match
                              # the user's
                              
                              self.update_display_to_clear(user_funds, bot_funds, pot_total)
                              # reloads and clears the display
                              
                            else:
                              bot_bet = 100
                              # otherwise the bet is set to 100
                              
                          else: 
                            user_input = user_input[:-1]
                            
        
                self.display_updating_text(user_input, bot_bet)
                # displays the text the user writes

              pot_total += int(bot_bet) + int(user_bet)
              # adds both bets to the pot
              
              self.iterate_round(user_funds, game_round, bot_funds, pot_total, user_bet, bot_bet, community_cards_total, blinds)

                
          self.update_display_to_clear(user_funds, bot_funds, pot_total)
          # reloads and clears the display
          
          self.check_if_bust(bot_funds, user_funds)
          # checks to make sure neither player has run out of money
          
          clock.tick(60)
          # loads the display
        
    
    pygame.quit()
    # ends the game loop

  def display_fixed_text(self, user_funds, bot_funds, pot_total):


      funds_text = self.small_font.render(f"Funds: {bot_funds}", 
      True, self.yellow_text)
      self.screen.blit(funds_text, (370, 150))
      # displys the bot player's funds above their bet

      pot_text = self.small_font.render(f"Pot: {pot_total}",
      True, self.yellow_text)
      self.screen.blit(pot_text, (380, 390))
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
 
  def update_display_to_clear(self, user_funds, bot_funds, pot_total):
    #self.screen.fill((0, 128, 0))
    self.display_fixed_drawings()
    self.display_fixed_text(user_funds, bot_funds, pot_total)
    # draws the items and text onto the screen
    self.display_community_cards()
    # displays the current community cards
    pygame.display.flip()
    # loads the display
  
  def reset_round_variables(self, blinds, user_bet, bot_bet, pot_total, user_funds, bot_funds, game_round):
    self.reset_all()
    # resets the community cards and hands
    user_bet = blinds
    bot_bet = blinds
    pot_total = user_bet + bot_bet
    user_funds -= blinds
    bot_funds -= blinds
    # sets all of the bets and funds again
    game_round = 1
    community_cards_total = 0
    # resets what round of the game is next
  
  def display_updating_text(self, user_input, bot_bet):
    enter_bet_text = self.small_font.render(f"Enter your bet: {user_input}",
    True, self.yellow_text)
    # sets the text to be displayed
    self.screen.blit(enter_bet_text, (20, 180))
    # displays the text onto the screen
    player_bet_text = self.small_font.render(f"Bet: {user_input}", 
    True, self.yellow_text)
    self.screen.blit(player_bet_text, (640, 450))
    # displays the users current bet in the bottom right
    # corner
    bot_bet_text = self.small_font.render(f"Bet: {bot_bet}",
    True, self.yellow_text)
    self.screen.blit(bot_bet_text, (380, 180))
    # displays the bot's bet in the top middle
    
    pygame.display.flip()
    # allows it to be displayed
  
  def check_if_bust(self, bot_funds, user_funds):
    if bot_funds <= 0:
      user_win_text = self.font.render("Bot bust!",
      True, self.yellow_text)
      self.screen.blit(user_win_text, (360, 270))
      pygame.display.flip()
      time.sleep(3)
      self.running = False
      main()

      
    if user_funds <= 0:
      bot_win_text = self.font.render("You bust!",
      True, self.yellow_text)
      self.screen.blit(bot_win_text, (360, 270))
      pygame.display.flip()
      time.sleep(3)
      self.running = False
      main()

  def match_bot_bet(self, user_input, user_max_bet, bot_bet, user_bet, user_funds, bot_funds, pot_total):
    if user_input == "":
      pass
      # skips check if input is empty
    else:
      checking = True
      # allows the check loop to run
      while checking:
        if int(user_input) > user_max_bet:
          bot_bet = user_bet
          # bot matches the user's bet
          checking = False
          # check is ended
        else:
          bot_bet = 100
          checking = False
          # otherwise makes the base bet of
          # 100
      
      self.update_display_to_clear(user_funds, bot_funds, pot_total)
      # reloads and clears the display

  def iterate_round(self, user_funds, game_round, bot_funds, pot_total, user_bet, bot_bet, community_cards_total, blinds):
    # dealing the community cards
    if user_funds > 0:
      if game_round == 1:
        self.deal_community_card(3)
        # deals the flop cards
        #game_round += 1
        community_cards_total = 3
      elif game_round == 2:
        self.deal_community_card(1)
        # deals the turn card
        #game_round += 1
        community_cards_total = 4
      elif game_round == 3:
        self.deal_community_card(1)
        # deals the river card
        community_cards_total = 5
        #game_round += 1
      elif game_round == 4:

        self.update_display_to_clear(user_funds, bot_funds, pot_total)
        # reloads and clears the display
        
        name, win_type, high_card = compare_hands(self.players,
        self.community_cards)
        # outputs the winner
        
        if name == 'Bot':
          bot_funds += pot_total
          pot_total = 0
          # if the bot has won, the pot will be sent
          # to its funds
        else:
          user_funds += pot_total
          pot_total = 0
          # if the user has won, the pot will be sent
          # to their funds
        
        win_text = self.small_font.render(f"{name} won with {win_type} of high card {high_card}",
        True, self.yellow_text)
        self.screen.blit(win_text, (250, 200))
        # outputs the winner
        
        pygame.display.flip()
        # allows it to be displayed
        
        user_bet = 0
        bot_bet = 0
        # resets all of the displayed values
        
      
        time.sleep(5)
        self.reset_round_variables(blinds, user_bet, bot_bet, pot_total, user_funds, bot_funds, game_round)
    
    else:
      self.deal_community_card(5 - community_cards_total)
      # deals the remaining community cards

      self.update_display_to_clear(user_funds, bot_funds, pot_total)
      # reloads and clears the display
      
      name, win_type, high_card = compare_hands(self.players,
      self.community_cards)
      # outputs the winner
      
      if name == 'Bot':
        bot_funds += pot_total
        # if the bot has won, the pot will be sent
        # to its funds
      else:
        user_funds += pot_total
        # if the user has won, the pot will be sent
        # to their funds
      
      win_text = self.small_font.render(f"{name} won with {win_type} of high card {high_card}",
      True, self.yellow_text)
      self.screen.blit(win_text, (250, 200))
      # outputs the winner
      
      pygame.display.flip()
      # allows it to be displayed
      
      pot_total = 0
      user_bet = 0
      bot_bet = 0
      # resets all of the displayed values
      
      time.sleep(5)
      self.reset_round_variables(blinds, user_bet, bot_bet, pot_total, user_funds, bot_funds, game_round)

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

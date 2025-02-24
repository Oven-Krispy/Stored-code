import random
# imports random to use for card shuffling
import pygame
# imports pygame to allow use of the display
from collections import Counter
# imports the counter for checking suits and values 

# Card class
class Card:
  suits = {'Yellow': 'Y', 'Red': 'R', 'Blue': 'B', 'Green': 'G'}
  # dictionary of the basic suits
  values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'O', 'R', '+2']
  # array of the basic values
  wild_suit = {'Wild': 'W'}
  # dictionary for the wild cards
  wild_value = ['+4', 'W']
  # array of the wild card values
  zero_value = ['0']
  # array of the zero cards

  def __init__(self, suit, value):
    self.suit = suit
    # defines the suit of a card
    self.value = value
    # defines the value of a card

  def __repr__(self):
    return f"{self.suit} {self.value}"
    # allows a card to be represented as a string e.g. B7

# Deck class
class Deck:
  def __init__(self):
    self.reset_deck()
    # shuffles the deck

  def reset_deck(self):
    self.cards = ([Card(suit, value) for suit in Card.suits for value in Card.values] * 2 +
                  [Card(suit, value) for suit in Card.wild_suit for value in Card.wild_value] * 4 +
                  [Card(suit, value) for suit in Card.suits for value in Card.zero_value])
    # creates all the cards in the deck
    self.shuffle()
    # calls the method which randomises the order of the cards

  def shuffle(self):
    random.shuffle(self.cards)
    # randomises the order of the cards

  def draw(self):
    if not self.cards:
      self.reset_deck()
      # resets the deck if no cards are left
    hand.append(self.cards.pop())
    # adds the next card to the player's hand and removes it from
    # the pool of available cards

# Drawing face up cards
def draw_card(card, x, y, face_up = True):
  card_width, card_height = 80, 120
  # sets the dimensions of the cards
  large_font = pygame.font.Font(None, 40)
  # sets the font for the central value on the card
  small_font = pygame.font.Font(None, 31)
  # sets the font for the corner values on the card
  
  if face_up:
    color_dict = {
      'Red': (215, 38, 0),
      'Green': (55, 171, 17),
      'Yellow': (236, 192, 7),
      'Blue': (9, 86, 191),
      'default': (0, 0, 0)
    } # dictionary of the colours of the cards and text
    
    color = color_dict.get(card.suit, color_dict['default'])
    # gets the colour of the centre of the card
    
    pygame.draw.rect(screen, color, (x, y, card_width, card_height))
    # draws the centre of the card
    pygame.draw.rect(screen, white, (x, y, card_width, card_height), 2)
    # draws the outline of the card

    corner_text = small_font.render(card.value, True, white)
    # sets the text to be displayed in the corners of the card
    centre_text = large_font.render(card.value, True, white)
    # sets the text to be displayed in the card's centre

    value_x = x + (2 if card.value in ['+2', '+4'] else 6)
    bottom_value_x = x + (51 if card.value in ['+2', '+4'] else 56)
    # sets the positions of the displayed text with changes if 
    # the card is a +2 or + 4

    screen.blit(corner_text, (value_x, y + 8))
    # displays top left value on the card
    screen.blit(centre_text, (x + 27, y + 45))
    # displays centre value on the card
    screen.blit(corner_text, (bottom_value_x, y + 90))
    # displays the bottom right value on the card
    
    if card.value == 'O':
      skip_lines = [(value_x + 12, y + 12), (x + 42, y + 50), (bottom_value_x + 12, y + 94)]
      # sets the position of the line for the skip symbol
      for pos in skip_lines:
        pygame.draw.line(screen, white, pos, (pos[0] - 8, pos[1] + 10), 3)
        # draws all three skip lines needed on the card

all_values = ['+4', 'W', '+2', 'O', 'R', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
# sets the rank order of the card values
all_suits = ["Wild", "Red", "Blue", "Green", "Yellow"]
# sets the rank order of the card suits

hand = []
# initialises the player's hand

drawing_cards = Deck()
# allows the use of the deck class

for _ in range(7):
  drawing_cards.draw()
  # deals seven cards to the player

pygame.init()
screen = pygame.display.set_mode((800, 600))
# sets up the display

while True:
  screen.fill((0, 0, 0))
  # fills the screen background
  hand_sorted = sorted(hand, key=lambda card: (all_suits.index(card.suit), all_values.index(card.value)))
  # sorts the cards in the player's hand by suit and then by
  # the value of the card
  for j, card in enumerate(hand_sorted):
    draw_card(card, (375 - (len(hand_sorted) * 13)) + j * 30, 450, face_up = True)
    # displays the cards in sorted order 
      
  pygame.display.flip()
  # allows the display actions to be shown


  # TEST TO RESET HANDS 
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_r:
        hand = []
        # clears the player's hand
        drawing_cards = Deck()
        for _ in range(7):
          drawing_cards.draw()
          # deals the player seven new cards





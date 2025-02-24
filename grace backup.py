import random, pygame

from collections import Counter
# imports the counter which will be used when comparing hands


# Card class
class Card:
  suits = {'Yellow': 'Y', 'Red': 'R', 'Blue': 'B', 'Green': 'G'}
  # a dictionary containing ties between the suits and the letter to represent them
  values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'O', 'R', '+2']
  # an array which contains the possible card values
  wild_suit = {'Wild' : 'W'}
  # a dictionary for the suits of the wild cards
  wild_value = ['+4', 'W']
  # an array containing the two types of wild card
  zero_value = ['0']

  def __init__(self, suit, value):
    self.suit = suit
    # initiates the suit attribute
    self.value = value
    # initiates the value attribute


  def __repr__(self):
    return f"{self.suit} {self.value}"


# Deck class
class Deck:
  def __init__(self):
    self.reset_deck()
    # sets the deck to empty to start a round

  def reset_deck(self):
    self.cards = ([Card(suit, value) for suit in Card.suits for value in Card.values ] * 2) + ([Card(suit, value) for suit in Card.wild_suit for value in Card.wild_value] * 4 + [Card(suit, value) for suit in Card.suits for value in Card.zero_value]) 
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
    hand.append(self.cards.pop())
    # Remove and return the top card from the deck, and reset if empty
  


# drawing face up cards
def draw_card(card, x, y, face_up = True):
    card_width, card_height = 80, 120
    # sets the dimensions of the cards
    large_font = pygame.font.Font(None, 40)
    small_font = pygame.font.Font(None, 31)
    # sets the font for the value and suit
    
    if face_up:
      if card.suit is "Red":
        color = (215, 38, 0)
      elif card.suit is "Green":
        color = (55, 171, 17)
      elif card.suit is "Yellow":
        color = (236, 192, 7)
      elif card.suit is "Blue":
        color = (9, 86, 191)
      else:
        color = (0, 0, 0)
        
      pygame.draw.rect(screen, color, (x, y, card_width, card_height))
      # draws the card face
      pygame.draw.rect(screen, white, (x, y, card_width, card_height), 2)
      # draws the card border
        
      # sets the colour of the text based off the suit
      corner_text = small_font.render(card.value, True, white)
      centre_text = large_font.render(card.value, True, white)
      # writes the suit and the value onto the card

      value_x = x + (2 if card.value is '+2' or card.value is '+4' else 6)
      bottom_value_x = x + (51 if card.value is '+2' or card.value is '+4' else 56)
      # shifts the position of the value on the 10 card since
      # it is a larger value than the others

      screen.blit(corner_text, (value_x, y + 8))
      screen.blit(centre_text, (x + 27, y + 45))
      screen.blit(corner_text, (bottom_value_x, y + 90))
      # writes the value in the top right and bottom left corners
      # and the suit in the centre of the card
      
      skip_lines = [(value_x + 12, y + 12), (x + 42, y + 50), (bottom_value_x + 12, y + 94)]
      
      if card.value == 'O':
        for pos in skip_lines:
          pygame.draw.line(screen, white, pos, (pos[0] - 8, pos[1] + 10), 3)
  

all_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'O', 'R', '+2', '+4', 'W']
all_suits = ["Wild", "Red", "Blue", "Green", "Yellow"]


hand = []
white = (255, 255, 255)

drawing_cards = Deck()
for i in range(7):
  drawing_cards.draw()



pygame.init()
# allows the use of the display
screen = pygame.display.set_mode((800, 600))
# sets the size of the display
while True:
  screen.fill((0, 0, 0))
  for j in range(len(hand)):
    
    suits = [card.suit for card in hand]
    # pulls the value of each card in the hand of cards
    sorted_by_suit = sorted([all_suits.index(suit) for suit in suits])
    # sorts the cards into rank order
      
    test_font = pygame.font.Font(None, 30)
    ranking_test = test_font.render(str(sorted_by_suit), True, white)
    screen.blit(ranking_test, (20, 20))
    
    
    draw_card(hand[j], (375 - (len(hand) * 13)) + j * 30, 450, face_up = True)
    # draws the user's two cards
    
    
  pygame.display.flip()
  # allows it to be displayed
  
  
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_r:
        hand = []
        drawing_cards = Deck()
        for i in range(7):
          drawing_cards.draw()



  
  



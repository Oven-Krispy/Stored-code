import random, pygame


# Card class
class Card:
  suits = {'Yellow': 'Y', 'Red': 'R', 'Blue': 'B', 'Green': 'G'}
  # a dictionary containing ties between the suits and the letter to represent them
  values = ['2', '3', '4', '5', '6', '7', '8', '9', 'skip', 'reverse', '+2',]
  # an array which contains the possible card values
  wild_suit = {'Wild' : 'W'}
  wild_value = ['+4', 'wild']

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
    self.cards = ([Card(suit, value) for suit in Card.suits for value in Card.values ] * 2) + ([Card(suit, value) for suit in Card.wild_suit for value in Card.wild_value] * 4) 
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
    card_width, card_height = 70, 110
    # sets the dimensions of the cards
    font = pygame.font.Font(None, 36)
    # sets the font for the value and suit
    
    if face_up:
      if card.suit is "Red":
        color = (215, 38, 0)
      elif card.suit is "Green":
        color = (55, 171, 17)
      elif card.suit is "Yellow":
        color = (236, 212, 7)
      elif card.suit is "Blue":
        color = (9, 86, 191)
      else:
        color = (0, 0, 0)
        
      pygame.draw.rect(screen, color,
      (x, y, card_width, card_height))
      # draws the card face
      pygame.draw.rect(screen, (0, 0, 0),
      (x, y, card_width, card_height), 2)
      # draws the card border
        
      # sets the colour of the text based off the suit
      value_text = font.render(card.value, True, (255, 255, 255))
      suit_text = font.render(card.value, True, (255, 255, 255))
      # writes the suit and the value onto the card

      value_x = x + 6
      bottom_value_x = x + 48
      # shifts the position of the value on the 10 card since
      # it is a larger value than the others

      screen.blit(value_text, (value_x, y + 8))
      screen.blit(suit_text, (x + 24, y + 45))
      screen.blit(value_text, (bottom_value_x, y + 85))
      # writes the value in the top right and bottom left corners
      # and the suit in the centre of the card
      



hand = []

drawing_cards = Deck()
for i in range(7):
  drawing_cards.draw()


pygame.init()
# allows the use of the display
screen = pygame.display.set_mode((800, 600))
# sets the size of the display
while True:
  screen.fill((255, 255, 255))
  for j in range(7):
    draw_card(hand[j], 325 + j * 25, 450, face_up = True)
    # draws the user's two cards
    
  pygame.display.flip()
  # allows it to be displayed



  
  



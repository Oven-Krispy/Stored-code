import random

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
    print(self.cards.pop())
    # Remove and return the top card from the deck, and reset if empty

drawing_cards = Deck()
for i in range(5):
  drawing_cards.draw()



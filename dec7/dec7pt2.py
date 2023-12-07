import numpy as np
from scipy.stats import entropy


# Entropy function to get quick ranking
def calc_entropy(hand):
  value, counts = np.unique(hand, return_counts=True)
  value = np.flip(value)
  counts = np.flip(counts)
  # changes to pt1:
  # if hand has joker, add the amount of joker to the highest count of other cards to get maximum score 
  if (value[-1] == 1) & (len(value) > 1) :
    ix_of_card_to_change = counts[:-1].argmax()
    counts[ix_of_card_to_change] += counts[-1]
    counts = counts[:-1]
  val_entropy = entropy(counts)
  # flipped the order of entropy to rank easier with card values
  return(val_entropy*-1)

def get_entropy(e):
  return e[2]

def to_value(card):
  value_map = {
    "J":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "T":10,
    "Q":12,
    "K":13,
    "A":14
  }
  return value_map[card]

def get_cards(x):
  return x[0] 

game = []
# read input
with open("actual_input.txt") as f:
  for line in f.readlines():
    hand, bid = line.split()
    hand = [*hand]
    hand = [to_value(e) for e in hand]
    game.append([hand, int(bid), calc_entropy(hand)])


# the two criteria for sorting
game.sort(key=lambda i: (get_entropy(i) ,get_cards(i)))

rank = 1
total_sum = 0
for h in game:
  #h.append(rank*h[1])
  total_sum += rank*h[1]
  rank += 1
  
#print(game)
print(total_sum)
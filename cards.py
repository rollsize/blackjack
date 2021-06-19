import collections
import random
from pictures import Picture
import images
Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck():
    ranks = [str(n) for n in range(2, 11)] + list("jqka")
    suits = "s d c h".split() #spades diamonds clubs hearts

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits 
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __delitem__(self, key):
        del self._cards[key]

    def __getitem__(self, key):
        return self._cards[key]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def get_image(self, card):
        """ Get image of card """ 
        return card.suit + card.rank

def check_hand(hand) -> int:
    """ Return sum of cards ranks in hand """
    hand_value, value = 0, 0
    ace = [0, 11] # numbers, value
    for card in hand:
        if card.rank in ["k", "q", "j"]: value = 10 #k q j = 10
        elif card.rank == "a": # check how many aces
            ace[0] += 1
            value = 0
        else: value = int(card.rank)
        hand_value += value
    if ace[0] > 0: #if aces more then 0 count their values
        if hand_value + 11 > 21: 
            hand_value += 1 * ace[0]
        else:
            hand_value += 11 * ace[0]
    return hand_value # return sum

def compare_hands(p_hand, d_hand, money:int, bet:int):
    p_value = check_hand(p_hand)
    d_value = check_hand(d_hand)
    p_lenght, d_lenght = len(p_hand), len(d_hand)
    money_result = 0
    if (p_value == 21 and p_lenght == 2) and (d_value == 21 and d_lenght == 2):
        money_result += bet
        message_to_player = f"Dealer and you has blackjack, so it's a push!"
    elif (p_value == 21 and p_lenght == 2) and d_value != 21:
        money_result += bet + (bet * 1.5)
        message_to_player = f"Blackjack! You won {money_result} chips!"
    elif p_value != 21 and (d_value == 21 and d_lenght == 2):
        message_to_player = f"Dealer has Blackjack! You busts."
    elif p_value > d_value and p_value <= 21:
        money_result += bet * 2
        message_to_player = f"You won {money_result} chips."
    elif p_value == d_value and p_value <= 21:
        money_result += bet
        message_to_player = f"It's a push! You recieved {money_result} chips back."
    elif p_value <= 21 and d_value > 21:
        money_result += bet * 2 
        message_to_player = f"Dealer busts! You won {money_result} chips"
    else:
        message_to_player = f"Dealer wins, you lose {bet} chips."
    money += money_result
    p_cards_pos = (510, 320)
    d_cards_pos = (20, 20)
    del p_hand[:], d_hand[:]
    return money, message_to_player, p_cards_pos, d_cards_pos, p_hand, d_hand

def hit(deck, hand, cards_pos):
    if len(deck) == 0: #if deck is empty
        deck = cards.generate_deck()
    # Get a card and blit it on screen
    hand.append(deck[0]) # Append card to hand
    card = Picture(images.cards_path + f"{deck.get_image(deck[0])}.png", cards_pos) #for blit on game loop
    cards_pos = (cards_pos[0] - 80, cards_pos[1]) # Next card pos is
    del deck[0] # Del card from deck
    return deck, hand, card, cards_pos # return values

def generate_deck():
    """ Generate a deck """
    deck = FrenchDeck()
    random.shuffle(deck)
    return deck

def use_chec_buff():
    pass
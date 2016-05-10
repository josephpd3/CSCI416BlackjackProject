from numpy import random as rd

suits = [
    'HEARTS',
    'DIAMONDS',
    'SPADES',
    'CLUBS'
]

pips = [
    'ACE',
    'TWO',
    'THREE',
    'FOUR',
    'FIVE',
    'SIX',
    'SEVEN',
    'EIGHT',
    'NINE',
    'TEN',
    'JACK',
    'QUEEN',
    'KING'
]


class Card():
    """
    Defines playing cards w/ pip and suit
    """

    def __init__(self, pip, suit):
        self.pip = pip
        self.suit = suit

    def __str__(self):
        """
        Produces a string representation of the card
        """
        return self.pip + ' OF ' + self.suit

    def __repr__(self):
        """
        When print()ing the card directly, uses the returned value
        """
        return self.__str__()


class Deck():
    """
    Defines a deck of playing cards
    """

    def __init__(self):
        """
        Initializes the deck with every combination of pip and suit
        """
        self.cards = []
        for suit in suits:
            for card in [Card(pip, suit) for pip in pips]:
                self.cards.append(card)

    def shuffle(self):
        """
        Randomizes order of cards in deck
        """
        rd.shuffle(self.cards)

    def deal(self):
        """
        `Draws` the top card off the deck
        """
        return self.cards.pop()


class Hand():
    """
    Defines a player's hand in blackjack
    """

    def __init__(self):
        self.cards = []

    def __str__(self):
        """
        Produces a string representation of a hand
        """
        self_string = ''

        for idx, card in enumerate(self.cards):
            self_string += str(idx + 1) + ') ' + str(card)
            if idx != (len(self.cards) - 1):
                self_string += '\n'
        return self_string

    def __repr__(self):
        """
        Allows print() calls to directly print the hand
        """
        return self.__str__()

    @property
    def score(self):
        """
        Generates `score` property on calls to Hand.score
        """
        # Generate a dictionary of pip scores
        score_dict = {pip: (idx + 1) for idx, pip in enumerate(pips)}
        score = 0
        ace_count = 0

        # Iterate through hand, scoring cards via the dictionary
        for card in self.cards:
            if card.pip != 'ACE':
                score = score + score_dict[card.pip]
            else:
                ace_count = ace_count + 1

        # For every ace, determine if high or low
        for ace in range(ace_count):
            if (score + 11) > 21:
                score = score + 1
            else:
                score = score + 11

        return score

    def add(self, card):
        """
        Adds a `drawn` card to the hand
        """
        self.cards.append(card)

    def empty(self):
        """
        Empties the hand
        """
        self.cards.clear()

    def isBusted(self):
        """
        Checks whether the hand score exceeds 21
        """
        return self.score > 21


def declare_result(score):
    """
    Given a score, determines the result of a round and prints it
    """
    print('* * * * * * * * * * * * * * * *')
    if score < 21:
        print('Your score is: ' + str(score))
    elif score == 21:
        print('Blackjack! Damn fine job.')
    else:
        print('Busted! Better luck next time.')
    print('* * * * * * * * * * * * * * * *')


def play_round():
    """
    Plays a round of Blackjack
    """
    deck = Deck()
    hand = Hand()

    deck.shuffle()

    # deal 2 cards to hand
    for x in range(2):
        hand.add(deck.deal())

    # Keep variable designating continuation of round
    round_going = True
    while round_going:
        print('Your Hand:')
        print(hand)
        print('Current Score: ' + str(hand.score))

        if hand.isBusted():
            declare_result(hand.score)
            round_going = False
            continue
        elif hand.score == 21:
            declare_result(hand.score)
            round_going = False
            continue
        else:
            option = input('Hit (h) or Stay (s)?\n')

        if option.lower() == 'h':
            # player decides to `hit`
            hand.add(deck.deal())
            continue
        elif option.lower() == 's':
            # player decides to `stay
            declare_result(hand.score)
            break
        else:
            # player can't read or type correctly, keep prodding
            continue

    return input('Would you like to play again? (y/n)\n').lower() == 'y'


# Main function, with game loop
if __name__ == '__main__':
    while play_round():
        pass

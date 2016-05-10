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
    def __init__(self, pip, suit):
        self.pip = pip
        self.suit = suit

    def __str__(self):
        return self.pip + ' OF ' + self.suit

    def __repr__(self):
        return self.__str__()


class Deck():
    def __init__(self):
        self.cards = []
        for suit in suits:
            for card in [Card(pip, suit) for pip in pips]:
                self.cards.append(card)

    def shuffle(self):
        rd.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Hand():
    def __init__(self):
        self.cards = []

    def __str__(self):
        self_string = ''

        for idx, card in enumerate(self.cards):
            self_string += str(idx + 1) + ') ' + card.__str__()
            if idx != (len(self.cards) - 1):
                self_string += '\n'
        return self_string

    def __repr__(self):
        return self.__str__()

    @property
    def score(self):
        score_dict = {pip: (idx + 1) for idx, pip in enumerate(pips)}
        score = 0
        ace_count = 0

        for card in self.cards:
            if card.pip != 'ACE':
                score = score + score_dict[card.pip]
            else:
                ace_count = ace_count + 1

        for ace in range(ace_count):
            if (score + 11) > 21:
                score = score + 1
            else:
                score = score + 11

        return score

    def add(self, card):
        self.cards.append(card)

    def empty(self):
        self.cards.clear()

    def isBusted(self):
        return self.score > 21


def declare_result(score):
    print('* * * * * * * * * * * * * * * *')
    if score < 21:
        print('Your score is: ' + str(score))
    elif score == 21:
        print('Blackjack! Damn fine job.')
    else:
        print('Busted! Better luck next time.')
    print('* * * * * * * * * * * * * * * *')


def play_round():
    deck = Deck()
    hand = Hand()

    deck.shuffle()

    for x in range(2):
        hand.add(deck.deal())

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
            hand.add(deck.deal())
            continue
        elif option.lower() == 's':
            declare_result(hand.score)
            break
        else:
            continue

    return input('Would you like to play again? (y/n)\n').lower() == 'y'


if __name__ == '__main__':
    while play_round():
        pass

// Bring in super awesome libraries for cool programming
var lodash = require('lodash');
var rls = require('readline-sync');

// Card suits
var suits = [
    'HEARTS',
    'DIAMONDS',
    'SPADES',
    'CLUBS'
];

// Card pips
var pips = [
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
];

/**
 * Class defining playing cards with pip and suit represented
 * 
 */
class Card {

    /**
     * Initializes a Card
     * 
     * @param  {String} pip
     * @param  {String} suit
     */
    constructor(pip, suit) {
        this.pip = pip,
        this.suit = suit
    }

    /**
     * Returns the printed representation of a Card
     * 
     * @return {String} Printed Representation
     */
    toString() { return this.pip + ' OF ' + this.suit; }

}

/**
 * Class defining a deck of playing cards that can be shuffled or
 * have cards dealt from the top
 * 
 */
class Deck {

    /**
     * Initializes a Deck of cards, iterating through all pips and suits
     * to generate a full deck.
     * 
     */
    constructor() {
        var suit, pip;

        this.cards = [];

        suits.map(suit => {
            pips.map(pip => {
                this.cards.push(new Card(pip, suit));
            })
        });
    }

    /**
     * Shuffles the deck by randomizing the order of the cards within
     * 
     */
    shuffle() { this.cards = lodash.shuffle(this.cards); }

    /**
     * Removes and returns the card at the top (end of the array) of the deck
     * 
     * @return {Card} The "top" card off the deck
     */
    deal() { return this.cards.pop(); }

}

/**
 * Class defining a player's hand in blackjack.
 * Can add cards, empty, print held cards, and determine score.
 * 
 */
class Hand {

    /**
     * Initializes Hand object with empty card array
     */
    constructor() { this.cards = [] }

    /**
     * Adds a card to the hand
     * 
     * @param {Card} card
     */
    add(card) { this.cards.push(card); }

    /**
     * Empties the hand
     * 
     */
    empty() { this.cards = []; }

    /**
     * Prints the hand to the console with cards numbered starting
     * at 1 (+1 to index)
     * 
     */
    print() {
        this.cards.forEach(function(card, index){
            var displayIndex = index + 1;
            console.log(displayIndex + ') ' + card.toString());
        });
    }

    /**
     * Checks whether hand score exceeds limit of 21
     * 
     * @return {Boolean} is the hand busted?
     */
    isBusted(){ return this.getScore() > 21; }

    /**
     * Calculates the hand score, saving Aces for last because they
     * are 11 if they don't bust and 1 if they do.
     * 
     * @return {Integer} score
     */
    getScore(){
        var idx, card, cardValue, ace;
        var score = 0;
        var aceCount = 0;

        // Iterate through hand, scoring cards by ordered index in `pips` array
        for (idx in this.cards) {
            card = this.cards[idx];
            if (card.pip != 'ACE') {
                cardValue = lodash.findIndex(pips, pip => pip == card.pip ) + 1;
                score = score + cardValue;
            } else {
                aceCount = aceCount + 1;
            }
        }

        // For every ace, add the relevant score
        for (ace in aceCount) {
            if ((score + 11) > 21) {
                score = score + 1;
            } else {
                score = score + 11;
            }
        }

        return score;
    }

}

/**
 * Given a score, determines the result of a round.
 * 
 * @param  {Integer} score
 */
function declareResult(score) {
    console.log('* * * * * * * * * * * * * * * *');
    if (score < 21) {
        console.log('Your score is:', score);
    } else if (score == 21) {
        console.log('Blackjack! Damn fine job.');
    } else {
        console.log('Busted! Better luck next time.');
    }
    console.log('* * * * * * * * * * * * * * * *');
}

/**
 *  Plays a round of Blackjack
 * 
 */
function playRound() {
    var deck = new Deck();
    var hand = new Hand();
    var x, option, busted;

    deck.shuffle();

    // Deal 2 cards to hand
    for (x in lodash.range(2)) {
        hand.add(deck.deal());
    }

    // Label the loop for continues/breaks
    round:
    while(true) {
        console.log('Your Hand:');
        hand.print();
        console.log('Current Score:', hand.getScore());
        if (hand.isBusted()) {
            declareResult(hand.getScore());
            break round;
        } else if (hand.getScore() == 21) {
            declareResult(hand.getScore());
            break round;
        } else {
            option = rls.question('Hit (h) or Stay (s)?\n');
        }

        switch(option.toLowerCase()) {
            // Player decides to `hit`
            case 'h':
                hand.add(deck.deal());
                continue round;
            // Player decides to `stay`
            case 's':
                declareResult(hand.getScore());
                break round;
            // Player can't read or type correctly, keep prodding
            default:
                continue round;
        }
    }

    return rls.question('Would you like to play again? (y/n)\n').toLowerCase() == 'y';
}

/**
 * Main function, holds game loop
 * 
 */
function main() {
    while(playRound()){}
}

// Run main function
main();
from random import shuffle

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
        
    def __repr__(self):
        return "{} of {}".format(self.value,self.suit)
        
# c = Card("Hearts","A")
# c2 = Card("Diamonds","10")
# c3 = Card("Spades","K")
# print(c,c2,c3)

class Deck:
    def __init__(self):
        suits = ["Hearts","Diamonds","Clubs","Spades"]
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = [Card(value,suit) for suit in suits for value in values]      
        #print(self.cards)
        
        #OR
        # self.cards = []
        # for suit in suits:
        #     for value in values:
        #         #print(Card(value,suit))
        #         self.cards.append(Card(value,suit))
        #     print(self.cards)
    def __repr__(self):
        return "Deck of {} cards".format(self.count())
    
    def __iter__(self):
        return iter(self.cards)
        
    def count(self):
            return len(self.cards)
            
    def _deal(self,num):
        count = self.count()
        actual = min([count,num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]  # it remove 5 from 52
        self.cards = self.cards[:-actual] #47
        return cards
    
    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self,hand_size):
        return self._deal(hand_size)
        
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self
                
d = Deck()
#d.cards.pop()
#print(d.count())
#d.shuffle()
# card = d.deal_card()
# print(card)
# hand = d.deal_hand(50)
# card2 = d.deal_card()
# print(card2)
# #print(hand)
# print(d.cards)

for card in d:
    print(card)
        
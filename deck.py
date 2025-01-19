suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 
         'Jack', 'Queen', 'King', 'Ace']
# deck = []

# for suit in suits:
#     for rank in ranks:
#         card = (f'{rank} of {suit}')
#         deck.append(card)

deck = [ f'{suit} of {rank}'
        for suit in suits
        for rank in ranks
        if suit == 'Spades'] # added conditional of only spades

print(deck)

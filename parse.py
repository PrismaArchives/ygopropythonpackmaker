import json
import requests


class YgoParser:


    #Create empty array that can be assigned a value later. Remove test variables when done.
    
    ygo_api = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
    
    
    #request is a Dictionary that's KV pair requests the ygoprodeck API for anything that matches.
    def __init__(self, request):
        self.request = request
        
        #all the cards returned from the request    
        self.cards = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php', params=request)
        
        #decode json and have the primary object turn into a dictionary that we define
        self.cards_dict = self.cards.json()
        
        #here we access the data object and now have a list of every card in the search query
        self.card_list = self.cards_dict['data']

        self.curr_card_list = self.card_list
        
        #gets and establishes the length of the card list (amount of cards found) for later use
        self.cl_len = len(self.curr_card_list)
        print(str(self.cl_len) + " Cards Found.")
   

    def getCardInList(self, num):
        if num >= self.cl_len:
            print("number too large! printing card number " + str(self.cl_len - 1) + ", the last card in the list")
            num = self.cl_len - 1
        if num < 0:
            num = 0
            print("negative numbers are invalid, getting first card in list.")
        return self.curr_card_list[num]

    #card is the card beings searched. card is a dictionary, with each value within being a list.
    def getCardInfo(self, card, key):
        #position of the key in the dictionary
        key_dict_pos = -1
        for k1 in card:
            if (k1 == key):
                key_dict_pos = key
        if(key_dict_pos == -1):
            print('invalid key')
        else:
            return card[key_dict_pos]

    #gets every card found with a certain key-value pairs
    def getCardsWithInfo(self, search):
        cards = []
        for card in self.curr_card_list:
            for k1 in card:
                for k2 in search:
                    if(k1 == k2):
                        if (card.get(k1) == search.get(k2)):
                            cards.append(card)
                            
        print(str(len(cards)) + " Cards Found.")
        self.curr_card_list = cards
        return cards

    #removes cards with given information from the current list
    def removeCardsWithInfo(self, search):
        pass


    
    #returns a list with the name of all cards that match parameters
    def getCardNames(self, card_list):
        card_names = []
        for card in card_list:
            card_names.append(self.getCardInfo(card, 'name'))
            
        return card_names
    

    
#x = YgoParser({'race': 'Dragon'})
#print(x.getCardInfo(x.getCardInList(0), 'name'))
#print(x.getCardInfo(x.getCardInList(0), 'race'))
#x.getCardsWithInfo({'archetype':'Blue-Eyes'})
#print(x.getCardNames())


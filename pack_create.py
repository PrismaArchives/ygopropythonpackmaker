from parse import YgoParser


#this is for creating the potential cards in a booster pack, see PackOpen for what cards someone gets from opening a pack
class PackCreator:

    #Initializes with an initial search of potential cards
    def __init__(self, params):
        self.parser = YgoParser(params)
        self.cards_in_pack = self.x.curr_card_list

    #Grab initial listing of cards that meet parameters, parameters is a dictionary
    def filterPotentialPack(self, filter_params):
        cards = []
        for i in self.parser.getCardsWithInfo(filter_params):
            for j in self.cards_in_pack:
                if (i == j):
                    cards.append(i)

        self.cards_in_pack = cards
            
        

    #Add cards with these parameters to the Pack list
    def addCardstoPack(self, params):
        added_cards_list = YgoParser(params).curr_card_list
        self.cards_in_pack.append(added_cards_list)


    def filterOutFromPack(self, filter_params):
        cards = []
        for i in self.parser.getCardsWithInfo(filter_params):
            for j in self.cards_in_pack:
                if (i != j):
                    cards.append(i)

        self.cards_in_pack = cards

    def finalizePack(self):
        self.parser.getCardNames(self.cards_in_pack)
    
#{'name': 'Blue-Eyes White Dragon'}

pack = PackCreator({'archetype' : 'Blue-Eyes'})
pack.filterPotentialPack({'race' : 'Dragon'})
print(pack.parser.getCardNames(pack.cards_in_pack))

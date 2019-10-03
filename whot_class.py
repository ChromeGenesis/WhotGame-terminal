from random import choice
from random import shuffle
from DepotMarket import DepotMarket
from manual import manual

class Whot:
    'A Game of cards usually involving two players by default see manual for more info'                                
    def InitDepot(self):
        Whot.Cards = DepotMarket.copy()
        shuffle(Whot.Cards)
        return Whot.Cards
        
    def InitPlayerCard(self):
        'Initialize player cards'
        self.startcard1 = []
        self.startcard2 = []
        for i in Whot.Cards[0], Whot.Cards[1], Whot.Cards[2], Whot.Cards[3], Whot.Cards[4]:
            self.startcard1.append(i)
        for i in Whot.Cards[5], Whot.Cards[6], Whot.Cards[7], Whot.Cards[8], Whot.Cards[9]:
            self.startcard2.append(i)

    def InitStartCard(self):
        'Initializes start cards for players to play on'
        self.PlayedCards().append(Whot.Cards[10])
        self.PlayedCards().append(Whot.Cards[11])

    def NormCards(self):
        'Normalize the cards if startcard has whot 20 in it'
        if self.PlayedCards()[len(self.PlayedCards())-1][1] == 20:
            misc_cards = []
            for i in Whot.Cards[20], Whot.Cards[21], Whot.Cards[22], Whot.Cards[23], Whot.Cards[24]:
                misc_cards.append(i)
            shuffle(misc_cards)
            self.PlayedCards().append(choice(misc_cards))
            self.NormCards()
            
    def PlayedCards(self, cards=[]):
        'Returns the played cards in an ordered dict'
        return cards
        pass

    def InitPlayer1Cards(self):
        'Initializes the cards for Player1 to start'
        global card1
        card1 = self.startcard1

    def InitPlayer2Cards(self):
        'Initializes the cards for Player2 to start'
        global card2
        card2 = self.startcard2
    
    def Player1Cards(self):
        "returns player1's cards"
        return card1
        pass

    def Player2Cards(self):
        "returns Player2's cards"
        return card2
        pass

    def Manual(self):
        'See the manual of the game'
        man = print(manual)
        return man
        

class Player1(Whot):
    global check_player1_played
    check_player1_played = True
    'Objects and attributes for Player1'        
    def Play(self, playcard):
        'Player1 Plays a valid card in his/her cardstack'
        self.LoopDepot()
        if check_player2_played_before:
            if (playcard) in self.Player1Cards():
                if playcard[0] == self.PlayedCards()[len(self.PlayedCards())-1][0] or playcard[1] == self.PlayedCards()[len(self.PlayedCards())-1][1] or playcard[1] == 20:
                    if playcard[1] == 2:
                        print('Pick Two Cards')
                    elif playcard[1] == 1:
                        print('Hold On')
                    elif playcard[1] == 8:
                        print("Hold On")
                    elif playcard[1] == 14:
                        print("General Market")
                    elif playcard[1] == 20:
                        print('Ask for a card...')
                    print('')
                    print(playcard, 'has been Played')
                    self.PlayedCards().append(playcard)
                    self.Player1Cards().remove(playcard)
                    print('Cards left: ', len(self.Player1Cards()))
                    #check_player1_played = True
                    if len(self.Player1Cards()) == 1:
                        print("Last Card!")
                    elif len(self.Player1Cards()) == 0:
                        print("CheckMate!.....PLAYER 1 HAS WON")
                        exit()
                else:
                    raise WhotException('Error: Invalid Move!')
                    #check_player1_played = False
            else:
                raise WhotException('Error playcard is not in your cardstack!')
                #check_player1_played = False
            return 'list of played cards:  ', self.PlayedCards()
            pass

    
    def gomart(self):
        'Sends Player1 to Market'
        self.LoopDepot()
        self.Player1Cards().append(Whot.Cards[12])
        Whot.Cards.remove(Whot.Cards[12])
        #check_player1_played = True
        pass

    def LoopDepot(self):
        if len(Whot.Cards) <= 25:
            self.InitDepot()

    def sendmart(self):
        'Player1 sends opponent to Market'
        self.LoopDepot()
        self.Player2Cards().append(Whot.Cards[13])
        Whot.Cards.remove(Whot.Cards[13])
        pass
    
    def Player1Cards(self):
        return card1
        pass

    def gogenmart(self):
        self.LoopDepot()
        self.Player1Cards().append(Whot.Cards[14])
        Whot.Cards.remove(Whot.Cards[14])
        #check_player1_played = True
        pass

    def sendgenmart(self):
        self.LoopDepot()
        self.Player2Cards().append(Whot.Cards[15])
        Whot.Cards.remove(Whot.Cards[15])
        pass
    

class Player2(Whot):
    'Objects and attributes for Player2'
    global check_player2_played_before
    check_player2_played_before = True
    def Play(self, playcard):
        'Player2 Plays a valid card in his/her cardstack'
        self.LoopDepot()
        if check_player1_played:
            if (playcard) in self.Player2Cards():
                if playcard[0] == self.PlayedCards()[len(self.PlayedCards())-1][0] or playcard[1] == self.PlayedCards()[len(self.PlayedCards())-1][1] or playcard[1] == 20:
                    if playcard[1] == 1:
                        print("Hold On")
                    elif playcard[1] == 2:
                        print("Pick Two")
                    elif playcard[1] == 8:
                        print("Hold On")
                    elif playcard[1] ==14:
                        print("General Market")
                    elif playcard[1] == 20:
                        print("Ask for a card...")
                    print('')
                    print(playcard, 'has been Played')
                    self.PlayedCards().append(playcard)
                    self.Player2Cards().remove(playcard)
                    print('Cards left: ', len(self.Player2Cards()))
                    #check_player2_played_before = True
                    if len(self.Player2Cards()) == 1:
                        print("Last Card!")
                    elif len(self.Player2Cards()) == 0:
                        print("CheckMate!.....PLAYER 2 HAS WON")
                        exit()
                else:
                    raise WhotException('Error: Invalid Move!')
                    #check_player2_played_before = False
            else:
                print('Error: playcard is not in your cardstack!')
                #check_player2_played_before = False
            return 'list of played cards:  ', self.PlayedCards()
            pass
        else:
            raise WhotException("Its not your turn to play!......Player1 has to play first")
        
    def LoopDepot(self):
        if len(Whot.Cards) <= 25:
            self.InitDepot()

    def gomart(self):
        self.LoopDepot()
        self.Player2Cards().append(Whot.Cards[16])
        Whot.Cards.remove(Whot.Cards[16])

    def sendmart(self):
        self.LoopDepot()
        self.Player1Cards().append(Whot.Cards[17])
        Whot.Cards.remove(Whot.Cards[17])


    def Player2Cards(self):
        return card2
        pass

    def gogenmart(self):
        self.LoopDepot()
        self.Player2Cards().append(Whot.Cards[19])
        Whot.Cards.remove(Whot.Cards[19])

    def sendgenmart(self):
        self.LoopDepot()
        self.Player1Cards().append(Whot.Cards[18])
        Whot.Cards.remove(Whot.Cards[18])

class WhotException(Exception):
    def __init__(self, message):
        self.message = message
        self.run()
    def run(self):
        return self.message

g=Whot()
g.InitDepot()
g.InitPlayerCard()
g.InitPlayer1Cards()
g.InitPlayer2Cards()
g.InitStartCard()
g.NormCards()

if __name__ == '__main__':
    p1=Player1()
    p2=Player2()
    pc=g.PlayedCards()
    pc1=p1.Player1Cards()
    pc2=p2.Player2Cards()

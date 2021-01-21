import random               # for dice roll and shuffling of deck
import pyinputplus as pyip  # used to have check validation on input from the user  pip install pyinputplus
import time                 # for using sleep function
import emoji                # to use emoji when win and drawing game  $ pip install emoji --upgrade

class Card:
 def __init__(self, name, suit):               # init constructor of Card class
     self.suit = suit
     self.top_speed,self.engine_size,self.cool_factor,self.innovation,self.engine_capacity,self.no_of_year_old=name   # unpacking of literals
     self.showing = False

 def __repr__(self):                            # string represenattion of a Card Object
    if self.showing:                            # if card show variable TRue , show the card features else keep it down 
      return  str(self.suit) + " has features of strength " + " top_speed = "+str(self.top_speed)+", engine_size = "+str(self.engine_size)+", cool_factor = "+str(self.cool_factor)+", innovation = "+str(self.innovation)+", engine_capacity = "+str(self.engine_capacity)+", and no_of_year_old = "+str(self.no_of_year_old)
    else:
      return "Face Down"

class StandardDeck:

  def __init__(self):     # init constructor of StandardDeck class
                                
    self.cards = []       # list of 16 cards created and appended
    self.outdateddeck=[]  #  outdated deck are appened when the game starts after each round
    suits = ["Aston_Martin","Audi","BMW","Chevrolet","Datsun","Ford","Maruti","Zen","Polo","Ferrai","Porsche","XUV","Kissan","Swift","Ambassdor","Desizre"]
    values = {"top_speed":[98, 79, 70, 84, 97, 81, 89, 86, 77, 76, 96, 82, 71, 93, 99, 74],       # higher the value ,the better feature 
              "engine_size":[18, 2, 14, 17, 8, 19, 3, 10, 15, 13, 7, 9, 4, 16, 1, 12],            # higher the value ,the better feature 
              "cool_factor":[9, 18, 14, 13, 6, 1, 16, 2, 10, 3, 12, 11, 4, 7, 15, 5],             # higher the value ,the better feature 
              "innovation":[19, 7, 13, 2, 6, 16, 11, 3, 18, 10, 1, 5, 9, 4, 8, 17],               # higher the value ,the better feature 
              "engine_capacity":[57, 43, 38, 78, 71, 86, 36, 32, 64, 49, 60, 76, 40, 66, 30, 74], # higher the value ,the better feature 
              "no_of_year_old":[12, 1, 15, 9, 14, 5, 8, 11, 17, 19, 13, 7, 10, 16, 6, 2],         # lower the value ,the better feature 
               }
    _i=0                                     # internal variable created for using in for loop 
    for suit  in suits:
        self.cards.append( Card( [values[x][_i] for x in values], suit) )
        _i+=1

  def __repr__(self):                         # string represchoosen_featureion of standardeck object
    return "Standard deck of cards:{0} remaining".format(len(self.cards))

  def shuffle(self, times=1 ):               # to shuffle main deck of cards
    random.shuffle(self.cards)
    print("Deck Shuffled \n")

  def outdateddeckshuffle(self, times=1 ):   # to shuffle outdateddeck of cards when each card is added to the list 
    random.shuffle(self.outdateddeck)
    # print("OutdatedDeck Shuffled")

  def draw_card(self):                       # for drawing a card and distributes the deck among 2 players 
    return self.cards.pop(0)


class Player:

    def __init__(self,player_name="1"):   # init constructor of Player Class
        self.player_name=player_name      # intance variable to hold player names
        self.player_hand=[]               # instnace variable to hold each player deck of cards initailly empty
        self.player_roll_die_wins=False   # to keep the track of who wins the roll die throw
        self.points=0                     # To keep a track of points against each player name to decide winner in each round and the winner in end of game 
        self.turn=False                   # to keep track of players turn
        self.godspellbool=False           # to keep track of and to allow player to play god spell once
        self.reserructspellbool=False     # to allow player to play resuct spell once 
        self.flag=True                    # flag to check that a single player cannot play god spell and resreuct in single round

    def draw_card(self,deck):
        # print(f'Player {self.player_name} is drawing  a card')
        self.player_hand.append(deck.draw_card())


# die_roll function for two players     
def dice_roll():
    player1.roll_die_number=0
    player2.roll_die_number=0
    player1.player1wins=0
    player2.player2wins=0
    round=0

    while True:
        round=round+1
        print(f'Round {str(round)} of Die roll {emoji.emojize(":game_die:")} \n')
        ent=input(f'Player {player1.player_name} please press enter on the keyboard to roll the die once \n') 
        
        if ent=="":                               # hitting choosen_featureer ==""
           player1.roll_die_number = random.randint(1,6)
        ent1=input(f'Player {player2.player_name} please press enter on the keyboard to roll the die once \n') 
        
        if ent1=="":                               # hitting choosen_featureer ==""
          player2.roll_die_number = random.randint(1,6)
        print(f'Player {player1.player_name} Roll Dice Number is {player1.roll_die_number} \n')
        print(f'Player {player2.player_name} Roll Dice Number is {player2.roll_die_number} \n')
        if player1.roll_die_number == player2.roll_die_number:
            print(f'Draw, Lets roll the die again {emoji.emojize(":neutral_face:")} \n')    # if draw occurs continue the dice throw  
            continue
        elif player1.roll_die_number > player2.roll_die_number:
            print(f'{player1.player_name} Wins the Roll Die and will start the game  {emoji.emojize(":smiling_face_with_smiling_eyes:")} \n') 
            player1.player_roll_die_wins=True
            player1.turn=True
            break
        else  : 
             print(f'{player2.player_name} Wins the Roll Die and will start the game {emoji.emojize(":smiling_face_with_smiling_eyes:")} \n')
             player2.player_roll_die_wins=True
             player2.turn=True
             break
                
global gameround # a boolean for game round to give option to both players to play resseruct spell after round 1
gameround=0

# to compare charcaterstic of two cards
def check(choosen_feature,popped1,popped2,round):  # check function to cmpare the characterstic of two cards based on user input which feature to compare
        if choosen_feature=="top_speed" :
            if popped1.top_speed > popped2.top_speed:
                player1.points=player1.points+1
                print(f'Player 1 {player1.player_name} has win round {round} {emoji.emojize(":glowing_star:")} \n')
                player1.turn=True
            else:
                player2.points=player2.points+1  
                print(f'Player 2 {player2.player_name} has win round {round} {emoji.emojize(":glowing_star:")} \n')
                player2.turn=True     
        if choosen_feature=="engine_size" :
            if popped1.engine_size > popped2.engine_size:
                player1.points=player1.points+1
                print(f'Player 1 {player1.player_name} has win round {round} {emoji.emojize(":glowing_star:")} \n')
                player1.turn=True
            else:
                player2.points=player2.points+1
                print(f'Player 2 {player2.player_name} has win round {round} {emoji.emojize(":glowing_star:")} \n') 
                player2.turn=True  
        if choosen_feature=="cool_factor":
            if popped1.cool_factor > popped2.cool_factor:
                player1.points=player1.points+1
                print(f'Player 1 {player1.player_name} has win round {round} {emoji.emojize(":glowing_star:")} \n')
                player1.turn=True
            else:
                player2.points=player2.points+1 
                print(f'Player 2 {player2.player_name} has win round {round} {emoji.emojize(":glowing_star:")} \n')
                player2.turn=True
        if choosen_feature=="innovation" :
            if popped1.innovation > popped2.innovation:
                player1.points=player1.points+1
                print(f'Player 1 {player1.player_name} has win round {round} {emoji.emojize(":glowing_star:")} \n')
                player1.turn=True
            else :
                player2.points=player2.points+1
                print(f'Player 2 {player2.player_name} has win round {round} {emoji.emojize(":glowing_star:")} \n')
                player2.turn=True            
        if choosen_feature=="engine_capacity":
            if popped1.engine_capacity > popped2.engine_capacity:
                player1.points=player1.points+1
                print(f'Player 1 {player1.player_name} has win round {round} {emoji.emojize(":glowing_star:")} \n')
                player1.turn=True
            else :
                player2.points=player2.points+1
                print(f'Player 2 {player2.player_name} has win round {round}{emoji.emojize(":glowing_star:")} \n')
                player2.turn=True
        if choosen_feature=="no_of_year_old":
            if popped1.no_of_year_old > popped2.no_of_year_old:
                player2.points=player2.points+1
                print(f'Player 2 {player2.player_name} has win round {round} {emoji.emojize(":glowing_star:")} \n')
                player2.turn=True 
            else :
                player1.points=player1.points+1
                print(f'Player 1 {player1.player_name} has win round {round} {emoji.emojize(":glowing_star:")} \n')
                player1.turn=True

        popped2.showing= False              # popped card is now kept face down before appending to outdated deck
        popped1.showing= False              # popped card is now kept face down before appending to outdated deck
        deck.outdateddeck.extend([popped1,popped2])  # card popped by player 1 and player2 are appended to outdated deck as individual cards
        deck.outdateddeckshuffle()         # oudated deck is shuffled after another card ia added

# implementation of God spell
def Godspell(player1,player2,variable1=False,variable2=False):
   if player1.godspellbool and variable1:
        cardposition=pyip.inputNum(prompt=f"Please choose a card that you want your opponent {player2.player_name} to select from the deck.Your opponent currently has {len(player2.player_hand)} cards left now ",min=1,max=len(player2.player_hand))
        player2.player_hand.append(player2.player_hand.pop(cardposition-1))        # re-arranging the list of player 2 cards ( the popped card is appened to the end of the player 2 cards list)
        return player2.player_hand
   elif player2.godspellbool and variable2:
        cardposition=pyip.inputNum(prompt=f"Please choose a card that you want your opponnet {player1.player_name} to select from the deck.Your opponent currently has {len(player1.player_hand)} cards left now ",min=1,max=len(player1.player_hand))
        player1.player_hand.append(player1.player_hand.pop(cardposition-1))       # re-arranging the list of player 1 cards ( the popped card is appened to the end of the player 1 cards list)
        return player1.player_hand


# implementation of Resseruct spell    
def Resurrect_spell(player1,player2,var1=False,var2=False):
    if player1.reserructspellbool and var1:
        randomcardposition=random.randint(0,len(deck.outdateddeck)-1)            # create a random number from a outdated deck between 0 postion and 1 less than outdated deck length
        print(f'The random card picked from outdated deck is at position {randomcardposition} and is currently {deck.outdateddeck[randomcardposition]} added to your deck {player1.player_name} \n ')  
        player1.player_hand.append(deck.outdateddeck.pop(randomcardposition))    # append the card at the last ( end of deck)
    elif player2.reserructspellbool and var2:
        randomcardposition=random.randint(0,len(deck.outdateddeck)-1)            # create a random number from a outdated deck from 0 to len(deck)-1
        print(f'The random card picked from outdated deck is at position {randomcardposition} and is currently {deck.outdateddeck[randomcardposition]} added to your deck {player2.player_name} \n' )  
        player2.player_hand.append(deck.outdateddeck.pop(randomcardposition))    # append the card at the last ( end of deck)


# playing of normal game
def normal_game(gameround):
      round=1
      while(len(player1.player_hand)>=1 and len(player2.player_hand)>=1):   # game continue till the player deck are over
          print(f'Game Round No {round}') 
          if player1.turn:
              if gameround and not player1.reserructspellbool: 
                  response=pyip.inputYesNo(prompt=f"{player1.player_name} Do you want to play Resurrect spell [Yes/No] \n")  
                  if response=="yes":
                      player1.reserructspellbool=True
                      player1.flag=False
                      var1,var2=True,False
                      Resurrect_spell(player1,player2,var1,var2)   # calling the function reserruct spell
                  elif response=="no":
                      pass    

              print(f"Player {player1.player_name} will pick the card first now \n")

              popped1=player1.player_hand.pop(-1)
              popped1.showing=True     # card is shown now after picking
              player1.turn=False       # player 1 turn is set to false now
              
              choosen_feature=pyip.inputMenu(["top_speed" ,"engine_size" ,"cool_factor","innovation" ,"engine_capacity","no_of_year_old"],numbered=True,prompt=f'Player 1 {player1.player_name} Please select one of the following feature to challenge your opponent on \n')
              
              if not player1.godspellbool and player1.flag: # flag varaible to ensure a person cannot play god spell and reseruct spell both in once round
                    response=pyip.inputYesNo(prompt=f'{player1.player_name} Do you want to pay God spell [Yes/No] \n')  
                    if response=="yes":
                        player1.godspellbool=True 
                        variable1,variable2=True,False
                        player2.player_hand=Godspell(player1,player2,variable1,variable2)
                        time.sleep(1)
                        if player1.godspellbool and not player2.reserructspellbool and gameround:  
                             response=pyip.inputYesNo(prompt=f"{player2.player_name } Do you want to play Resurrect spell [Yes/No] \n")  # if player 2 choose to play reseruct in reponse to if player 1 plays god spell
                             if response=="yes":
                                  player2.reserructspellbool=True
                                  var1,var2=False,True
                                  Resurrect_spell(player1,player2,var1,var2) # doubt on this line
                                  player1res=pyip.inputMenu(["Resercuted card","Earlier choice"],numbered=True,prompt=f'Player 1 {player1.player_name} please select which you want Player 2 {player2.player_name} to play with now \n')
                                  if player1res=="Resercuted card":
                                      pass
                                  elif player1res=="Earlier choice":                    # if the player 1 chooses earlier card , then second card from top is popped and appened to last of the deck list
                                        player2.player_hand.append(player2.player_hand.pop(-2))                       
                    elif response=="no":
                           pass    

              if (gameround and not player2.reserructspellbool):
                  response=pyip.inputYesNo(prompt=f"{player2.player_name} Do you want to play Resurrect spell [Yes/No] \n")  # doubt on this line
                  if response=="yes":
                      player2.reserructspellbool=True
                      var1,var2=False,True
                      Resurrect_spell(player1,player2,var1,var2)
                  elif response=="no":
                      pass 


              print(f'Player 2 {player2.player_name} will pick the card now \n')

              popped2=player2.player_hand.pop(-1)
              popped2.showing=True 
              player2.turn=False
              time.sleep(1)
              print(f'The card taken by player 1 {player1.player_name} is {popped1} \n') 
              print(f'The card taken by player 2 {player2.player_name} is {popped2} \n')
              check(choosen_feature,popped1,popped2,round)  
              gameround=1   
              player1.flag=True 

          elif player2.turn:
              if (gameround and not player2.reserructspellbool):
                  response=pyip.inputYesNo(prompt=f"{player2.player_name } Do you want to play Resurrect spell [Yes/No] \n")  
                  if response=="yes":
                      player2.reserructspellbool=True
                      player2.flag=False
                      var1,var2=False,True
                      Resurrect_spell(player1,player2,var1,var2)
                  else :
                      pass 
              print(f"Player 2 {player2.player_name} will pick the card first now \n")      
              popped2=player2.player_hand.pop(-1)
              popped2.showing=True
              player2.turn=False

              choosen_feature=pyip.inputMenu(["top_speed" ,"engine_size" ,"cool_factor","innovation" ,"engine_capacity","no_of_year_old"],numbered=True,prompt=f'Player 2 {player2.player_name} Please select one of the following feature to challenge your opponent on \n' ) 

              if not player2.godspellbool and player2.flag:
                  response=pyip.inputYesNo(prompt=f'{player2.player_name} Do you want to pay God spell [Yes/No] \n')  
                  if response=="yes":
                        player2.godspellbool=True 
                        variable1,variable2=False,True
                        player1.player_hand=Godspell(player1,player2,variable1,variable2)  #at here
                        time.sleep(1)
                        if player2.godspellbool and not player1.reserructspellbool and gameround:
                            response=pyip.inputYesNo(prompt=f"{player1.player_name } Do you want to play Resurrect spell [Yes/No] \n")  # if player 1 choose to play reseruct in reponse to if player 2 plays god spell
                            if response=="yes":
                                  player1.reserructspellbool=True
                                  var1,var2=True,False
                                  Resurrect_spell(player1,player2,var1,var2)
                                  player2res=pyip.inputMenu(["Resercuted card","Earlier choice"],numbered=True,prompt=f'Player 2 {player2.player_name} please select which you want Player 1 {player1.player_name} to play with now \n')
                                  if player2res=="Resercuted card":  # if the user chooses reseructed card, then nothing needs to be done as it will be automatically at first poistion of the deck
                                      pass
                                  elif player2res==  "Earlier choice":
                                      player1.player_hand.append(player1.player_hand.pop(-2))   #if it is earlier chocie then , the card at 2 position is added to top of deck again
                    
                  else:
                        pass 
                  
              if (gameround and not player1.reserructspellbool):
                  response=pyip.inputYesNo(prompt=f"{player1.player_name } Do you want to play Resurrect spell [Yes/No] \n")  
                  if response=="yes":
                      player1.reserructspellbool=True
                      var1,var2=True,False
                      Resurrect_spell(player1,player2,var1,var2)
                  elif response=="no":
                      pass  
        
              print(f'Player 1 {player1.player_name} will pick the card now  \n')
              popped1=player1.player_hand.pop(-1)
              popped1.showing=True  
              player1.turn=False
              time.sleep(1)
              print(f'The card taken by player 1 {player1.player_name} is {popped1} \n') 
              print(f'The card taken by player 2 {player2.player_name} is {popped2} \n')
              check(choosen_feature,popped1,popped2,round)
              gameround=1 
              player2.flag=True    
          round+=1

      # for deciding final winner of the Game                         
      if player1.points>player2.points:
              print(f'{player1.player_name} wins the Final Game against {player2.player_name} by {player1.points-player2.points} points {emoji.emojize(":glowing_star:")} {emoji.emojize(":glowing_star:")} {emoji.emojize(":glowing_star:")} \n ')
      elif player1.points==player2.points:
              print(f'{player2.player_name} and {player1.player_name} have a draw {emoji.emojize(":neutral_face:")} \n')
      else:    
              print(f'{player2.player_name} wins the Final Game against {player1.player_name} by {player2.points-player1.points} points {emoji.emojize(":glowing_star:")} {emoji.emojize(":glowing_star:")} {emoji.emojize(":glowing_star:")}\n')


if __name__=="__main__":
 
  deck=StandardDeck()   # create an instance of standarddeck class and it will craete a deck of 16 cards calling Card class
  deck.shuffle()        # schuffle the deck after creating it goes to line no 40

  input1=pyip.inputStr(f'Please enter Player 1 name {emoji.emojize(":man:")} \n')
  input2=pyip.inputStr(f'Please enter Player 2 name {emoji.emojize(":woman:")} \n')

  player1=Player(input1.upper())   # create 2 instaces of player class with their instance variable
  player2=Player(input2.upper())
  
  # perparing the individual deck for each player ( equally dictribute 8 cards among each player)
  while len(deck.cards)>0:
     player1.draw_card(deck)
     player2.draw_card(deck)
  
  dice_roll()                 # calling dice roll function to decide who will start the game and setting players turn
           
  normal_game(gameround)      # calling for normal_game function


  
    
  
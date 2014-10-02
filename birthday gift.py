 #done--
input ("Hi mom Happy birthday!> ")
input ("welcome to your birthday supprise!>")
input ("I know you couldn't find a good puzzle game so I made my own. >")

def dogcat():
    input ("so lets start off small with a question. >")

    catdog = input ("what is your first childs name. ").strip().lower()

    if catdog ==("soren"):
        input ("ok good you remember! >")
        input ("the puzzles are all linked, your end goal is to create a birthday cake!> ")
        input ("and the best part is there is no images on the screen so you can't get sick>")
        input ("ok now lets begin.>")
        input ("so what do you want to get first on the list?> ")
        input ("your son should hand you a sheet now.>")
        dogdog()


    elif catdog == ("devin"):
        input ("really? just wow try again.>")

    else:
        input ("I am sorry what ever you typed is not correct ")
    dogcat()

#answer to name------------------------------------------------------------------
#done--
def dogdog():
    input ("each item has a code, right down the code every time you complete an area>")
    
    catcat = input ("so now you know how this works choose one on the list just type in the name. ")

    if catcat == ("cake"):
        input ("ok go right ahead!> ")
        cake1()
    elif catcat == ("invisable candles"):
        input ("good choose loading puzzle.> ")
        invis()
    elif catcat == ("icing"):
        input ("ok then lets do this!>")
        doorofdoom()
    elif catcat == ("happiness"):
        input ("good choice moving on! ")
        happy1()
    elif catcat == ("solve"):
        winner()

    else:
        input ("I do not understand")
    dogdog()


#cake2---------------------------------------------------------------------------
#done--
def cake1():
    input ("you enter a maze showen on the sheet at each of the dead ends is a number.> ")
    input ("reach all the ends the put them in order from least to greatest.> ")
    input ("input your aswer by typing answer at any dead end.> ")
    input ("remember to type R or L to move.> ")


    derp = input ("would you still like to continue{yes or no} ").strip().lower()

    if derp == ("yes"):
        input ("you continue into the maze")
        maze1()
    elif derp == ("no"):
        input ("ok choose another path.> ")
        dogdog()
    else:
        input ("I am sorry I do not understand. ")
    cake1()


#maze1---------------------------------------------------------------------------
#done--
def maze1():

    mazerunner = input ("would you like to go right{R} or left{L} or forward {F}. ").strip().lower()

    if mazerunner == ("R"):
        input ("you head right. ")
        rightend()
    elif mazerunner == ("L"):
        input ("you head left. ")
        firstleft()
    elif mazerunner == ("F"):
        input ("you deside to head forwards. ")
        forwardsone()

    else:
        input ("I am sorry I do not understand. ")
    maze1()

#mazerightdeadend---------------------------------------------------------------
#done--
def rightend():
    input ("you found a dead end, the number is {23}.> ")

    thomas = input ("would you like to answer the code or go back for more answers? ")

    if thomas == ("go back"):
        input ("you deside to go find more numbers. ")
        maze1()
    elif thomas == ("answer"):
        input ("ok")
        mazeanswer()
    else:
        input ("I am sorry I do not understand. ")
    rightend()
    







#mazeanswer---------------------------------------------------------------------
#done--
def mazeanswer():
    input("please list the numbers,> ")

    answerthequestion = ("remember to list them in order from least to greatest, with a space in between each one. ")

    if answerthequestion == ("1 18 23 50 820"):
        input ("you are correct the cake code for the sheet is {12}.you go to the start to find another part to the cake ")
        dogdog()
    elif answerthequestion == ("go back"):
        input ("you go back into the maze. ")
        maze1()
    else:
        input ("I am sorry that is incorrect.if you want to go back type {go back}. ")
    mazeanswer()
#maze forwardsone----------------------------------------------------------------
#done--
def forwardsone():

    deadendForL = input ("you come to a cross road would you lik to go forward or left?answer with{L or F}. ")

    if deadendForL == ("F"):
        input ("you deside to go forwards")
        forwardendmiddle()
    elif deadendForL == ("L"):
        input ("you travel to the left")
        leftofthemiddle()
    else:
        input ("I am sorry I do not understand. ")
    forwardsone()
    
#forwardendmiddle-----------------------------------------------------------------
#done--
def forwardendmiddle():
    input ("you come to a dead end, there is a number on the wall {1}. ")

    endoftheline = input ("you now have two options, you can {go back} to the start, or try to {answer} the question. ")

    if endoftheline == ("go back"):
        input ("you head back to the start to find more numbers. ")
        maze1()
    elif endoftheline == ("answer"):
        input ("you attempt to solve the puzzle. ")
        mazeanswer()
    else:
        input ("I am sorry I do not understand. ")
        forwardendmiddle()
#leftofthemiddle----------------------------------------------------------------
#done--
def leftofthemiddle():
    input ("you come to a dead end, on the wall is a number{50}. ")

    middleoftheleft = input ("you found a new number would you like to try to solve the maze or go back. ")

    if  middleoftheleft == ("solve"):
        input ("you are now attempting to solve the maze. ")
        mazeanswer()
    elif middleoftheleft == ("go back"):
        input ("you head back in seach of more numbers. ")
        maze1()
    else:
        input ("I am sorry I do not understand. ")
    leftofthemiddle()
        
#firstleft-----------------------------------------------------------------------
#done--
def firstleft():
    input("after walking for a while you turn the corner.> ")
    input ("you come to a crossroad.> ")

    pickledpeper = ("would you like to go forwards or right. ")

    if pickledpeper == ("F"):
        input ("you deside to go forwards. ")
        FirLefFor()
    elif pickledpeper == ("right"):
        input ("you head to the right. ")
        rightofleft()
    else:
        input ("I am sorry I do not understand. ")
    firstleft()        

#FirLefright---------------------------------------------------------------------
#done--
def rightofleft():
    input ("you find a dead end with a number{this number is interactive with the real world how many books are on top of soren's cabnit in his room}. ")

    llama = input ("would you like to try to solve the maze or go back to find more numbers. ").strip().lower()    

    if llama == ("go back"):
        input ("you go back into the maze to find more numbers. ")
        maze1()
    elif llama == ("solve"):
        input ("you attempt to solve the maze. ")
        mazeanswer()
    else:
        input ("I am sorry I do not understand. ")
    rightofleft()

#FirLefFor-----------------------------------------------------------------------
#done--
def FirLefFor():
    input ("you come to a dead end with a number{there are 4 green cards hidden in the game room,the highest moltiple you can create with the cards is your answer. ")

    turkey = input ("would you like to try to solve the puzzle or go back to find more answers. ")

    if turkey == ("solve"):
        input ("you try to solve the maze. ")
        mazeanswer()
    elif turkey == ("go back"):
        input ("you deside to go back. ")
        maze1()
    else:
        input ("I am sorry I do not understand. ")
    FirLefFor()
#happy1-------------------------------------------------------------------------        
def happy1():
    ("are you happy? ")

    alpaca = input ("answer yes or no. ")

    if alpaca == ("yes"):
        input ("you achive happiness the code is {32}. ")
        dogdog()

    elif alpaca == ("no"):
        input ("really? ")
    happy1()   


#inviscandles1-------------------------------------------------------------------
def invis():
    input ("you come upon a chest with multiple locks each one has a question. ")

    crockodile = input ("would you like to answer this puzzle or back to the start? ")

    if crockodile == ("yes"):
        input ("you continue. ")
        lock1()
    elif crockodile == ("no"):
        input ("you deside to head back")
        dogdog()
    else:
        input ("I am sorry I do not understand. ")
    invis()

#lock1----------------------------------------------------------------------------
#done--
def lock1():
    input ("you look at the first lock. ")

    baby = input (" it asks what did you want to name bella. ").strip().lower()

    if baby == ("mocha"):
        input ("correct moving on. ")
        lock2()
    else:
        input ("nope, try again. ")
    lock1()

#lock2----------------------------------------------------------------------------
def lock2():
    input ("you now pay attention to the second lock. ")
    input ("the next answer is in the form of a riddle... ")
    input ("Llamas and Orange Omlets Killed your Urban Pineapple. ")
    domino1 = ("when you find the answer type it in. ")

    if domino1 == ("1262"):
        input ("correct! moving on. ")
        lock3()
    else:
        input ("I am sorry I do not understand. ")
    lock2()
#lock3-----------------------------------------------------------------------------        
def lock3():
    input("the chest gives you a challenge.> ")
    input("you must tie a knot in the string provided, but you are not alowed to let go of the ends of the string.> ")

    dogbird = input ("when you solve this your son will hand you a card, enter the number on the card. ")

    if dogbird ==("1560"):
        input ("that is correct, the invisable candle code has been added{222}. ")
        dogdog()
    else:
        input ("incorrect")
    lock3()
    
#icing------------------------------------------------------------------------------
def doorofdoom():
    input ("there is a door with a single question")

    hotdog = input ("what is 6 divided by a half?")
    if hotdog == ("12"):
         input ("you got the code {20}. ")
        dogdog()
    else:
        input ("I am sorry I do not understand. ")
    doorofdoom()

#ending---------------------------------------------------------------------------------
def winner():
    input ("you have reached the end! ")
    youareawinner = input ("what are the codes in the order on the sheet with spaces between them. ")

    if youareawinner == ("12 222 20 32"):
        input ("HAPPY BIRTHDAY MOM!")
        input ("I love you so much. ")
        input ("now get a big hug from the one you love the most! ")

    else:
        input ("I am sorry I do not understand. ")












dogcat()

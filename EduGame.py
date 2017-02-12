import RPi.GPIO as GPIO
import random
import Mathgame
import Logicgame



GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.output(2, 1)
GPIO.output(3, 1)
GPIO.output(4, 1)
GPIO.output(17, 1)



def clearscreen() :
    for i in range(0,24,1) :
        print("\n")

def mathGameMenu() :
        print("Welcome to the math game!")
        mgamechoice = input("Choose an operation to practice:\n"
              "1. Addition & Subtraction\n"
              "2. Multiplication & Division\n"
              "3. Exponents and Roots\n")
        return int(mgamechoice)

def addsub():
    print("Directions: Fill in the blank to make the statement true.\n")
    a = random.randrange(1,999,1)
    b = random.randrange(1,999,1)
    #operation = random.randrange(1,2,1)
    #if operation == 1:
    ans = a + b
    #else:
     #   ans = a - b
        
    eqstructure = random.randrange(1,3,1)
    if eqstructure == 1:
        print("__ + ",b," = ",ans)
        userans = input("\n>>>>> ")
        if int(userans) == a:
            print("Correct!\n")
        else :
            print("Incorrect! The correct answer is ",a)
    elif eqstructure == 2:
        print(a," + __ = ",ans)
        userans = input("\n>>>>> ")
        if int(userans) == b:
            print("Correct!\n")
        else:
            print("Incorrect! The correct answer is ",b)
    else:
        print(a," + ",b," = __")
        userans = input("\n>>>>> ")
        if int(userans) == ans:
            print("Correct!\n")
        else:
            print("Incorrect! The correct answer is ",ans)
    xt = input("Type 0 to exit, or 1 to continue")
    return int(xt)

def multdiv() :
    print("Directions: Fill in the blank to make the statement true.\n")
    a = random.randrange(1,99,1)
    b = random.randrange(1,99,1)
    ans = a * b
        
    eqstructure = random.randrange(1,3,1)
    if eqstructure is 1:
        print("__ * ",b," = ",ans)
        userans = input("\n>>>>> ")
        if int(userans) is a:
            print("Correct!\n")
        else :
            print("Incorrect! The correct answer is ",a)
    elif eqstructure is 2:
        print(a," * __ = ",ans)
        userans = input("\n>>>>> ")
        if int(userans) is b:
            print("Correct!\n")
        else:
            print("Incorrect! The correct answer is ",b)
    else:
        print(a," * ",b," = __")
        userans = input("\n>>>>> ")
        if int(userans) is ans:
            print("Correct!\n")
        else:
            print("Incorrect! The correct answer is ",ans)
    xt = input("Type 0 to exit, or 1 to continue")
    return int(xt)

def logicGameMenu() :
        print("Welcome to the logic game!")
        print("Directions: ")

#def logicsGamemain() :


print("Welcome to Learn by Doing(tm)!\n"
      "Which game would you like to play today?\n"
      "1. Math Game\n"
      "2. Logic Game\n>>>>> ")
topgamechoice = input()
#int(topgamechoice)
if topgamechoice == "1":
    xtmain = 1
    while xtmain != 0:
        mret = mathGameMenu()
        if mret == 1:
            xtmain = addsub()
        elif mret == 2:
            xtmain = multdiv()
        else:
            print("Error")
    
elif topgamechoice == "2":
    logicGameMenu()
    logicGamemain()
else:
    print("Error3")
    
##gamestart = { 1 : addsub(),
##              2 : multdiv(),
###             3 : exproot(),
##                }
##
##while userans != "exit":
##    gamestart[gamechoice]()

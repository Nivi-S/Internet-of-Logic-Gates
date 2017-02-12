import RPi.GPIO as GPIO
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

print ("Logic Gate Simulation")

def AND (a,b):

    if a == 1 :
        if b == 1:
            return 1
    else:
        return 0

def NAND (a,b):
    if AND(a,b) == 1:
        return 0
    else:
        return 1


def OR(a,b):
    if a == 1:
        return 1
    elif b == 1:
        return 1
    else:
        return 0

def NOT (a):
    if a == 1:
         return 0;
    else :
        return 1
    
def NOR (a, b):
    if OR(a,b) == 1:
        return 0
    else:
        return 1
    
def XOR(a,b):
    if a !=b:
        return 1
    else:
        return 0
    
score = 7
##
##for i in range(0, 5, 1):
##    question = input("What type of gate do you want to simulate - OR, AND, NOT, NAND, or XOR?  ")
##
##    if question == 'AND':
##        a = random.randrange(0, 2, 1)
##        b = random.randrange(0, 2, 1)
##        print("A = ", a, " ", "B = ", b)
##        x = AND(a,b)
##        userans = int(input("A AND B = ? \t"))
##        if userans == x:
##            score += 1
##        print("score = " ,score)
##
##    elif question == 'OR':
##        a = random.randrange(0, 2, 1)
##        b = random.randrange(0, 2, 1)
##        print("A = ", a, " ", "B = ", b)
##        x = OR(a,b)
##        userans = int(input("A OR B = ? \t"))
##        if userans == x:
##            score += 1
##        print("score = " ,score)
##
##    elif question == 'NOT':
##        a = random.randrange(0, 2, 1)
##        x= NOT(a)
##        userans = int(input("NOT A = ? \t"))
##        if userans == x:
##            score += 1
##        print("score = " ,score)
##
##
##    elif question == 'NOR':
##        a = random.randrange(0, 2, 1)
##        b = random.randrange(0, 2, 1)
##        print("A = ", a, " ", "B = ", b)
##        x = NOR(a,b)
##        userans = int(input("A NOR B = ? \t"))
##        if userans == x:
##            score += 1
##        print("score = " ,score)
##
##    elif question == 'NAND':
##        a = random.randrange(0, 2, 1)
##        b = random.randrange(0, 2, 1)
##        print("A = ", a, " ", "B = ", b)
##        x = NAND(a,b)
##        userans = int(input("A NAND B = ? \t"))
##        if userans == x:
##            score += 1
##        print("score = " ,score)
##
##    elif question == 'XOR':
##        a = random.randrange(0, 2, 1)
##        b = random.randrange(0, 2, 1)
##        print("A = ", a, " ", "B = ", b)
##        x = XOR(a,b)
##        userans = int(input("A XOR B = ? \t"))
##        if userans == x:
##            score += 1
##        print("score = " ,score)
##        
##    else: break;
##
##    
def dec_to_bin(z):
    if z >= 8:
        return bin(z)[2:]
    elif z < 8 and z >= 4:
        return "0" + bin(z)[2:]
    elif z < 4 and z >= 2:
        return "00" + bin(z)[2:]
    else:
        return "000" + bin(z)[2:]



zi = dec_to_bin(int(score)) 
z = str(zi)
zf0 = int(z[0])
zf1 = int(z[1])
zf2 = int(z[2])
zf3 = int(z[3])
GPIO.output(2,zf0) 
GPIO.output(3,zf1)
GPIO.output(4,zf2)
GPIO.output(17,zf3)

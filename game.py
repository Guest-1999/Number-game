# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 14:52:39 2022

@author: rahma
"""

 
import random
def find_num(x = 10):
    r_num = random.randint(1, x)
    guesses = 0
    print("I will think of a number from 1 to 10, can you find?", end=" " )
    print("Type number below ")
    while True:
        guesses += 1
        try:
            guess = int(input(">>> "))
        except ValueError:
            print("Insert number please!")
            guess = int(input(">>> "))
        if guess > r_num :
                print("Try smaller number")
        elif guess < r_num :
                print("Try bigger number")
        else:
                 break   
    print(f"Congrats, you guessed correct in {guesses}"
                      " shot/s!")
    return guesses
            
    
def pc_find_num(x = 10):
    
    pc_guesses = 0
    low = 1
    high = x
    print("\nNow You think of a number from 1 to 10, I will try to find!")
    input("Press enter to start!")
    while True:
        pc_guesses += 1
        if low != high:
            guess = random.randint(low, high)
        else:
           guess = low
        answer = input(f"You thought of {guess},"
                      " right? Yes(y), my guess is smaller (-),"
                      " my guess is bigger(+) \n>>> ")
        if answer == "-":
            high = guess - 1
        elif answer == "+":
            low = guess + 1
        else:
            break
    print(f"I guessed correct in {pc_guesses} shot/s")
    return pc_guesses


def play(x = 10):
    
    while True:
        user_guess = find_num()
        pc_guess = pc_find_num()
        if user_guess > pc_guess:
            print("I won the game! 🥳👏🎉")
        elif pc_guess > user_guess:
            print("You won the game! 🥳👏🎉")
        else:
            print("\nThe game is tie! 🥳👏🎉")
        more = input("Do you want to play again? Yes(y)/No(n) \n>>> ")
        if more == "n":
            break
    
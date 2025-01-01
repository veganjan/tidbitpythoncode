# MIT License
# Copyright (c) 2025 Jan Sange Hansen ripcurldane@proton.me
# Game based on Chinese Remainder Theorem
# Game where the program guesses what number between 1 and 100 you are thinking of.
# If it doesn't guess right away, it will ask a series of questions--remainders upon division by 3,5,7.
# Author Jan S. Hansen ripcurldane@proton.me

import random
import sys
import time

# Sign-off message
def sign_off():
    print("\nBy: Jan S Hansen",end=" , ")
    print("ripcurldane@proton.me")
    print("© 2024 Jan Sange Hansen. All rights reserved.")

def funn(i, j=None):
    '''When j=None, the function processes the first remainder upon division by 3. Based on this info it guesses at the number. If successful, it finishes and exits.
    When j is not none, the function processes the remainder upon division by 5. Based on the two remainers by division of 3, 5 it guesses at the number. If successful, it finishes and exits.

    '''
    if j is not None:
        intersection = list(set(num3[i]) & set(num5[j]))
        guessN = random.choice(intersection)
        response=input(f"Is your number {guessN} ? (y/n)")
        if response == 'y':
            print("\nHaah! Excellent, I have ESP!!\n")
            sign_off() 
            print("\nHave a great day!!\n")  
            sys.exit()  
    else:
        guessN = random.choice(num3[i])
        response=input(f"Is your number {guessN} ? (y/n)")
        if response == 'y':
            print("\nHaaaah! Excellent, I have ESP!!\n")
            time.sleep(5)
            print("\nHave a great day!!\n") 
            sign_off() 
            sys.exit()  

# construct lists of numbers

num3 = [[i for i in range(1, 101) if i % 3 == remainder] for remainder in range(3)]
num5 = [[i for i in range(1, 101) if i % 5 == remainder] for remainder in range(5)]
num7 = [[i for i in range(1, 101) if i % 7 == remainder] for remainder in range(7)]

print("Think of a number between 1 and 100 !\n")

ready = input("Ready? Press (y/n): ")

# Take a stab in the dar to guess the number.
guessN = random.randint(1, 100)
response=input(f"Is your number {guessN} ? (y/n)")

if response == 'y':
    print("\nHaah! Excellent, I have ESP!!\n")
    time.sleep(5)
    print("\nHave a great day!!\n")  
    sign_off()
    sys.exit()  
    
print("mmh, okay. One more question!\n")

r3 = int(input("Tell me the remainder when dividing by 3? \n\n(0,1,2):  "))

# process remainder upon division by 3
mm = -1

while mm < 3:    
    mm += 1
    if r3 == mm:
        funn(mm,j=None)
        k = mm

print("mmh, okay. Let me ask you aanother question!\n")

r5 = int(input("What's the remainder on division by 5? \n\n (0,1,2,3,4):  "))

# process remainder upon division by 5
mm = -1
while mm < 5:    
    mm += 1
    if r5 == mm:
        funn(k,mm)

print("mmh, okay. Let me ask you a final question!\n")

r7 = int(input("Remainder when you divide by 7? \n\n (0,1,2,3,4,5,6): "))

# Find the number using the remainders upon division by 3,5,7
num1 = (70 * r3) + (21 * r5) + (15 * r7)

num = num1 % 105

print(f"Me thinks your number is {num} :-)!")
time.sleep(5)
print("\nExcellent, I have ESP!!\nHave a great day!!")
 


# Call the sign-off function
sign_off()

# Exit the program
sys.exit()

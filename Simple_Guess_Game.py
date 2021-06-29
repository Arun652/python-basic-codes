import random as r
num=r.randint(1,10)
flag=True
while flag:
    guess=input("Guess the digit between 1-10: ")
    if not guess.isdigit():
        print("Invalid input ,input is not a digit",end='\n')
    elif(int(guess)<num):
        print("The number is close little less ",end='\n')
    elif(int(guess)>num):
        print('oops The number is high then guess ',end='\n')
    else:
        print("Bingo!")
        flag=False
    

import random
#When you run the program you'll get a random number between 1-6
roll_again="yes"
#if you want to roll again you can give the input accordingly
while(roll_again=="yes" or roll_again=="y"):
    #random.randint() function will give you a random integer from the specified range
    print(random.randint(1,7))
    roll_again=input("Do you want to roll again: y/yes or n/no:: ")

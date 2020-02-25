import random

rand_input=random.randint(1,9)


def Guess_number(rand_input):
    no_of_chances=0
    while no_of_chances<3:
        user_input=(input("Guess the number :"))
        no_of_chances=no_of_chances+1
        if user_input==rand_input:
            print ("You have guessed the correct number ",rand_input)
        elif no_of_chances <3:
            print("The guessed number is wrong")
            print ("You have "+str(3-no_of_chances)+" chances left")
        else:
            print ("You lose all the chances")
            print ("The guess number is ", rand_input)


if __name__ =="__main__":
    Guess_number(rand_input)
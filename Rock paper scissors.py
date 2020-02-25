#method -1

def rock_paper_scissors():

    if a==b:
        print ("Its a tie")
    elif a=="rock" and b=="scissors":
        print(a, ", A wins")
    elif a=="rock" and  b=="paper":
        print ("A wins")
    elif a=="paper"and b=="scissors":
        print ("B wins")
    elif a=="paper" and  b=="rock":
        print ("A wins")
    elif a=="scissors" and b == "paper":
        print("A wins")
    elif a=="scissors"and  b=="rock":
        print("B wins")
    else:
        print ("Invalid input, you have not enetered rock, paper or scissors, try again")
        pass

a = input("enter the elements for rock, paper,scissor: ")
b = input("enter the elements for rock, paper,scissor: ")


#if  __name__ =="__main__":
rock_paper_scissors()


#method -2

import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))
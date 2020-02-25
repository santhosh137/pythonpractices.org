def check():
    n = int(input("Enter the number"))
    if n%2==0:
        print ("The number is Even")
    elif n<0:
        print ("Enter the postive integer")
        check()
    else:
        print ("The number is odd")




if __name__ == "__main__":
    check()

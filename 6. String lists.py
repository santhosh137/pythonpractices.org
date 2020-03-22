user_string =input("Enter a string: ")
print (user_string)

print (user_string[::-1])


if user_string==user_string[::-1]:
    print (user_string +" is a palindrome")
else:
    print (user_string +"  is  not a palindrome ")

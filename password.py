import re

# now we take an input password in a string
password = input("Enter the password you want to check : ")

if len(password) < 8:
    print("The entered password is not of 8 characters : ")

elif not re.search("[A-Z]", password):
    print("The entered password must contain a uppercase letter : ")

elif not re.search("[a-z]", password):
    print("The entered password must contain a lowercase letter : ")

elif not re.search("[0-9]", password):
    print("the password must contain a digit : ")

elif not re.search("[@!#$%^&*]", password):
    print("please use a special character in your password : ")

else:
    print("The password you entered is strong")
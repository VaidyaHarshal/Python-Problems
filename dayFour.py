"""
Question 14:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:
Hello world!

Then, the output should be:
UPPER CASE 1
LOWER CASE 9

"""

def check_case(charList):
    upperCase = 0
    lowerCase = 0

    for i in str(charList):                 # Loop to iterate through each character of the string
        if i.isupper():                     # Checking if the character is upper case character
            upperCase += 1
        elif i.islower():                   # Checking if the character is lower case character
            lowerCase += 1

    print(f"UPPER CASE {upperCase} \nLOWER CASE {lowerCase}")

charList = input("Enter the sentence to check the upper and lower case characters \n")
check_case(charList)


"""

Question 15:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:
9

Then, the output should be:
11106

"""

def compute_value(num):
    comp_val = (int(num) + int(num+num) + int(num+num+num) + int(num+num+num+num))          # Concatenate string and convert into int to perform addition of numbers
    # comp val = (int(num) + int(2*num) + int(3*num) + int(4*num))                          # Alternative method to perform the addition
    return comp_val

num = (input("Enter the number to compute the value \n"))                                   # Take input number from the user to compute the value
val = compute_value(num)
print(val)
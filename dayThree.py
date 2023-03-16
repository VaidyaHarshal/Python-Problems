"""
Question 10:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again

Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.We use set container to remove duplicated data automatically and then use sorted() to sort the data.

"""

input_str = input("Enter the sentence which you want to display \n").split(" ")     # Take input from user and split the sentence using space to store into list
uniq_str = set(input_str)                                                           # Convert the list into set to remove duplicates
print(" ".join(sorted(uniq_str)))                                                   # Print the words alphabetically using sorted method


"""
Question 11:

Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001

Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

def check(x):                           # check function returns true if the decimal value if the binary numbers are divisible by 5
    return int(x, 2) % 5 == 0           # int(x,b) takes x as string and b as base from which it will be converted to decimal

data = input("Enter the binary numbers to be checked \n").split(",")
data = list(filter(check, data))        # in filter(func,object) function, elements are picked from 'data' if found True by 'check' function
print(",".join(data))                   # Printing the binary numbers who decimal values are divisible by 5


"""
Question 12:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""
temp_list = []

for nums in range(1000,3001):               # Loop for the nums in the from 1000-3000
    counter = 0
    for i in str(nums):                     # Converting the number into string in order to iterate through each digit using for loop
        if int(i) % 2 != 0:                 # Checking whether each digit is divisible by 2 after changing the type from string to int again
            counter = 1

    if counter == 0:
        temp_list.append(str(nums))         # Appending the number into a new list if all the digits are divisible by 2

print(",".join(temp_list))                  # Printing the numbers whose all digits are divisible by 2


"""
Question 13:
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:
hello world! 123

Then, the output should be:
LETTERS 10
DIGITS 3

"""

char_count = 0
num_count = 0
input_val = input("Enter the sentence for the word and number count \n")
print(input_val)

for i in str(input_val):
    print(i)
    if i.isalpha():                 # To check if i is alphanumeric or not
        char_count += 1
    elif i.isnumeric():             # To check if i is numeric or not
        num_count += 1

print("LETTERS ", char_count)
print("DIGITS ", num_count)


# Alternative way

letter = 0
digit = 0
input_val = input("Enter the sentence for the word and number count using alternative way \n")

for i in input_val:
    if ('a' <= i and i <= 'z') or ('A' <= i and i <= 'Z'):      # Checking if i is between the ascii values of a-z or A-Z
        letter += 1
    elif ('0' <= i <= '9'):                                     # Checking if i is between the ascii values of 0-9
        digit += 1

print(f"LETTERS {letter} \nDIGITS {digit}")
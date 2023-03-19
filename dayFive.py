"""
Question 16:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9

Then, the output should be:
1,9,25,49,81

"""

def square_odd(numList):
    newList = [str(int(i)**2) for i in numList if int(i) % 2 != 0]              # Checking if i is divisible by 2 and finding squares of all odd numbers
    print(newList)
    return newList

numList = input("Enter a comma seperated sequence of numbers \n").split(",")
final_val = square_odd(numList)
print(",".join(final_val))


"""
Question 17:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.

Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100

Then, the output should be:
500

"""

lst = []
final_amt = 0
while True:
    inputVal = input("Enter the transaction type D for Deposit or W for withdraw and Q for quit \n").lower()
    if inputVal == 'd':
        final_amt += int(input("Enter the amount to be deposited \n"))          # Adding the numbers if the option is Deposit
    if inputVal == 'w':
        withdraw_amt = int(input("Enter the amount to be withdrawn \n"))        
        if final_amt > withdraw_amt:                                            # Checking if withdraw amount exceeds balance
            final_amt -= withdraw_amt                                           # Substracting the number if option is W
        else:
            print("Low Balance")
            break
    if final_amt < 0:
        break
    if inputVal == 'q':
        break
print(final_amt)
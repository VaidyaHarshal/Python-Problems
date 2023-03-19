"""
Question 18:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345

Then, the output of the program should be:
ABd1234@1

"""
def testPass(strList):
    lst = []
    for val in strList:
        smallAlpha = 0
        NumCnt = 0
        CapAplha = 0
        SpecialCnt = 0
        if 6 <= len(val) <= 12:                         # Checking for the length of the password
            print("Password is of right length \n")
        else:
            continue
        for i in str(val):
            if 'a' <= i <= 'z':                         # Checking for small letters in the password
                smallAlpha += 1
            elif '0' <= i <= '9':                       # Checking for numeric characters in the password
                NumCnt += 1
            elif 'A' <= i <= 'Z':                       # Checking for capital letters in the password
                CapAplha += 1
            elif i == '$' or i == '#' or i == '@':      # Checking for special characters in the password
                SpecialCnt += 1  
            else:
                continue
        if smallAlpha >= 1 and NumCnt >= 1 and CapAplha >= 1 and SpecialCnt >= 1:       # Append in the list only if all conditions are met
            lst.append(val)
    return lst
            

passStr = input("Enter the passwords to be tested in a comma seperated way \n").split(",")
lst = testPass(passStr)
print(",".join(lst))


"""
Question:
You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name
2: Then sort based on age
3: Then sort by score
The priority is that name > age > score.

If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85

Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

"""

def sort_tupl(sortedLst, sort_num):
    if sort_num == 1:
        return(sorted(sortedLst, key=lambda x:(x[0])))                          # Using the lambda function to sort the values by considering the first element of tuple
    if sort_num == 2:
        return(sorted(sortedLst, key=lambda x:(x[1])))                          # Using the lambda function to sort the values by considering the second element of tuple
    if sort_num == 3:
        return(sorted(sortedLst, key=lambda x:(x[2])))                          # Using the lambda function to sort the values by considering the third element of tuple
    if sort_num == 4:
        return(sorted(sortedLst, key=lambda x:(x[0], x[1], x[2])))              # Using the lambda function to sort the values by considering all the elements of tuple

lst = []
while True:
    tupl_val = tuple(input("Enter the values for the tuple \n").split(","))
    if not tupl_val[0]:                                                         # Stop when there are no more elements entered by the user
        break
    lst.append(tupl_val)                                                        # Appending the tuple in the list
sort_num = int(input("Enter the number in order to sort the tuple 1:Sort based on name/2:Then sort based on age/3:Then sort by score/4: Then sort by all values \n"))
sortedLst = sort_tupl(lst, sort_num)
print(sortedLst)

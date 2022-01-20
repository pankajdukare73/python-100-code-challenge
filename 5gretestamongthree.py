#fined greatest among three number
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if num1>num2:
    if num1>num3:
        print("The number",num1,"is greater than",num2,"and",num3)
    else:
        print("The number",num3,"is greater than",num1,"and",num2)
elif num2>num3:
    print("The number",num2,"is greater than",num1,"and",num3)
else:
    print("The number",num3,"is greater than",num1,"and",num2)

"""
Author:pankaj dukare
Output:
    Enter the first number:78
    Enter the second number:45
    Enter the third number:56
    The number 78 is greater than 45 and 56

    Enter the first number:23
    Enter the second number:98
    Enter the third number:34
    The number 98 is greater than 23 and 34

    Enter the first number:34
    Enter the second number:67
    Enter the third number:89
    The number 89 is greater than 34 and 67
"""
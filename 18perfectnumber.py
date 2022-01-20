#check the number is perfect of not
#perfect number is sum of divisor is same as number ex.6
num=int(input("Enter number to check number is Perfect or not:"))
perfect=0
for i in range(1,num):
    if num%i==0:
        perfect=perfect+i
if num==perfect:
    print("The number",num,"is Perfect number.")
else:
    print("The number",num,"is not perfect number.")

"""
Author:pankaj dukare
Output:
    Enter number to check number is Perfect or not:6
    The number 6 is Perfect number.

    Enter number to check number is Perfect or not:10
    The number 10 is not perfect number.
"""
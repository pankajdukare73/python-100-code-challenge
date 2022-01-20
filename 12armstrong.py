#Check the number is armstrong or not
#if addition of cube of each digit of number is same as number then number is armstrong
num=int(input("Enter number to check number is armstrong or not:"))
temp=num
arm=0
while(num>0):
    digit=num%10
    arm=arm+digit**3
    num//=10
if arm==temp:
    print("The number",temp,"is Armstrong.")
else:
    print("The number",temp,"is not Armstrong.")

"""
Author:pankaj dukare
Output:
    Enter number to check number is armstrong or not:153
    The number 153 is Armstrong.

    Enter number to check number is armstrong or not:121
    The number 121 is not Armstrong.
"""
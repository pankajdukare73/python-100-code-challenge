# Enter the number to check it strong or not
#strong  number is sum of digit factorial is same as number ex.145
num=int(input("Enter number to check number is Strong or not:"))
temp=num
fact=1
strong=0
while(num>0):
    digit=num%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    strong=strong+fact
    num//=10
if strong==temp:
    print("The number",temp,"is strong number.")
else:
    print("The number",temp,"is not strong number.")

"""
Author:pankaj dukare
Output:
    Enter number to check number is Strong or not:145
    The number 145 is strong number.

    Enter number to check number is Strong or not:562
    The number 562 is not strong number.
"""
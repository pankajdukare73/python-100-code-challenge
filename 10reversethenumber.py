#reverse the given number
num=int(input("Enter number to reverse to it:"))
temp=num
rev=0
while(num>0):
    digit=num%10
    rev=rev*10+digit
    num//=10
print("The reverse number of",temp,"is",rev)

"""
Author:pankaj dukare
Output:
    Enter number to reverse to it:472
    The reverse number of 472 is 274
"""
#fined the sum of digit of number
num=int(input("Enter the number to fined sum of its digit:"))
digitsum=0
temp=num
while(num>0):
    digit=num%10
    digitsum+=digit
    num=num//10
print("The sum of digit of number",temp,"is",digitsum)

"""
Author:pankaj dukare
Output:
    Enter the number to fined sum of its digit:593
    The sum of digit of number 593 is 17
"""
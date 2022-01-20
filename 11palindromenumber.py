#check the number is palindrome or not
#polindrome means reverse number and orginal number are same
num=int(input("Enter number to check it palindrome or not:"))
temp=num
rev=0
while(num>0):
    digit=num%10
    rev=rev*10+digit
    num//=10
if rev==temp:
    print("The number",temp,"is palindrome.")
else:
    print("The number",temp,"is not palindrome.")

"""
Author:pankaj dukare
Output:
    Enter number to check it palindrome or not:121
    The number 121 is palindrome.
    
    Enter number to check it palindrome or not:786
    The number 786 is not palindrome.
"""
#fined the harshad number of given number
#harshad number is division of num and sum of is digit
num=int(input("Enter the number to fined its harshad number:"))
temp=num
digit_sum=0
while(num>0):
    digit=num%10
    digit_sum+=digit
    num//=10
harshadno=temp//digit_sum
print("The harshad number of {0} is {1}".format(temp,harshadno))

"""
Author:pankaj dukare
Output:
    Enter the number to fined its harshad number:153
    The harshad number of 153 is 17
"""
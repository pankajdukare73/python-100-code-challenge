#sum of first N natural number
N=int(input("Enter the Nth number to fined sum of them:"))
sum=0
for i in range(1,N+1):
    sum+=i
print("The sum of first",N,"th natural number is",sum)

'''
Author:Pankaj Dukare
Output:
    Enter the Nth number to fined sum of them:100
    The sum of first 100 th natural number is 5050
'''

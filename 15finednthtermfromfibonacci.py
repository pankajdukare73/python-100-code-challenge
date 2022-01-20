# fined nth term of fibonacci series
n=int(input("Enter the Nth term of fibonacci series you want to fined:"))
n1=0
n2=1
prev=0
for i in range(0,n-1):
    prev=n1
    n1=prev+n2
    n2=prev
print(f"the {n} th term of fibonacci series is {n1}")

"""
Author:pankaj dukare
Output:
    Enter the Nth term of fibonacci series you want to fined:10
    the 10 th term of fibonacci series is 34
"""
#fined the fibonacci series upto n
n=int(input("Enter the Number of term fibonacci series fined:"))
n1=0
n2=1
prev=0
for i in range(0,n):
    print(n1,end=" ")
    prev=n1
    n1=prev+n2
    n2=prev

"""
Author:pankaj dukare
Output:
    Enter the Number of term fibonacci series fined:10
    0 1 1 2 3 5 8 13 21 34
"""
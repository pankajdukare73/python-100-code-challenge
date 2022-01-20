#fined prime number between the range
start=int(input("Enter the starting number from you fined prime number:"))
end=int(input("Enter the ending number upto you fined prime number:"))
flag=0
count=0
for i in range(start,end+1):
    if(i==1):
        continue
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if flag==0:
        count+=1
        print(i,end=" ")
print("\nThe total number of prime number between",start,"to",end,"are",count)
"""
Author:pankaj dukare
Output:
    Enter the starting number from you fined prime number:1
    Enter the ending number upto you fined prime number:50
    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 
    The total number of prime number between 1 to 50 are 15
"""
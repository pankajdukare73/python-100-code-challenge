#check the year is leap or not
year=int(input("Enter the year to check this is leap or not:"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("The year",year,"is leap year")
        else:
            print("The year",year,"is not leap year")
    elif year%4==0:
        print("The year",year,"is leap year")
    else:
        print("The year",year,"is not leap year")
else:
    print("The year",year,"is not leap year")

"""
Author:pankaj dukare
Output:
    Enter the year to check this is leap or not:2000
    The year 2000 is leap year

    Enter the year to check this is leap or not:2100
    The year 2100 is not leap year

    Enter the year to check this is leap or not:2004
    The year 2004 is leap year

    Enter the year to check this is leap or not:2005
    The year 2005 is not leap year
"""
   
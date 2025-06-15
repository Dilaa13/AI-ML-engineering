no1 = int(input("Enter number 1: "))
no2 = int(input("Enter number 2: "))
no3 = int(input("Enter number 3: "))

if (no1> no2) & (no1> no3):
    print("The Maximum value is: ", no1)
    if(no2>no3):
        print("The minimum value is: ",no3)
    else:
        print("The minimum value is: ",no2)
    

if (no2> no1) & (no2> no3):
    print("The Maximum value is: ", no2)
    if(no1>no3):
        print("The minimum value is: ",no3)
    else:
        print("The minimum value is: ",no1)

if (no3> no2) & (no3> no1):
    print("The Maximum value is: ", no3)
    if(no2>no1):
        print("The minimum value is: ",no1)
    else:
        print("The minimum value is: ",no2)

print(" \n")

maximum = max(no1 , no2 , no3)
minimum = min(no1 , no2 , no3)

print("The maximum value is: ",maximum)
print("The minimum value is: ",minimum)


    

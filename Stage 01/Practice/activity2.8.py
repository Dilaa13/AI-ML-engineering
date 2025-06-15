n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

def avg(n1,n2,n3):
    total = n1+n2+n3
    avrg = total/3
    return avrg

result = avg(n1,n2,n3)

print("The average of entered 3 values is: ", result)

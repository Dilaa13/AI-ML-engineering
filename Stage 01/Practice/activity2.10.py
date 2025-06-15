n = int(input("Enter a number: "))

def fact(n):
    fac = 1
    while n>=1:
        fac = fac*n
        n = n-1
    return fac

result = fact(n)

print("The factorial of the entered number is : ", result)

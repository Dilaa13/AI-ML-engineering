total = 0

while True:
    number = int(input("Enter a number: "))
    if number == -999:
        break
    total = total + number

print("The summation of entered values : ", total)
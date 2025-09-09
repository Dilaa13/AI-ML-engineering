x = ["Temple" , "13" , "True" , "45.69" , True]
print(x)
print(x[0])
print(type(x))

x[0] = "Bottle"

print(x)

y = ("Temple" , "13" , "45.32" , False)
print(y)
print(y[2])
print(type(y))

#y[0] = "bottle"

i = 0
while i < len(x):
    print(x[i])
    i = i+1

print("---------------------------------")

for i in range(len(x)):
    print(x[i])

print("---------------------------------")

print(x[0:3])
print(x[1:3])


i = 1
marks = []

for i in range(10):
    mark = float(input(f"Enter the marks of student {i+1} : "))
    marks.append(mark)

min_mark = min(marks)
max_mark = max(marks)
avg_mark = sum(marks)/len(marks)

print("\n Results\n")
print("The minimum mark of class is : ", min_mark)
print("The maximum mark of class is : ", max_mark)
print("The average mark of class is : ", avg_mark)
    

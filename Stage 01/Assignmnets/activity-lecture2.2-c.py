i = 0

def grade(mark):
    if mark>75:
        return "A"
    elif mark>=65 and mark <= 75:
        return "B"
    elif mark>=55 and mark<65:
        return "C"
    elif mark>=45 and mark<55:
        return "S"
    else:
        return "W"

for i in range(5):
    mark = int(input(f"Enter the marks of subject {i+1} : "))
    result = grade(mark)
    print(f"Grade of the subject {i+1}: ", result)


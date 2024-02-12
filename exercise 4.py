maths = int(input("math: "))
english = int(input("enlish: "))
chem = int(input("chem: "))
bio = int(input("bio: "))
computer = int(input("computer: "))

total = maths+english+chem+bio+computer
print(total)
average = total/5
print(average)
if average >= 0 and average <= 39:
    print("E")
if average >= 40 and average <= 50:
    print("D")
if average >= 51 and average <= 60:
    print("C")
if average >= 61 and average <= 70:
    print("B")
elif average >= 71 and average <= 100:
    print("A")
else:
    print("invalid")
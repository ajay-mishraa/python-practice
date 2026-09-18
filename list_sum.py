# DAY 12

numbers =list(map(int,input("Enter numbers separeted by space: ").split()))

total = 0

for number in numbers:
    total += number
    
print("List:", numbers)
print("sum =",total)    
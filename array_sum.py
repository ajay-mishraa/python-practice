# Day 14: Find Sum of Array Elements

numbers = list(map(int, input("Enter numbers: ").split()))

total = 0

for num in numbers:
    total += num

print("Sum:", total)
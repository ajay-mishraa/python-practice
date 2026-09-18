# DAY 13

# Find Maximum and Minimum in an Array

numbers = list(map(int, input("Enter numbers: ").split()))

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

print("Maximum:", maximum)
print("Minimum:", minimum)
# Day 15: Add Array Insertion Program

numbers = list(map(int, input("Enter array elements: ").split()))

position = int(input("Enter position to insert: "))
value = int(input("Enter value: "))

numbers.insert(position, value)

print("Array after insertion:", numbers)
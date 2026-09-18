# Day 16: Add Array Deletion Program

numbers = list(map(int, input("Enter array elements: ").split()))

position = int(input("Enter position to delete: "))

if 0 <= position < len(numbers):
    deleted = numbers.pop(position)

    print("Deleted element:", deleted)
    print("Array after deletion:", numbers)
else:
    print("Invalid position")
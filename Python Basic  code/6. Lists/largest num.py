# Find largest number in list.

numbers = [10, 20, 5, 34, 29]

largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("Largest number is: ", largest)


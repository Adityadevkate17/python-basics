    # Count digits in a number

n = int(input("Enter a number:"))

count = 0

while n > 1:  
     n = n // 10
     count += 1

print("Number of digits:", count)


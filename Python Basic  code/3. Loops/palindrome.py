# Check palindrome number

n = int(input("Enter a number:"))

reverse = 0
temp = n

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
 
if temp == reverse:
    print ("It is palindrome")
else:
    print ("It is not palindrome")
    
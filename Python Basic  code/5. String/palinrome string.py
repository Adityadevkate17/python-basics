# Check string is palindrome or not.
str = input("Enter a string:")

reverse = str[::-1]   #[start(beginning) : stop(end) : step(-1)] # slicing 

if str ==  reverse:
    print("IT is palindrome")
else:
    print("It is not palidrome")
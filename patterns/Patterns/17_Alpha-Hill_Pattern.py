#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA
 
n = int(input("Enter size: "))

for i in range(1, n + 1):
    ch = 'A'

    # spaces
    for j in range(1, n - i + 1):
        print(" ", end="")

    # increasing
    for j in range(1, i + 1):
        print(ch, end="")
        ch = chr(ord(ch) + 1)

    # decreasing
    ch = chr(ord('A') + i - 2)

    for j in range(1, i):
        print(ch, end="")
        ch = chr(ord(ch) - 1)

    print()
    
      

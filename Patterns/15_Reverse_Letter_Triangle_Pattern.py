# ABCDE
# ABCD
# ABC
# AB
# A

str = input("Enter size:")

for i in range(n, 0, -1):
    ch = 'A'

    for j in range(i):
        print(ch, end="")
        ch = chr(ord(ch) + 1) ## Move to next alphabet (A→B, B→C, ...)

    print()

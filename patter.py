def pattern(n):
    for i in range(n):
        for j in range (i+1):
            print("*", end=" ")
        print()

def print_pattern(n):
    for i in range(n):
        s = ''
        for j in range(i+1):
            s = s + '*'
        print(s)

n = int(input("Enter the no of row want to print"))
pattern(n)
print_pattern(n)

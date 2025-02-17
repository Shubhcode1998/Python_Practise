def func():
    t = int(input())
    for i in range(t):
        a1 , b1 = input().split()
        a = int(a1)
        b = int(b1)
        if (a < b):
            print(a, end=" ")
            print(b)
        else:
            print(b, end=" ")
            print(a)
        print()

def main():
    func()

if __name__ == "__main__":
    main()
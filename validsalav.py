def func():
    t = int(input())
    for i in range(t):
        a, b = 0, 0
        x = input()
        l = len(x)
        for j in range(l):
            if x[j] == 'A':
                a += 1
            elif x[j] == 'B':
                b += 1
        if a > b:
            print("A")
        elif a < b:
            print("B")


def main():
    func()

if __name__ == "__main__":
    main()
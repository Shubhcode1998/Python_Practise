
def func():
    t = int(input())
    for i in range (t) :
        x,y,z = input().split()
        a = int(x)
        b = int(y)
        c = int(z)
        if(a < b & b < c):
            print("STAIR")
        elif (a < b & b > c):
            print("PEAK")
        else:
            print("NONE")



def main():
    func()

if __name__ == "__main__":
    main()
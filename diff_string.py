
def func():
    t = int(input())
    for i in range(t):
        str1 = input()
        l = len(str1)
        f = 0
        for j in range(1,l):
            if(str1[0] != str1[j]):
                print("YES")
                print(str1[l//2:] + str1[:l//2]) # use // for integer division
                f =1
                break
        if f == 0 :
            print("NO") # capitalize the 'N'

def main():
    func()

if __name__ == "__main__":
    main()



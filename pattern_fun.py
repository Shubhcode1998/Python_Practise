def pattern(n):
        for i in range(1,n+1):
                s = ''
                for j in range(1,i+1):
                        s = s + '*'
                print(s)
		
    


n = int(input("enter no of rows"))
pattern(n)

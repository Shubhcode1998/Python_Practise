def area(l,b,o):
	if o == 1:
		return (l*b)/2
	elif o == 2 :
		return (l*b)
	else :
		return 0


o = int(input("typr of shape 1 for triangle , 2 for rectagle , other for none of shape"))
l = float(input("length of shape"))
b = float(input("bredth of shape"))

ans = area(l,b,o)
print("area of shape provided is ",ans)

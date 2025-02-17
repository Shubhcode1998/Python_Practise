import math


def circle(r):
	area = 2 * math.pi*(r**2)
	circum = 2 * math.pi*r
	dia = 2*r
	return area,circum,dia


if __name__ =="__main__":
	r = input("Enter the radius")
	r = float(r);
	area , circum,dia = circle(r)
	print(f" area {area}, cirumference {circum}, diametre {dia}")


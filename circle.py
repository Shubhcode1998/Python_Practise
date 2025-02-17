def circle_cal():
    r = input("enter the radius of circle ")
    r = float(r)
    area = 2 * 3.14 * r * r
    print(f"area of circle {round(area,2)}")
    circumference = 2 * 3.14 * r 
    print(f"area of circle {round(circumference,2)}")
    diametre = 2 * r 
    print(f"area of circle {round(diametre,2)}")


def main():
    circle_cal()


if __name__ == "__main__":
    main()



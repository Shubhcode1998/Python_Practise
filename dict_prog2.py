import statistics


stocks = {
	"rel":[120,132,124],
	"mil":[234,453]
    
}

def print_all():
        for s,p in stocks.items():
                avg = statistics.mean(p)
                print(f"{s} ==> {p} ==> avg:",round(avg,2))


def add():
	s = input("enter a stock ticker to add:")
	p = input("enter price of this stock:")
	p = float(p)
	if s in stocks:
		stocks[s].append(p)
	else:
		stocks[s] = [p]
	print_all()


def main():
    op=input("Enter operation (print, add or amend):")
    if op.lower() == 'print':
        print_all()
    elif op.lower() == 'add':
        add()
    else:
        print("Unsupported operation:",op)

if __name__ == '__main__':
    main()

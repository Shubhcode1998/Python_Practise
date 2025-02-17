import statistics

stocks = {
    'info' : [600,630,620],
    'rel' :[1430,1490,1567],
    'mtl' : [234,180,160]
}

def print_all():
    for stock, p in stocks.items():
        a = statistics.mean(map(float, p))
        print(f"{stock}==>{p}==>avg: {round(a, 2)}")

def add():
    s1 = input("Enter the name of stock ")
    s1 = s1.lower()
    p = input("Enter the price of stock ")
    p=float(p)
    if s1 in stocks :
        stocks[s1].append(p)
    else:
        stocks[s1] = [p]

    print_all()

def main():
    s = input("enter the choice from given print ,add ")
    s = s.lower()
    if s == 'print':
        print_all()
    elif s == 'add':
        add()

if __name__ == "__main__" :
    main()

with open("/Users/shubhammandal/Documents/python_practise/stocks.csv","r") as f , open("/Users/shubhammandal/Documents/python_practise/output.csv","w") as out:
    out.write("company Name, PE ratio,PB ration\n")
    next(f)
    for line in f:
        tokens = line.split(",")
        stocks = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])
        pe = round(price/eps,2)
        pb = round(price/book,2)
        out.write(f"{stocks},{pe},{pb}\n")

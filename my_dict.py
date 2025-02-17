population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}


def print_all():
    for country , p in population.items():
        print(f"{country}==>{p}")

def add():
    s1 = input("Enter the name of country ")
    s1 = s1.lower()
    if s1 in population :
        print("country already exist in ")
        return
    p1 = input("Enter the population ")
    p1 = float(p1)
    population[s1] = p1
    print_all()

def remove():
    s1 = input("Enter the country to be removed ")
    s1 = s1.lower()
    if s1 not in population :
        print("country does not exist")
        return
    del population[s1]
    print_all()

def query():
    s1 = input("Enter the country ")
    s1 = s1.lower()
    if s1 not in population :
        print("country does not exist")
        return
    print(f"{s1} population is {population[s1]}")
    


def main():
    s = input("enter the choice from given print ,add , remove , query")
    s = s.lower()
    if s == 'print':
        print_all()
    elif s == 'add':
        add()
    elif s == 'remove':
        remove()
    else :
        query()


if __name__ == "__main__" :
    main()

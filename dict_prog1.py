


population = {
	"india" : 143,
	"chna" : 144,
	"pakistan" : 45,
	"usa" : 121
}

def add():
	country = input("enter the country name")
	country = country.lower()
	if country in population:
		print("already exist in database")
		return
	
	pop = float(input("enter the population"))
	population[country] = pop
	print_all()


def remove():
	country = input("enter the country name to remove")
	country = country.lower()
	if country not in population:
		print("does not exist in database")
		return
	
	del population[country]
	print_all()


def query():
	country = input("enter the country name to remove")
	country = country.lower()
	if country not in population:
		print("does not exist in database")
		return
	
	print("Population of {country} is {population[country]} crore ")
	

def print_all():
	for country,p in population.items():
		print(f"{country}==>{p}")


print("enter the choice print , add , remove , query")

opt = input();

if(opt == 'print'):
	print_all()
elif (opt == 'add'):
	add()
elif(opt == 'remove'):
	remove()
elif(opt == 'query'):
	query()

class AdultException(Exception):
    pass

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_minor(self,age):
        if age >= 18 :
            raise AdultException
        else:
            return age

    def display(self):
        try:
            print(f"age-->{self.get_minor(self.age)}")
        except AdultException:
            print("Person is an adult")
        finally:
            print(f"Person name is {self.name}")

person("Bhavin",17).display()

person("Kartik",34).display()
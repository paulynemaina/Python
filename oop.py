# object-oriented programming

# class Person:
#     def __init__(self):
#        self.name = "Ezra"
#        self.age = 89
#        self .course = "Mit"
#
#
#
#
# person = Person()
# person.name = "Paulyne"
#
# print(person.name)
# print(person.age

# new
class People:
    def __init__(self, name, county, country):
        self.name = name
        self.county = county
        self.country = country
person1 = People(name="wairimu", county="meru", country="kenya")
person2 = People(name="collo", county="kajiado", country="kenya")

print(f"my name is {person1.name} from {person1.county} in {person1.country}")
print(f" I'm {person2.name} from {person2.county} in {person2.country}")
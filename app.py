# import student class from new
from new import Student

# inherit student class and print its properties


class Person(Student):
    pass


print(Person.name, Person.age, Person.gender)

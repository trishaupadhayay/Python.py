# # single inheritance

# class Animal():
#     def property(self):
#         print("Animal has 4 legs")


# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# d=Dog()       

# d.property()
# d.bark()


# Multiple inheritance
# class Father():
#     def skill1(self):
#         print("Driving")
# class Mother():
#     def skill2(self):
#         print("Coking")
# class Child(Father,Mother):
#     def Qualities(self):
#         print("Inherited skills form parents:")

# x=Child()
# x.Qualities()
# x.skill1()
# x.skill2()

# Multilevel inheritance

class Grandfather:
    def house(self):
        print("Grandfather's House")


class Father(Grandfather):
    def bike(self):
        print("Father's Bike")


class Son(Grandfather):
    def laptop(self):
        print("Son's Laptop")


class Grandson(Father, Son):
    def car(self):
        print("Grandson's Car")


# Son object
s = Son()
s.house()
s.laptop()

# Grandson object
g = Grandson()
g.house()
g.bike()
g.laptop()
g.car()




# hierarchical inheritance

# class Institute():
#     def name(self):
#         print("NSTIW Allahabad")

# class Teacher(Institute):
#     pass
# class Student(Institute):
#     pass
# class Housekeeping(Institute):
#     pass

# t=Teacher()
# s=Student()
# h=Housekeeping()

# s.name()
# t.name()
# h.name()





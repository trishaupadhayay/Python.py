class aipa :
    def __int__(self,name,roll_no,trade ,marks): #contructor
        self.name=name
        self.roll_no=roll_no
        self.trade=trade
        self.marks=marks

std1=aipa("Trisha",1,"AIPA",75)
std2=aipa("Aditi",2,"Aipa",85)



print(std1.name)
print(std1.roll_no)
print(std1.trade)
print(std1.marks)

print(std2.name)
print(std2.roll_no) 
print(std2.trade)
print(std2.marks)



class student:
    def __init__(self,name,roll_no,trade ,marks): #contructor
        self.name=name
        self.roll_no=roll_no
        self.trade=trade
        self.marks=marks

    def display_details(self):
        print("Name:",self.name)
        print("Roll No:",self.roll_no)
        print("Trande:",self.trade)
        print("Marks:",self.marks)

    def check_result(self):
        if self.marks >=40:
            print("Pass")
        else:
            print("Fail")

    def percentage(self,total_marks):
        return (self.marks/total_marks)*100



students1=student("Aditi",1,"AIPA",75)
students2=student("Renu",2,"AIPA",85)

students1.display_details()
students1.check_result()
print(students1.percentage(100),"%")
students2.display_details()
students2.check_result()
print(students2.percentage(100),"%")














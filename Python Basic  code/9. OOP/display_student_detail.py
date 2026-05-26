# Create method to display student details.

class student:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_details(self):
        print("name:", self.name)
        print("age:", self.age)
        print("grade:", self.grade)

student = student("Ronny" , 20 , "A")
student.display_details()


        
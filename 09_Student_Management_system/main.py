class Student:


    num_students = 0

    def __init__(self, name, roll):
        self.name= name
        self.roll = roll 
        Student.num_students += 1


student1 = Student("Patrick", 1)
student2 = Student("Rocky", 2)
student3 = Student("Rakesh", 3)
student4 = Student("Ravi", 4)

class StudentManagementSystem:
    
    def __init__(self,):
        self.students = []


    def add_student(self, student):
        self.students.append(student)
        print(student.name, "added successfully")


    def remove_student(self, roll):
        for student in self.students:
            if student.roll == roll:
                self.students.remove(student)
                print(student.name,"removed successfully")
                return 
        print("Student not found")     

    
    def display_name(self):
        for student in self.students:
            print(student.name)

    def search_students(self, roll):
        for student in self.students:
            if student.roll == roll:
                print("Name:", student.name)
                print("Roll:", student.roll)
                return
        print("Student not found")


    def update_student_name(self, roll, new_name):
        for student in self.students:
            if student.roll == roll:
               student.name = new_name
               print(student.name, "Name updated sucessfully")
               return

        print("Student not found")    



sms = StudentManagementSystem()

sms.add_student(student1)
sms.add_student(student2)
sms.add_student(student3)
sms.add_student(student4)
sms.remove_student(3)

sms.display_name()
sms.search_students(99)
sms.update_student_name(99, "Patrick")

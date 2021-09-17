from os import name


class Person:
    name
    id

    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

    def self_Introduce(self):
        print("My name is " + self.name + " my ID is " + str(self.id))


class Student(Person):
    def __init__(self, name, id, school) -> None:
        super().__init__(name, id)
        self.school = school

    def self_Introduce(self):
        super().self_Introduce()
        print("I am studying at UTE")

    def study(self):
        print("Student is studying!")


student = Student('Dat', 1, 'UTE')
student.self_Introduce()
student.study()
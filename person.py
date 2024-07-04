class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print("Name: ", self.name, "age: ",self.age, "Gender: ", self.gender)
    
obj = Person(name="Aster" ,age=21 ,gender="Male")
obj.introduce()

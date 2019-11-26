# class Shark():
#     def __init__(self,name):
#         self.name = name
#         print("This is the constructor method.")
#
#     def swim(self):
#         print(self.name + ' is swimming')
#
#     def be_awesome(self):
#         print(self.name + " is being awesome")
#
#
# def main():
#     a = Shark('sass')
#     a.swim()
#     a.be_awesome()
#
#
# if __name__ == "__main__":
#     main()

# class Sample:                         ## Class Level Variable
#     animal_type = 'rabbit'
#     location = "ocean"
#     followers = 5
#
#
# obj = Sample()
# print(obj.animal_type)
# print(obj.location)
# print(obj.followers)


class Shark:                            ## instance variable
    def __init__(self, name, age):
        self.name = name
        self.age = age


new_shark = Shark("Sammy", 5)
print(new_shark.name)
print(new_shark.age)
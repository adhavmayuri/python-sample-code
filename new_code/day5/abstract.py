class Person:
    def __init__(self):
        self.name = "Jack Matte"

    def bio(self):
        self.addr = "Bakers street, London"
        self.taxInfo = "HUAPK29971"
        self.contact = "01-777-523-342"
        print(self.addr, self.taxInfo, self.contact)

    def interest(self):
        self.favFood = "Chinese"
        self.hobbies = "Python Programming"
        self.bloodGroup = "A+"
        print(self.favFood, self.hobbies, self.bloodGroup)

obj = Person()
print(obj.name)
obj.bio()
obj.interest()
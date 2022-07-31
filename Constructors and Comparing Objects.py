
class computer:

    def __init__(self):
        self.name = "Naveen"
        self.age = 20


    def update(self):
        self.age = 30

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = computer()
c1.age =  30
c2 = computer()

if c1.compare(c2):
    print("They are the same")
else:
    print("They are different")

c1.name = "Rashi"
c1.age = 12
c1.update()

print(c1.name)
print(c2.name)



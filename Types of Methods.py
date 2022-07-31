class student:

    school = "Telusko"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class...in abc module")


s1 = student(82, 30, 40)
s2 = student(89, 10, 12)

print(student.getschool())
print(s1.avg())
print(s2.avg())
student.info()


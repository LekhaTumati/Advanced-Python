class a:
    def feature1(self):
        print("Feature1 working")

    def feature2(self):
        print("Feature2 working")

class b(a):
    def feature3(self):
        print("Feature3 working")

    def feature4(self):
        print("Feature4 working")

class c(b):
    def feature5(self):
        print("Feature5 working")


a1 = a()
b1 = b()
c1= c()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
c1.feature5()
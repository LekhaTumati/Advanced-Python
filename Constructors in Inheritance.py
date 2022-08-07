class a:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature1A working")

    def feature2(self):
        print("Feature2 working")

class b():

    def __init__(self):
        print("in B init")

    def feature1(self):
        print("Feature1B working")

    def feature4(self):
        print("Feature4 working")

class c(a,b):
    def __init__(self):
        super().__init__()
        print("in C init")


    def feat(self):
        super().feature2()

a1 = c()
a1.feature1()



class a:
    def show(self):
        print("in A Show")

class b(a):

    def show(self):
        print("in B show")


a1 = b()
a1.show()
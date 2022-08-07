

class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class laptop:

    def code(self, ide):
        ide.execute()

ide = MyEditor()

lap1 = laptop()
lap1.code(ide)
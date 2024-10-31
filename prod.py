class test:

    def __init__(self):
        print("constructor")

    def test1(self):
        print("print test1")

    def test2(self):
            print("child method")
    class test2:
        def __init__(self):
            print("constructor child")
        def demo(self):
            print("demo")

class child(test):
    def __init__(self):
        print("second constructor")
    def show(self):
        print("show method")


t= test()
t.test1()
t.test2()
t1=t.test2()
t1.demo()
c=child()
c.show()
c.test1()


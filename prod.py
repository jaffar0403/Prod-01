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


t= test()
t.test1()
t.test2()
t1=t.test2()
t1.demo()


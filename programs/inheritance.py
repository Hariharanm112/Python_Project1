class inheritance:
    def a (self):
      print("parent")
class b(inheritance):
    def b (self):
        print("B")
class c(b):
    def c (self):
        print("c")
m=c()

m.c()
m.b()
m.a()
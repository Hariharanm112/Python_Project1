class encapsulation:
    def __init__(self,name,age):
        self.name = name
        self._age = age
        self.__salary=100

    def show(self):
        return self.__salary
p=encapsulation("hari",20)
print(p.show())
print(p._age)
print(p.name)
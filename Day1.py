class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is" + self.name + "," + self.age)
    
    p1 = person("Bill",63)
    p1.myfunc()
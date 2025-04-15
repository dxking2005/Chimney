class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        # 添加空格以美化输出格式
        print(f"Hello my name is {self.name}, {self.age}")

# 在类定义完成后进行实例化
p1 = Person("Bill", 63)
p1.myfunc()
class Thing:
    def __init__(self, name: str):
        self.name: str = name

class Thing1(Thing):
    def __init__(self, name: str, age: int):
        self.age: int = age
        super().__init__(name=name)

class Thing2(Thing):
    def __init__(self, name: str, age: int):
        self.age: int = age
        super().__init__(name=name)


def create_object(obj, name, age):
    return obj(name=name, age=age)


if __name__ == "__main__":
    hector = create_object(Thing1, name = "Hector", age = 22)
    helena = create_object(Thing2, name = "Helena", age = 26)

    print(type(hector))
    print(type(helena))
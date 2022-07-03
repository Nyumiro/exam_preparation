global_id = 0


class Fruit:
    def __init__(self, name, cost, color, weight):
        self.name = name
        self._cost = cost
        self._color = color
        self.__weight = weight
        self.__id = self.__create_id()

    def __repr__(self):
        return 'id:' + str(self.__id) + ', ' + str(self._cost) + ', ' + self._color + ', ' + str(self.__weight)

    def __create_id(self):
        global global_id
        global_id += 1
        return global_id


class Apple(Fruit):
    def __init__(self, name, cost, color, weight):
        super().__init__(name, cost, color, weight)


class Orange(Fruit):
    def __init__(self, name, cost, color, weight):
        super().__init__(name, cost, color, weight)


class Banana(Fruit):
    def __init__(self, name, cost, color, weight):
        super().__init__(name, cost, color, weight)


basket = [Banana('banana', 10, 'red', 1), Banana('banana', 10, 'yellow', 1)]

for i in basket:
    print(i._color)
    print(i.__weight)
    print(i)

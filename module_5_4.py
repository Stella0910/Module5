class House:
    
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history += [args[0]]
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor in range(1, self.number_of_floors + 1):
            for i in range(1, self.new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)

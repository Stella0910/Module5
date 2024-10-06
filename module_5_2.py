class House:
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


elbrus = House('ЖК Эльбрус', 10)
akacia = House('ЖК Акация', 20)

print(elbrus.__str__())
print(akacia.__str__())
print(elbrus.__len__())
print(akacia.__len__())

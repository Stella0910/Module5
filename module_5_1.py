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


# elbrus = House('ЖК Эльбрус', 30)
# elbrus.go_to(18)


gorsky = House('ЖК Горский', 18)
gorsky.go_to(5)

domik_v_derevne = House('Домик в деревне', 2)
domik_v_derevne.go_to(10)

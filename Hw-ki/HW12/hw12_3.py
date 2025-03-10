"""3. Класс «Автобус». Класс содержит свойства:
● скорость speed
● максимальное количество посадочных мест max_number
● максимальная скорость max_speed
● список фамилий пассажиров  list_names
● флаг наличия свободных мест available_seats
● словарь мест в автобусе dict_seats
Методы:
● посадка и высадка одного или нескольких пассажиров
● увеличение и уменьшение скорости на заданное значение
● операции in, += и -= (посадка и высадка пассажира по
фамилии)"""


class Bus:
    max_number = 5
    max_speed = 90
    list_names = []
    available_seats = True
    dict_seats = {}

    def __init__(self, speed):
        self.speed = speed


    def func_available_seats(self):  # не получилось реализовать проверку на места
        if len(self.list_names) <= self.max_number:
            self.available_seats = True
        else:
            self.available_seats = False


    def in_out(self, in_out, person):
        if in_out == "in":
            self.list_names.append(person)
        if in_out == "out":
            self.list_names.remove(person)


    def __add__(self, other):
        if other > 0 and (other + self.speed) <= self.max_speed:
            print("Увеличение скорости")
            return self.speed + other
        elif other < 0 and (self.speed + other) > 0:
            print("Уменьшение скорости")
            return self.speed + other
        elif other == 0:
            print("Скорость не меняется")
            return self.speed
        else:
            print("Скорость изменить нельзя")


    def dictionary_seats(self):
        for key in range(self.max_number):
            self.dict_seats[key + 1] = ""
        for n in range(len(self.list_names)):
           self.dict_seats[n+1] = self.list_names[n]
        print(self.dict_seats)


    def exit_bus(self, name):
        if name in self.list_names:
            self.list_names.remove(name)
            print(self.list_names)
        else:
            print("Спец.органы дезинформированы. Такого человека нет в автобусе")


    def entrance_bus(self, name):
        self.list_names.append(name)
        print(self.list_names)


bus = Bus(60)
person1 = "Ivanov"
bus.in_out("in", person1)

person2 = "Petrov"
bus.in_out("in", person2)
person3 = "Smith"
bus.in_out("in", person3)
person4 = "Too"
bus.in_out("in", person4)
bus.dictionary_seats()
print(bus.list_names)


print("Smith вышел:")
bus.in_out("out", person3)
print(bus.list_names)
bus.dictionary_seats()


print("Too вышел:")
bus.in_out("out", "Too")
print(bus.list_names)
bus.dictionary_seats()


print("Много людей зашло")
bus.in_out("in", "Кукушкин")
bus.in_out("in", "Зайцев")
bus.in_out("in", "Восьмеркин")
bus.in_out("in", "Круз")
bus.dictionary_seats()
print(bus.list_names)


print("По требованию спец.органов Зайцев должен покинуть автобус")
bus.exit_bus("Зайцев")
print("По требованию спец.органов Сидоров должен покинуть автобус")
bus.exit_bus("Сидоров")
print(bus.list_names)


print("Сидоров зашел в автобус на следующей остановке")
bus.entrance_bus("Сидоров")
bus.dictionary_seats()



print(bus + 40)
print(bus + (-20))
print(bus + 0)






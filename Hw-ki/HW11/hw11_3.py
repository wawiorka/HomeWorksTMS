"""3. Программа с классом Car. При инициализации объекта
ему должны задаваться атрибуты color, type и year.
Реализовать пять методов. Запуск автомобиля – выводит
строку «Автомобиль заведён». Отключение автомобиля –
выводит строку «Автомобиль заглушен». Методы для
присвоения автомобилю года выпуска, типа и цвета."""

class Car:

    def __init__(self, color, type, year):
        self.__color = color
        self.__type = type
        self.__year = year

    def start_car(self):
        print("Автомобиль заведён")

    def disabling_car(self):
        print("Автомобиль заглушен")

    def get_year(self):
        return self.__year

    def get_brand(self):
        return self.__type

    def get_color(self):
        return self.__color

    # def set_year(self, year):
    #     self.__year = year
    #
    # def set_brand(self, type):
    #     self.__type = type
    #
    # def set_color(self, color):
    #     self.__color = color


auto1 = Car("красный", "Мазда", 2020)
auto2 = Car("белый", "Фольксваген", 2023)
auto3 = Car("черный", "Мерседес", 2024)

auto1.start_car()
auto1.disabling_car()
print(auto1.get_year())
print(auto1.get_color())
print(auto1.get_brand())
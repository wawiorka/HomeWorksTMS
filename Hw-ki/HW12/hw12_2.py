"""2. ПчёлоСлон
Экземпляр класса инициализируется двумя целыми числами,
первое относится к пчеле, второе – к слону. Класс реализует
следующие методы:
● fly() – возвращает True, если часть пчелы не меньше части
слона, иначе – False
● trumpet() – если часть слона не меньше части пчелы,
возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
● eat(meal, value) – может принимать в meal только ”nectar”
или “grass”. Если съедает нектар, то value вычитается из
части слона, пчеле добавляется. Иначе – наоборот. Не
может увеличиваться больше 100 и уменьшаться меньше 0."""

class BeeElephant:
    def __init__(self, num_bee, num_el):
        self.num_bee = num_bee
        self.num_el = num_el


    def fly(self):
        return self.num_bee >= self.num_el


    def trumpet(self):
        if self.num_bee <= self.num_el:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"


    def eat(self, meal, value):
        if meal == "nectar":
            if 0 <= self.num_bee <= (100 - value) and (0 + value) <= self.num_el <= 100:
                self.num_bee += value
                self.num_el -= value
        elif meal == "grass":
            if (0 + value) <= self.num_bee <= 100 and 0 <= self.num_el <= (100 - value):
                self.num_bee -= value
                self.num_el += value


animal = BeeElephant(25, 30)
print(animal.fly())
print(animal.trumpet())
animal.eat("nectar", 20)
print(animal.num_bee)
print(animal.num_el)
print("2---*---*---")
animal.eat("grass", 30)
print(animal.num_bee)
print(animal.num_el)
print("3---*---*---")
animal.eat("grass", 30)
print(animal.num_bee)
print(animal.num_el)
print("4---*---*---")
animal.eat("nectar", 20)
print(animal.num_bee)
print(animal.num_el)

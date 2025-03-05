"""2. Напишите программу с классом Math. При
инициализации атрибутов нет. Реализовать методы addition,
subtraction, multiplication и division. При передаче в методы
двух числовых параметров нужно производить с
параметрами соответствующие действия и печатать ответ."""

class Math:

    def addition(self, num1, num2):
        result = num1 + num2
        print(f"Результат сложения {num1} и {num2}: {result}")

    def subtraction(self, num1, num2):
        result = num1 - num2
        print(f"Результат вычитания {num1} и {num2}: {result}")

    def multiplication(self, num1, num2):
        result = num1 * num2
        print(f"Результат умножения {num1} и {num2}: {result}")

    def set_zero(self, num2):
        if num2 == 0:
            raise ZeroDivisionError("Делить на 0 нельзя.")

    def division(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Делить на 0 нельзя.")
        else:
            result = num1 / num2
            print(f"Результат деления {num1} и {num2}: {result}")


try:
    res = Math()
    res.num1 = 32
    res.num2 = 0
    res.addition(res.num1, res.num2)
    res.subtraction(res.num1, res.num2)
    res.multiplication(res.num1, res.num2)
    res.division(res.num1, res.num2)

except ZeroDivisionError as e:
    print(e)

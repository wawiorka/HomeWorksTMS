"""2. Реализовать программу для бесконечной циклической
последовательности чисел (например, 1-2-3-1-2-3-1-2...).
Последовательность реализовать с помощью генераторной
функции, количество чисел для вывода задаётся
пользователем с клавиатуры."""

def gen_func(finish):
    a = 1
    k = 0
    while k <= finish:
        yield a
        a += 1
        k += 1
        if k % 3 == 0:
            a = 1
            yield a
            a += 1
            k += 1


n = int(input("Введите желаемое количество чисел "))
b = gen_func(n)

for i in b:
    print(i, end="-")


# хотела ниже усовершенствовать код, сократить его, через while True реализовать.
# То же самое почти, не довольна

# def gen_func(finish):
#     a = 1
#     k = 0
#     while True:
#         yield a
#         a += 1
#         k += 1
#         if k % 3 == 0:
#             a = 1
#             yield a
#             a += 1
#             k += 1
#         if k == finish:
#             break
#
#
# n = int(input("Введите желаемое количество чисел "))
# b = gen_func(n)

for i in b:
    print(i, end="-")
# последовательная задача
import math
import time
a = 100.45
b = 50.5


# def task(name, duration):
#     print(f"Задача {name} началась")
#     time.sleep(duration)
#     print(f"Задача {name} завершилась")

start_time = time.time()

# y1 = 5 * a + 3 * math.pow(b, 2)* math.sqrt(1 + math.pow(math.sin(a), 2))
# y2 = math.sqrt(b + math.pow(math.sin(a), 2))
y = round(5 * a + 3 * math.pow(b, 2)* math.sqrt(1 + math.pow(math.sin(a), 2)) + math.sqrt(b + math.pow(math.sin(a), 2)), 2)

end_time = time.time()

print(f"Решение последовательной задачи: {y}.")
print(f"Время последовательной задачи: {end_time - start_time:.6f} секунд")
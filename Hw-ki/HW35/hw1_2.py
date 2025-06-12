# поточная задача

import threading
import math
import time

def result1(a,b):
    y1 = 5 * a + 3 * math.pow(b, 2) * math.sqrt(1 + math.pow(math.sin(a), 2))
    return y1

def result2(a,b):
    y2 = math.sqrt(b + math.pow(math.sin(a), 2))
    return y2


def wrapme(func, res, *args, **kwargs):
    result.append(func(*args, **kwargs))

result = []

start_time = time.time()
a, b = 100.45, 50.5
thread1 = threading.Thread(target=wrapme, args=(result1, result, a, b))
thread2 = threading.Thread(target=wrapme, args=(result2, result, a, b))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

y = round(sum(result), 2)

end_time = time.time()

print(f"Решение поточной задачи: {y}.")
print(f"Время поточной задачи: {end_time - start_time:.6f} секунд")
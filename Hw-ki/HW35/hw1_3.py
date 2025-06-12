# процессорная задача

from multiprocessing import Process, Queue
import math
import time

def result1(a,b,queue):
    y1 = 5 * a + 3 * math.pow(b, 2) * math.sqrt(1 + math.pow(math.sin(a), 2)) + math.sqrt(b + math.pow(math.sin(a), 2))
    queue.put(round(y1, 2))
#
# def result2(a,b, queue):
#     y2 = math.sqrt(b + math.pow(math.sin(a), 2))
#     queue.put(y2)

def print_result(queue):
    while not queue.empty():
        print("Решение процессорной задачи:", queue.get())

start_time = time.time()
if __name__ == "__main__":
    a, b = 100.45, 50.5
    y = Queue()
    p1 = Process(target=result1, args=(a, b, y))
    # p2 = Process(target=result2, args=(a, b, y))
    p3 = Process(target=print_result, args=(y,))
    p1.start()
    p1.join()
    # p2.start()
    # p2.join()
    p3.start()
    p3.join()

end_time = time.time()

# print(f"Решение поточной задачи: {p3}.")
print(f"Время процессорной задачи: {end_time - start_time:.6f} секунд")
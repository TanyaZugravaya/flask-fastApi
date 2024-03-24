# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.
import random
import time
import threading
import multiprocessing
import asyncio


def generate_random_array():
    return [random.randint(1, 100) for _ in range(1_000_000)]


def calculate_sum(array):
    return sum(array)


def thread_task(array):
    start_time = time.time()
    result = calculate_sum(array)
    duration = time.time() - start_time
    with open("thread_result.txt", "w") as file:
        file.write(f"Thread Execution Time: {duration} seconds\nSum: {result}")


def process_task(array):
    start_time = time.time()
    result = calculate_sum(array)
    duration = time.time() - start_time
    with open("process_result.txt", "w") as file:
        file.write(f"Process Execution Time: {duration} seconds\nSum: {result}")


async def async_task(array):
    start_time = time.time()
    result = calculate_sum(array)
    duration = time.time() - start_time
    with open("async_result.txt", "w") as file:
        file.write(f"Async Execution Time: {duration} seconds\nSum: {result}")


if __name__ == '__main__':
    array = generate_random_array()

    thread = threading.Thread(target=thread_task, args=(array,))
    process = multiprocessing.Process(target=process_task, args=(array,))
    asyncio.run(async_task(array))

    thread.start()
    process.start()

    thread.join()
    process.join()

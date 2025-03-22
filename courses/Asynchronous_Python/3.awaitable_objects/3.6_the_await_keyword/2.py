"""
Описание задачи:
Расставьте ключевое слово await там, где это необходимо, чтобы код заработал.
Запустите код с помощью asyncio.run()

Sample Input:


Sample Output:
Начинаем задачу 1
Начинаем задачу 2
Начинаем задачу 3
Привет из корутины task1
Привет из корутины task2
Задача 1 завершилась
Привет из корутины task3
Задача 2 завершилась
Задача 3 завершилась
"""

import asyncio


async def task1():
    print("Начинаем задачу 1")
    await asyncio.sleep(1)
    print("Привет из корутины task1")
    await asyncio.sleep(1)
    print("Задача 1 завершилась")


async def task2():
    print("Начинаем задачу 2")
    await asyncio.sleep(2)
    print("Привет из корутины task2")
    await asyncio.sleep(2)
    print("Задача 2 завершилась")


async def task3():
    print("Начинаем задачу 3")
    await asyncio.sleep(3)
    print("Привет из корутины task3")
    await asyncio.sleep(3)
    print("Задача 3 завершилась")


async def main():
    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())
    task_3 = asyncio.create_task(task3())
    await asyncio.gather(task_1, task_2, task_3)


asyncio.run(main())

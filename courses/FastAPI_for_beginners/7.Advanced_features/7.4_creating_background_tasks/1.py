"""
Создайте приложение FastAPI, которое использует BackgroundTasks для
асинхронной имитации обработки заказа.

Используйте класс BackgroundTasks из fastapi для выполнения фоновой задачи.

Реализуйте функцию process_order(order_id: int), которая:
Имитирует обработку заказа с помощью time.sleep(3) (3 секунды).
Выводит в консоль сообщение: Order {order_id} processed.

Реализуйте эндпоинт GET /order/{order_id}, который:
Принимает параметр пути order_id (целое число).
Добавляет фоновую задачу для вызова функции process_order с параметром
order_id.

Возвращает JSON-ответ
{"message": "Order processing started", "order_id": order_id}.
"""

import time

from fastapi import FastAPI, BackgroundTasks, status

app = FastAPI()


def process_order(order_id: int):
    time.sleep(3)
    print(f"Order {order_id} processed.")


@app.get(
    "/order/{order_id}",
    response_model=dict,
    status_code=status.HTTP_200_OK
)
def get_order(order_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_order, order_id)
    return {"message": "Order processing started", "order_id": order_id}

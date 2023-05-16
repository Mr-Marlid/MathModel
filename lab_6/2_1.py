import numpy as np

arrival_interval = 0.1
service_time = 0.5
queue_limit = 5
total_cars = 400

queue1_length_sum = 0
queue2_length_sum = 0
lost_customers = 0
total_service_time = 0
departure_intervals = []

queue1 = []
queue2 = []
current_time = 0

for _ in range(total_cars):
    # Генерируем время прибытия следующего клиента
    next_arrival = np.random.exponential(arrival_interval)
    current_time += next_arrival

    # Удаляем клиентов, которые закончили обслуживание
    queue1 = [t for t in queue1 if t > current_time]
    queue2 = [t for t in queue2 if t > current_time]

    # Выбираем очередь для клиента
    if len(queue1) < queue_limit and (len(queue1) <= len(queue2) or len(queue2) == queue_limit):
        queue = queue1
    elif len(queue2) < queue_limit:
        queue = queue2
    else:
        lost_customers += 1
        continue

    # Генерируем время обслуживания и добавляем клиента в очередь
    service = np.random.exponential(service_time)
    if len(queue) == 0:
        departure_time = current_time + service
    else:
        departure_time = queue[-1] + service

    queue.append(departure_time)

    # Обновляем статистику
    if queue == queue1:
        queue1_length_sum += len(queue1)
    else:
        queue2_length_sum += len(queue2)

    total_service_time += service
    departure_intervals.append(service)

# Вычисляем искомые значения
avg_queue1_length = queue1_length_sum / total_cars
avg_queue2_length = queue2_length_sum / total_cars
lost_customers_percent = (lost_customers / total_cars) * 100
avg_service_duration = total_service_time / (total_cars - lost_customers)

print(f"Среднее число клиентов в первой очереди: {avg_queue1_length:.2f}")
print(f"Среднее число клиентов во второй очереди: {avg_queue2_length:.2f}")
print(f"Процент клиентов, которые отказались от обслуживания: {lost_customers_percent:.2f}%")
print(f"Интервалы времени между отъездами клиентов: {departure_intervals}")
print(f"Среднее время пребывания клиента на заправке: {avg_service_duration:.2f} единиц времени")

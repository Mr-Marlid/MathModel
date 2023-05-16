
'''
Чтобы определить оптимальные значения "зеленых" интервалов для обоих направлений,
можно провести имитационное моделирование. Вначале опишем базовые характеристики
системы, а затем проведем эксперименты с различными интервалами зеленого света,
чтобы найти оптимальное значение.

Параметры системы:

Математическое ожидание времени между автомобилями: 12 секунд для 1-го направления
и 9 секунд для 2-го направления.
Интервал между автомобилями при движении через туннель: 2 секунды.
Время красного света для обоих направлений: 60 секунд.
Сначала сгенерируем список с 1000 автомобилей для каждого направления
с экспоненциальным распределением времени между ними. Затем будем проводить
 имитационное моделирование с различными интервалами зеленого света и рассчитывать
 среднее время ожидания для всех автомобилей.

Для имитационного моделирования можно использовать следующий алгоритм:

Инициализация переменных для хранения времени ожидания, текущего времени и состояния светофора.
Обработка событий в порядке их возникновения: прибытие автомобиля, переключение светофора.
Обновление времени ожидания и текущего времени при возникновении событий.
Вычисление среднего времени ожидания для всех автомобилей.
Следует провести эксперименты с разными интервалами зеленого света и выбрать
те значения, при которых среднее время ожидания для всех автомобилей будет минимальным.
Важно также учесть, что сумма времени зеленого света для обоих направлений и времени
красного света должна быть равна общему циклу светофора.
'''

import numpy as np
import heapq


# Определим функцию для моделирования движения через туннель
def simulate_traffic_light(green_duration_1, green_duration_2, num_cars=1000):
    # Генерируем интервалы времени между прибытием автомобилей для каждого направления
    inter_arrival_time_1 = np.random.exponential(scale=12, size=num_cars)
    inter_arrival_time_2 = np.random.exponential(scale=9, size=num_cars)

    # Вычисляем времена прибытия автомобилей на светофор для каждого направления
    arrival_times_1 = np.cumsum(inter_arrival_time_1)
    arrival_times_2 = np.cumsum(inter_arrival_time_2)

    # Определяем длительность красного и полного цикла светофора
    red_duration = 60
    cycle_duration = green_duration_1 + green_duration_2 + 2 * red_duration

    # Инициализируем списки времен ожидания для каждого направления
    waiting_times_1 = []
    waiting_times_2 = []

    # Инициализируем очереди для каждого направления
    queue_1 = []
    queue_2 = []

    # Создаем список событий (прибытие автомобилей и переключение светофора)
    events = [(t, 1, 'arrival') for t in arrival_times_1] + [(t, 2, 'arrival') for t in arrival_times_2]

    # Добавляем начальные события переключения светофора
    events.append((green_duration_1, 0, 'red_both'))
    events.append((green_duration_1 + red_duration, 0, 'green_2'))

    # Преобразуем список событий в кучу (heap) для эффективного извлечения минимального элемента
    heapq.heapify(events)

    # Инициализируем текущее время и состояние светофора
    current_time = 0
    light_state = 'green_1'

    # Обрабатываем события, пока они есть
    while events:
        # Извлекаем следующее событие из кучи
        event_time, direction, event_type = heapq.heappop(events)
        current_time = event_time

        # Обрабатываем событие в зависимости от его типа (прибытие автомобиля или переключение светофора)
        if event_type == 'arrival':
            if direction == 1:
                heapq.heappush(queue_1, event_time)
            else:
                heapq.heappush(queue_2, event_time)
        else:  # event_type == 'light_switch'
            light_state = event_type

        # Если светофор зеленый для определенного направления и в очереди есть автомобили,
        # обрабатываем автомобили в очереди:
        if light_state == 'green_1' and queue_1:
            car_arrival_time = heapq.heappop(queue_1)
            waiting_time = current_time - car_arrival_time
            waiting_times_1.append(waiting_time)
            heapq.heappush(events, (current_time + 2, 1, 'arrival'))
        elif light_state == 'green_2' and queue_2:
            car_arrival_time = heapq.heappop(queue_2)
            waiting_time = current_time - car_arrival_time
            waiting_times_2.append(waiting_time)
            heapq.heappush(events, (current_time + 2, 2, 'arrival'))

        # Если обработано достаточное количество автомобилей, завершаем моделирование
        if len(waiting_times_1) >= num_cars and len(waiting_times_2) >= num_cars:
            break

            # Рассчитываем время следующего переключения светофора и добавляем соответствующее событие в кучу
        cycle_position = current_time % cycle_duration
        if cycle_position < green_duration_1 and light_state != 'green_1':
            next_event_time = green_duration_1
            next_event_type = 'red_both'
        elif cycle_position < green_duration_1 + red_duration and light_state != 'red_both':
            next_event_time = green_duration_1 + red_duration
            next_event_type = 'green_2'
        elif cycle_position < green_duration_1 + red_duration + green_duration_2 and light_state != 'green_2':
            next_event_time = green_duration_1 + red_duration + green_duration_2
            next_event_type = 'red_both'
        else:
            next_event_time = current_time + (cycle_duration - cycle_position)
            next_event_type = 'green_1'

        heapq.heappush(events, (current_time + (next_event_time - cycle_position), 0, next_event_type))

    # Рассчитываем среднее время ожидания для всех автомобилей
    average_waiting_time = (sum(waiting_times_1) + sum(waiting_times_2)) / (
            len(waiting_times_1) + len(waiting_times_2))
    return average_waiting_time


# Определяем функцию для нахождения оптимальных интервалов зеленого света
def find_optimal_green_intervals(min_green_duration, max_green_duration, step=1, num_cars=1000):
    best_waiting_time = float('inf')
    best_green_durations = (0, 0)

    for green_duration_1 in range(min_green_duration, max_green_duration + 1, step):
        for green_duration_2 in range(min_green_duration, max_green_duration + 1, step):
            avg_waiting_time = simulate_traffic_light(green_duration_1, green_duration_2, num_cars)

            if avg_waiting_time < best_waiting_time:
                best_waiting_time = avg_waiting_time
                best_green_durations = (green_duration_1, green_duration_2)

    return best_green_durations, best_waiting_time


# Проводим эксперименты, меняя значения зеленого света
min_green_duration = 30
max_green_duration = 120
step = 5

optimal_green_durations, optimal_waiting_time = find_optimal_green_intervals(min_green_duration, max_green_duration,
                                                                             step)
print(f"Оптимальные значения зеленого света: {optimal_green_durations}")
print(f"Минимальное среднее время ожидания: {optimal_waiting_time}")

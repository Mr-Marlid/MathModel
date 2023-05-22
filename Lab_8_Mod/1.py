import numpy as np
import pandas as pd

# 100 часов
sim_time = 100 * 60

#время поступления
t_1 = 30
#Первичная
t_2 = 30
#Вторичная, если прошли первичную
t_3 = 30
# Полная вторичная
t_4 = 100
#вероятность поломки
failure_probability = 0.05
# Переменные и счётчики
time = 0
status = 0
failure_count = 0
full_reg_count = 0
intermediate_storage = []

# Функция для генерации случайных чисел из экспоненциального распределения
def exp_regulation(mean_time):
    return np.random.exponential(mean_time)


# Функция имитации процесса регулирования
def simulate_regulation():
    global time, status, failure_count, full_reg_count, intermediate_storage

    while time < sim_time:
        # Генерация случайного времени прибытия для двух агрегатов
        time_to_next_arrival = exp_regulation(t_1)

        # Проверка, регулировались ли предыдущие агрегаты
        if status == 0:
            # Выполнение первичной регулировки
            time_to_primary_regulation = exp_regulation(t_2)
            time += time_to_primary_regulation

            # Проверка, не сработала ли первичная регулировка
            if np.random.random() < failure_probability:
                 # полная вторичная регулировка
                failure_count += 1
                time_to_secondary_regulation = exp_regulation(t_4)
                time += time_to_secondary_regulation
                status = 1                
            else:
                # вторичная регулировка
                time_to_secondary_regulation = exp_regulation(t_3)
                time += time_to_secondary_regulation
                status = 1
        else:
            # Добавить агрегаты в промежуточное хранилище
            intermediate_storage.append(2)
            status = 0

        # Проверка промежуточного хранилища на заполненность, требующую полного регулирования
        if len(intermediate_storage) >= 2:
            full_reg_count += len(intermediate_storage) // 2
            intermediate_storage = intermediate_storage[len(intermediate_storage) % 2:]

        time += time_to_next_arrival

    return failure_count, full_reg_count

# Старт симуляции
failure_count, full_reg_count = simulate_regulation()

# Рассчёт вероятности отказа первичной регуляции
failure_prob = failure_count / (sim_time / 60 * 2 / 30)

# Рассчёт среднего количество заполнителей в промежуточном хранилище, требующих полного регулирования
avg_full_reg = full_reg_count / (sim_time / 60 * 2 / 30)

# Рассчёт параметров системы промежуточного хранения для обеспечения безотказной работы агрегатов
max_arrivals = (1 - failure_prob) * 2 / 3
avg_arrivals = avg_full_reg / (sim_time / 60)

# Вывод
print("Результат:")
print(f"Вероятность отказа первичной регулировке: {failure_prob:.2f}")
print(f"Среднее количество агрегатов на промежуточном хранении, требующих полного регулирования: {avg_full_reg:.2f}")
print(f"Максимальное количество поступлений в систему промежуточного хранения для обеспечения отсутствия выхода из строя агрегатов:{ max_arrivals:.2f}")
print(f"Среднее количество поступлений в систему промежуточного хранения для обеспечения отсутствия отказов агрегатов:{ avg_arrivals:.2f}")
import numpy as np
import random

'''
Для анализа работы станка в течение обработки 500 деталей, необходимо смоделировать процесс
работы станка с учётом времени выполнения заданий, наладки станка, и устранения поломок.

Генерация случайных заданий: Моделируйте интервалы между заданиями, используя экспоненциальное
распределение со средним значением в 1 час.

Генерация времени наладки: Для каждого задания генерируйте случайное время наладки,
используя равномерное распределение на интервале 0.2-0.5 ч.

Генерация времени выполнения задания: Для каждого задания генерируйте случайное время
выполнения, используя нормальное распределение с математическим ожиданием 0.5 ч и
среднеквадратичным отклонением 0.1 ч.

Генерация времени между поломками: Моделируйте интервалы между поломками, используя
нормальное распределение со средним значением в 20 часов и среднеквадратичным отклонением 2 ч.

Генерация времени устранения поломки: Для каждой поломки генерируйте случайное время
устранения, используя равномерное распределение на интервале 0.1-0.5 ч.

Смоделируйте процесс работы станка, учитывая все вышеуказанные параметры. Следите за
временем, когда станок начинает и заканчивает каждое задание, а также за временем поломок и их устранения.

Проанализируйте загрузку станка, рассчитав отношение общего времени работы станка
(включая выполнение заданий, наладку, и устранение поломок) к общему времени работы
(время с начала первого задания до окончания обработки 500-го задания).

Проанализируйте среднее время выполнения задания, вычислив среднее значение времени
 выполнения всех заданий.

В результате вы получите информацию по загрузке станка и среднему времени выполнения
задания на основе смоделированных данных. Это позволит определить эффективность
станка и возможные меры по оптимизации его работы.
'''

# Constants
num_tasks = 100

# Generate tasks interarrival times
tasks_interarrival = np.random.exponential(scale=1, size=num_tasks)

# Generate setup times for tasks
setup_times = np.random.uniform(low=0.2, high=0.5, size=num_tasks)

# Generate task execution times
execution_times = np.random.normal(loc=0.5, scale=0.1, size=num_tasks)

# Generate breakdown interarrival times
breakdown_interarrival = np.random.normal(loc=20, scale=2, size=num_tasks)

# Generate breakdown repair times
repair_times = np.random.uniform(low=0.1, high=0.5, size=num_tasks)

# Simulation
task_start_times = [0] * num_tasks
task_end_times = [0] * num_tasks
current_time = 0
breakdown_time = breakdown_interarrival[0]
breakdown_index = 0

for i in range(num_tasks):
    # Check if the machine breaks down before the current task
    while current_time + tasks_interarrival[i] + setup_times[i] > breakdown_time:
        # Move current_time to the end of the repair time
        current_time = breakdown_time + repair_times[breakdown_index]
        breakdown_index += 1
        if breakdown_index < len(breakdown_interarrival):
            breakdown_time += breakdown_interarrival[breakdown_index]
        else:
            break

    # Task execution
    current_time += tasks_interarrival[i]
    task_start_times[i] = current_time
    current_time += setup_times[i] + execution_times[i]
    task_end_times[i] = current_time

total_time = task_end_times[-1] - task_start_times[0]
working_time = sum(setup_times) + sum(execution_times) + sum(repair_times[:breakdown_index])

# Results
machine_utilization = working_time / total_time
average_task_execution_time = np.mean(execution_times)

print(f"Machine utilization: {machine_utilization:.2%}")
print(f"Average task execution time: {average_task_execution_time:.2f} hours")

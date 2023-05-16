import math
import matplotlib.pyplot as plt
import numpy as np

# Метод Эйлера - это простой численный метод решения обыкновенного
# дифференциального уравнения. Он заключается в последовательном
# приближенном вычислении значений функции на всем интервале задания,
# используя значения функции и ее производной в начальной точке.
# задает начальные условия для решения дифференциального уравнения.

def init():
    y0, x0, x_n, h = 0, 0, 0.5, 0.1
    return y0, x0, x_n, h

# находим точное решение дифференциального уравнения,
# которое используется для сравнения с численным решением.
def exact_solution(x_values):
    exact_values = [math.tan(x) - x for x in x_values]
    return exact_values

# задаем правую часть дифференциального уравнения.
def f(x, y):
    return (y + x) ** 2

# Реализуем численное решение дифференциального
# уравнения первого порядка с помощью явного метода Эйлера
# Задача состоит в том, чтобы найти решение уравнения
# y'=(x+y)^2 на интервале от 0 до 0.5 с начальным условием y(0)=0.
def task_1():
    # Задаем начальные условия
    y0, x0, _, h = init()

    # Создаем списки для хранения значений y и x
    y_values = [y0]
    x_values = [x0]

    # Выполняем явный метод Эйлера
    while x_values[-1] < 0.5:
        y = y_values[-1] + h * f(x_values[-1], y_values[-1])
        x = x_values[-1] + h
        y_values.append(y)
        x_values.append(x)

    # Вычисляем точное решение

    exact_values = exact_solution(x_values)
    # Выводим значения на экран
    print("x\t y (Euler)\t y (exact)\t difference")
    print_(x_values, y_values)


def print_(x_values, y_values):
    exact_values = exact_solution(x_values)
    for i in range(len(x_values)):
        print("{:.1f}\t {:.6f}\t {:.6f}\t {:.6f}".format(x_values[i], y_values[i], exact_values[i],
                                                         abs(y_values[i] - exact_values[i])))
    plt.plot(x_values, y_values, label='Численное решение')
    plt.plot(x_values, exact_values, label='Точное решение')
    plt.legend()
    plt.show()


# 2222
# Реализуем метод Эйлера с модификацией Коши.
# В цикле while вычисляются значения y и x на каждом шаге,
# пока x не достигнет конечной точки интервала.
def euler_cosh(x0, y0, xn, h):
    x_values = [x0]
    y_values = [y0]
    while x0 < xn:
        y1 = y0 + h * f(x0, y0)
        y2 = y0 + h / 2 * (f(x0, y0) + f(x0 + h, y1))
        x0 += h
        y0 = y2
        x_values.append(x0)
        y_values.append(y0)
    return x_values, y_values


# В методе Эйлера с модификацией Коши используется улучшенный
# алгоритм решения дифференциального уравнения. Вместо использования
# только текущего значения функции, используется среднее значение на
# текущем и следующем шагах сетки,это позволяет более точно расчитать
# следующее значение функции.
def task_2():
    x0, y0, xn, h = init()
    x_values, y_values = euler_cosh(x0, y0, xn, h)
    print("x\t y (euler_cosh)\t y (exact)\t difference")
    print_(x_values, y_values)


# 33333
# Реализуем улучшенный метод Эйлера, который использует среднее
# значение на текущем и следующем шагах сетки для более точного
# расчета следующего значения функции. В цикле while вычисляются
# значения y и x на каждом шаге, пока x не достигнет конечной точки
# интервала.
def improved_euler(x0, y0, xn, h):
    x_values = [x0]
    y_values = [y0]
    while x0 < xn:
        y1 = y0 + h * f(x0, y0)
        y2 = y0 + h * f(x0 + h, y1)
        y0 = y0 + h / 2 * (f(x0, y0) + f(x0 + h, y2))
        x0 += h
        x_values.append(x0)
        y_values.append(y0)
    return x_values, y_values


# Улучшенный метод Эйлера для решения дифференциального уравнения
def task_3():
    x0, y0, xn, h = init()
    x_values, y_values = improved_euler(x0, y0, xn, h)
    print("x\t y (improved_euler)\t y (exact)\t difference")
    print_(x_values, y_values)


# 44444

# Метод Рунге-Кутты 4-го порядка - это численный метод
# решения дифференциальных уравнений. Он использует
# несколько коэффициентов, которые позволяют более
# точно приближать решение на каждом шаге сетки.
# Алгоритм метода состоит из нескольких шагов, включая
# задание начальных условий, вычисление коэффициентов
# k1, k2, k3 и k4 для нахождения следующего значения функции,
# и переход к следующей точке сетки.
def runge_kutta(x0, y0, xn, h):
    x_values = [x0]
    y_values = [y0]
    while x0 < xn:
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h / 2, y0 + k1 / 2)
        k3 = h * f(x0 + h / 2, y0 + k2 / 2)
        k4 = h * f(x0 + h, y0 + k3)
        y0 = y0 + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x0 += h
        x_values.append(x0)
        y_values.append(y0)
    return x_values, y_values


# Метод Рунге-Кутты 4-го порядка для решения дифференциального уравнения
# Реализуем метод Рунге-Кутты 4-го порядка, который является более
# точным методом для решения дифференциальных уравнений, чем метод
# Эйлера. В цикле while вычисляются значения y и x на каждом шаге,
# пока x не достигнет конечной точки интервала.
def task_4():
    x0, y0, xn, h = init()
    x_values, y_values = runge_kutta(x0, y0, xn, h)
    print("x\t y (runge_kutta)\t y (exact)\t difference")
    print_(x_values, y_values)

# Рунге-Кутты 4-го порядка и строит график численного решения и
# аналитического решения.

# Функция task_5() задает начальные условия, определяет функции
# k1, l1, k2, l2, k3, l3, k4 и l4 для реализации метода
# Рунге-Кутты 4-го порядка. Затем она вычисляет численное
# решение на заданном интервале, строит график численного
# решения и аналитического решения.

# Аналитическое решение получается путем решения дифференциального
# уравнения и подстановки начальных условий. График численного
# решения и аналитического решения позволяет сравнить результаты
# и оценить точность численного метода.
def task_5():
    # задание начальных условий
    x0 = 0
    y0 = 1
    z0 = 3
    h = 0.2
    N = int(1 / h)

    # функции для метода Рунге-Кутты 4 порядка
    def k1(x, y, z):
        return z

    def l1(x, y, z):
        return 2 * x * z / (x ** 2 + 1)

    def k2(x, y, z):
        return z + h * l1(x, y, z) / 2

    def l2(x, y, z):
        return 2 * (x + h / 2) * l1(x, y, z) / (x ** 2 + 1)

    def k3(x, y, z):
        return z + h * l2(x, y, z) / 2

    def l3(x, y, z):
        return 2 * (x + h / 2) * l2(x, y, z) / (x ** 2 + 1)

    def k4(x, y, z):
        return z + h * l3(x, y, z)

    def l4(x, y, z):
        return 2 * (x + h) * l3(x, y, z) / (x ** 2 + 1)

    # метод Рунге-Кутты 4 порядка
    x_arr = np.zeros(N + 1)
    y_arr = np.zeros(N + 1)
    y_ist_arr = np.zeros(N + 1)

    def y_ist(x):
        return -x ** 3 + 3 * x + 1

    x = x0
    y = y0
    z = z0

    x_arr[0] = x
    y_arr[0] = y
    y_ist_arr[0] = y_ist(x)

    for i in range(N):
        y_prev = y
        z_prev = z

        k1_val = k1(x, y_prev, z_prev)
        l1_val = l1(x, y_prev, z_prev)

        k2_val = k2(x, y_prev, z_prev)
        l2_val = l2(x, y_prev, z_prev)

        k3_val = k3(x, y_prev, z_prev)
        l3_val = l3(x, y_prev, z_prev)

        k4_val = k4(x, y_prev, z_prev)
        l4_val = l4(x, y_prev, z_prev)

        y = y_prev + (k1_val + 2 * k2_val + 2 * k3_val + k4_val) / 6
        z = z_prev + (l1_val + 2 * l2_val + 2 * l3_val + l4_val) / 6

        x += h

        x_arr[i + 1] = x
        y_arr[i + 1] = y
        y_ist_arr[i + 1] = y_ist(x)

    # построение графиков
    plt.plot(x_arr, y_arr, label="Численное решение")
    plt.plot(x_arr, y_ist_arr, label="Аналитическое решение")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


task_1()
task_2()
task_3()

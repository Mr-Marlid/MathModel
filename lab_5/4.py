import numpy as np
#функция для метода Рунге-Кутты 4-го порядка:
def runge_kutta(f, x0, y0, h, x_end):
    x = [x0]
    y = [y0]
    while x[-1] < x_end:
        k1 = f(x[-1], y[-1])
        k2 = f(x[-1] + h/2, y[-1] + h*k1/2)
        k3 = f(x[-1] + h/2, y[-1] + h*k2/2)
        k4 = f(x[-1] + h, y[-1] + h*k3)
        y_new = y[-1] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        y.append(y_new)
        x.append(x[-1] + h)
    return x, y

#функция точного решения:

def exact_solution(x):
    return np.tan(x) - x

y0 = 0
h = 0.1
x_end = 1.0

#Запускаем метод Рунге-Кутты и получаем численное решение:

x, y = runge_kutta(lambda x, y: (x+y)**2, 0, 0, h, x_end)

#Сравниваем численное решение с точным решением и выводим результаты в виде таблицы:

print("{:<10} {:8} {:8} {:9}".format("x", "y_num", "y_exact", "error"))
for i in range(len(x)):
    y_exact = exact_solution(x[i])
    error = abs( y[i] - y_exact)
    print("{:<10.1f} {:.7f} {:.7f} {:.7f}".format(x[i], y[i], y_exact, error))

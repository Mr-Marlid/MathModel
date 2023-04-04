from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Rectangle
import random

def rand_cisla(N):
    x = []
    for i in range(N):
        x.append(round(random.uniform(-7, 7), 2))
    return (x)

def massiv(x,y):
    black_x=[]
    black_y=[]
    green_x=[]
    green_y=[]
    k=0
    for i in range(len(x)):
        if y[i]**2+x[i]**2<49:
            black_x.append(x[i])
            black_y.append(y[i])
            k=k+1
        else:
            green_x.append(x[i])
            green_y.append(y[i])
    return black_x, black_y, green_x, green_y, k

# 7  по моему варианту
n = 8
x = []
y = []
print("Введите N - кол-во случайных точек")
N = int(input())  # кол-во случайных точек

theta = np.linspace(0, 2 * np.pi, 150)
radius = 7
a = radius * np.cos(theta)
b = radius * np.sin(theta)



   ##x**2+y**2<r**2
x_rand = rand_cisla(N)                     #получаем рандомные точки и рисуем
y_rand = rand_cisla(N)

black_x, black_y, green_x, green_y, M=massiv(x_rand,y_rand)
print("M=",M)

print("π=",(4*(M/N)) )

fig, ax = plt.subplots()
ax.add_patch(Rectangle((-7, -7), 14, 14, edgecolor='red', facecolor='none', fill=True, lw=1)) # нарисовали прямоугольник
plt.scatter(black_x, black_y, s=10, c="black")
plt.scatter(green_x,green_y, s=10, c="green")
plt.plot(a, b, c="blue")


plt.grid(True)
plt.legend()
plt.show()

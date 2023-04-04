from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Rectangle
import random

def integrand(x):
    return math.sqrt(11-(7*math.sin(x)*math.sin(x)))

def rand_cisla(ot_chisla,do_chisla, N):
    x = []
    for i in range(N):
        x.append(round(random.uniform(ot_chisla, do_chisla), 2))
    return (x)

def sravnen(x, y):
    k=0
    for i in range(len(x)):
        if y[i]<integrand(x[i]):
            k=k+1
    return k

def massiv(x,y):
    black_x=[]
    black_y=[]
    green_x=[]
    green_y=[]
    for i in range(len(x)):
        if y[i]<integrand(x[i]):
            black_x.append(x[i])
            black_y.append(y[i])
        else:
            green_x.append(x[i])
            green_y.append(y[i])
    return black_x, black_y, green_x, green_y

# 7  по моему варианту
n = 8
x = []
y = []
print("Введите N - кол-во случайных точек")
N = int(input())  # кол-во случайных точек
for i in np.arange(0,5,0.01):
    x.append(i)
    y.append(integrand(i))

fig, ax = plt.subplots()
ax.add_patch(Rectangle((0, 0), 5, (max(y)), edgecolor='red', facecolor='none', fill=True, lw=1)) # нарисовали прямоугольник
#plt.plot(x, y, c="blue", label='y=f(x)')

x_rand = rand_cisla(0, 5, N)                     #получаем рандомные точки и рисуем
y_rand = rand_cisla(0, max(y), N)


black_x, black_y, green_x, green_y=massiv(x_rand,y_rand)
plt.scatter(black_x, black_y, s=10, c="black")
plt.scatter(green_x,green_y, s=10, c="green")

#plt.scatter(x_rand, y_rand, s=10, c="green")

I = quad(integrand, 0, 5)[0]
print("Интеграл=", I)

M=sravnen(x_rand, y_rand)
print("M=",M)

a=5
print("a=",a)
b=round((max(y)),2)
print("b=",b)


S_primerno=(M/N)*a*b
print("S≈",S_primerno)

print("S(интеграл)=", I)

absolut=abs(S_primerno-I)
otnosit=(absolut/I)*100
print("Абсолютная погрешность =", absolut)
print("Относительная погрешность =", otnosit)


plt.plot(x, y, c="blue", label='y=f(x)')
plt.grid(True)
plt.legend()
plt.show()

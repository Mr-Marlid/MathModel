import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random

# получение значений функции
def func_y(i, n):
    if i < n:
        return (10 * i) / n
    if i >= n:
        return 10 * ((i - 20) / (n - 20))


# генерация случайных Х для точек
def rand_cisla(do_chisla, N):
    x = []
    for i in range(N):
        x.append(round(random.uniform(0, do_chisla), 2))
    return (x)

def k_tochek(x, y, N, n):
    k=0
    for i in range(N):
        if y[i]< func_y(x[i],n):
            k=k+1
    return k

def massiv(x,y,N,n):
    black_x=[]
    black_y=[]
    green_x=[]
    green_y=[]
    for i in range(N):
        if y[i]<func_y(x[i],n):
            black_x.append(x[i])
            black_y.append(y[i])
        if y[i]>func_y(x[i],n):
            green_x.append(x[i])
            green_y.append(y[i])
    return black_x, black_y, green_x, green_y


# 7  по моему варианту
n = 8
x = []
y = []

print("Введите N - кол-во случайных точек")
N = int(input())  # кол-во случайных точек

for i in range(21):
    x.append(i)
    y.append(func_y(i, n))

a = 20
b = 10
xx=[0,20]
yy=[0,0]
fig, ax = plt.subplots()
ax.add_patch(Rectangle((0, 0), a, b, edgecolor='red', facecolor='none', fill=True, lw=1)) # нарисовали прямоугольник

x_rand = rand_cisla(a, N)                     #получаем рандомные точки и рисуем
y_rand = rand_cisla(b, N)
#plt.scatter(x_rand, y_rand, s=10, c="green")

black_x, black_y, green_x, green_y=massiv(x_rand,y_rand,N, n)
plt.scatter(black_x, black_y, s=10, c="black")
plt.scatter(green_x,green_y, s=10, c="green")

M=k_tochek(x_rand, y_rand, N, n)     # получили кол-во случайных точек в треугольнике
print("M=",M)
print("a=", a)
print("b=",b)

#тут написать вызов функции разных точек

S_primerno=(M/N)*a*b
print("S≈",S_primerno)

S_tochno=(a*b)/2
print("S=",S_tochno)

absolut=abs(S_primerno-S_tochno)
otnosit=(absolut/S_tochno)*100
print("Абсолютная погрешность =", absolut)
print("Относительная погрешность =", otnosit)


plt.plot(x, y, c="blue", label='y=f(x)')
plt.plot(xx,yy, c="blue")
plt.grid(True)
plt.legend()
plt.show()

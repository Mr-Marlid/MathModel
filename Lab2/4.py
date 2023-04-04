import math
import random
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def func_p(x):
    return np.sqrt(19 * np.cos(x) ** 2 + 3 * np.sin(x) ** 2)

def M(x,y,N):
    r=[]
    fi=[]
    x_point = []
    y_point = []
    x_not_point = []
    y_not_point = []
    m = 0
    for i in range(N):
        r.append(math.sqrt(x[i]**2+y[i]**2))
    for i in range(N):
        if x[i]>0:
            fi.append(np.arctan(y[i]/x[i]))
        elif x[i]<0:
            fi.append(np.pi+np.arctan(y[i]/x[i]))
        elif x[i]==0 and y[i]>0:
            fi.append(np.pi/2)
        elif x[i] == 0 and y[i] < 0:
            fi.append(-(np.pi / 2))
        elif x[i] == 0 and y[i] == 0:
            fi.append(0)
    for i in range(N):
        ro=func_p(fi[i])
        if r[i]<ro:
            m+=1
            x_point.append(x[i])
            y_point.append(y[i])
        else:
            x_not_point.append(x[i])
            y_not_point.append(y[i])
    return m, x_point,y_point, x_not_point,y_not_point

#func_p = lambda x: np.sqrt(15 * np.cos(x) ** 2 + 7 * np.sin(x) ** 2)
# Функция p в декартовых координатах:
func_x = lambda x: func_p(x) * np.cos(x)
func_y = lambda x: func_p(x) * np.sin(x)


print("Введите N - кол-во случайных точек")
N = int(input())  # кол-во случайных точек

fi = 0
points_x = []
points_y = []
while fi < (np.pi * 2):
    points_x.append(func_x(fi))
    points_y.append(func_y(fi))
    fi += 0.001

max_x=max(points_x)
min_x=min(points_x)
max_y=max(points_y)
min_y=min(points_y)

x_rand=[]
y_rand=[]
for i in range (N):
    x_rand.append(round(random.uniform(min_x, max_x),4))
    y_rand.append(round(random.uniform(min_y, max_y), 4))

print("[",min_x,";",max_x,"]")
print("[",min_y,";",max_y,"]")

int_func = lambda x: 15*np.cos(x)**2+7*np.sin(x)**2
true_S = round(sp.integrate.quad(int_func, 0, 2*np.pi)[0] / 2, 2)

m, x_dr, y_dr, no_x, no_y=M(x_rand,y_rand,N)
s=round((m/N)*max_x*max_y*4,2)

del_x=round(math.fabs(true_S-s),2)
otn_x=round((del_x/true_S)*100)

print("M=",m)
print("S=",true_S)
print("Приближенная S=",s)
print("Абсолютная погрешность:", del_x)
print("Относительная погрешность:", otn_x,"%")
fig, ax = plt.subplots()
ax.add_patch(Rectangle((min_x, min_y), max_x-min_x, max_y-min_y, edgecolor='red', facecolor='none', fill=True, lw=1)) # нарисовали прямоугольник
my_figure = plt.plot(points_x, points_y, color='blue')
plt.scatter(x_dr,y_dr,s=5,c="black")
plt.scatter(no_x, no_y, s=5, c="green")

plt.grid(True)
plt.show()

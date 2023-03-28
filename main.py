import numpy as np
from matplotlib import pyplot as plt
import math
import numpy
from random import randint
from random import uniform
from scipy import integrate

n = 13 # Вариант
N = 250

def tr_func1(x):
    return (10*x)/n
def tr_func2(x):
    return 10*(x-20)/(n-20)+20

def S_tr(x,y):
    return x*y/2

def triangle_fn(arr_x):
    print("Треугольник")
    arr_y1 = []
    arr_y2 = []
    for i in arr_x:
        y = round(tr_func1(i),2)
        arr_y1.append(y)
        y = round(tr_func2(i),2)
        arr_y2.append(y)
    arr_y3 = [arr_y1[0],arr_y2[0]]
    arr_x1 = [0,0]
    fig, ax = plt.subplots()
    plt.grid()  # Строим сетку
    ax.plot(arr_x, arr_y1, 'black')
    ax.plot(arr_x, arr_y2, color='black')
    ax.plot(arr_x1, arr_y3, color='black')

    a = round(max(arr_y2),0)
    b = max(arr_x)
    area = S_tr(a,b)
    M = 0
    for i in range(N+1):
        x = uniform(min(arr_x), max(arr_x))
        max_y = round(max(arr_y2),0)
        min_x = min(arr_x)
        y = uniform(min_x,max_y)

        if(y> round(tr_func2(x),2) or y< round(tr_func1(x),2)):
            ax.plot(x, y, 'p',color = 'r')
        else:
            ax.plot(x, y, 'p', color = 'y')
            M += 1
    S = M / N * a * b
    S = round(S,2)
    print("Площадь треугольника = ",area, "\nМонте карло: ", S)

    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()

def fun_int(x):

    return math.sqrt(29 - n * math.pow(math.cos(x),2))

def integrall_fn(ax,fig):
    x = []
    y = []
    i = 0.1
    while(i!=7):
        x.append(i)
        y.append(round(fun_int(i),2))
        i = round(i+0.1,1)
    ax.plot(x, y, 'black')
    # Строим сетку
    plt.grid()
    M = 0

    min_y = round(min(y),0)
    a = round(max(x), 0)
    b = round(max(y), 2)
    for i in range(N + 1):
        x = uniform(0, a)
        y = uniform(min_y,b)

        if y < fun_int(x):
            ax.plot(x, y, 'p', color='y')
            M += 1
        else:
            ax.plot(x, y, 'p', color='r')

    f = lambda x: math.sqrt(29 - n * math.pow(math.cos(x),2))
    s = integrate.quad(f, 0, 7)
    print("Значение интеграла: ", s[0])
    S = round(M / N * a * b, 2)
    print( "\nМонте карло: ", S)
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()

def circle_fn():
    x = []
    y = []
    i = 0
    while(i<=2*n):
        x.append(n + n*math.cos(i))
        y.append(n + n*math.sin(i))
        i = round(i+0.1,1)
    fig, ax = plt.subplots()
    plt.grid()  # Строим сетку
    ax.plot(x, y, 'black')

    M = 0
    for i in range(N + 1):
        x = uniform(0, 2*n)
        y = uniform(0, 2*n)
        if not(math.pow((x - n),2) + math.pow((y-n),2) < math.pow(n,2)):
            ax.plot(x, y, 'p', color='r')
        else:
            ax.plot(x, y, 'p', color='y')
            M += 1

    area = 4*n*(n/12)
    S = M/N*math.pow((2*n),2)
    pi = S/math.pow(n,2)
    print("Круг :", "Площадь круга :",area, "Монте карло:" ,S, "pi = 3.14\n Монте карло: ",pi)
    ax.axis('equal')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()

def p_fn(f,a,b):
    return math.sqrt(a*math.pow(math.cos(f),2) + b*math.pow(math.sin(f),2))

def pp(x,y):
    return math.sqrt(math.pow(x,2) + math.pow(y,2))

def ff(x,y):
    if x>0:
        return math.atan(y/x)
    elif x<0:
        return math.atan(y/x)+math.pi
    elif y>0:
        return math.pi/2
    else:
        return math.pi*(3/2)

def eleps_fn():
    A = 10
    B = n-10
    x = []
    y = []
    i = 0
    while i <= 2 * math.pi+1:
        x.append(p_fn(i,A,B)*math.cos(i))
        y.append(p_fn(i,A,B)*math.sin(i))
        i = round(i + 0.1, 1)
    a = round(max(x),0)+1
    b = round(max(y),0)+1
    fig, ax = plt.subplots()
    plt.grid()  # Строим сетку
    ax.plot(x, y, 'black')
    M = 0
    for i in range(N + 1):
        x = uniform(-a, a)

        y = uniform(-b,b)

        if pp(x,y)<p_fn(ff(x,y),A,B) :
            ax.plot(x, y, 'p', color='y')
            M += 1
        else:
            ax.plot(x, y, 'p', color='r')

    S = M/N*(a*b*4)
    ss = math.pi/2*(A+B)
    print ("ss = ",ss,"\n S = ",S)

    ax.axis('equal')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()



def draw():
    print('Число точек:', N )
    arr_x = []
    fig, ax = plt.subplots()
    for i in range(23):
        arr_x.append(i)
    #triangle_fn(arr_x)
    integrall_fn(ax,fig)
    #circle_fn()
    #eleps_fn()
draw()
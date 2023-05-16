import math
def f(x, y):
    return (x + y)**2

def exact_solution(x):
    return math.tan(x) - x

x0 = 0
y0 = 0
xf = 0.5
h = 0.1
n = int((xf - x0) / h)
x = [0]*(n+1)
y = [0]*(n+1)
k1=[0]*n
k2=[0]*n
for i in range(0,n):
    k1[i] = h * f(x[i], y[i])
    k2[i] = h * f(x[i] + h/2, y[i] + k1[i]/2)
    y[i+1] = y[i] + k2[i]
    x[i+1] = x[i] + h

    print("({:.1f}, {:.6f})".format(x[i], y[i]))

for i in range(n):
    x = x0 + i*h
    y_exact = exact_solution(x)
    y_numerical = y0+k2[i]
    error = abs(y_exact - y_numerical)
    print("({:.1f}, {:.6f}, {:.6f}, {:.6f})".format(x, y_exact, y_numerical, error))
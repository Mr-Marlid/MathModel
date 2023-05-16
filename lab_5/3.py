import math

def f(x,y):
    return (x+y)**2

def improved_euler(h,x0,y0,xn):
    n = int((xn-x0)/h)
    x = [x0+i*h for i in range(n+1)]
    y = [y0]*(n+1)
    for i in range(n):
        y_pred = y[i] + h*f(x[i],y[i])
        y[i+1] = y[i] + h*(f(x[i],y[i])+f(x[i+1],y_pred))/2
    return x,y

x,y = improved_euler(0.1,0,0,0.5)

print("x\ty\texact")
for i in range(len(x)):
    exact = math.tan(x[i])-x[i]
    print("{:.1f}\t{:.6f}\t{:.6f}".format(x[i],y[i],exact))
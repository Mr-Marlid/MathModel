import math

def euler_method(x0, y0, h, xn):
    x_values = [x0]
    y_values = [y0]
    while x_values[-1] < xn:
        x = x_values[-1] + h
        y = y_values[-1] + h * (x_values[-1] + y_values[-1])**2
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

x0 = 0
y0 = 0
h = 0.1
xn = 0.5

x_values, y_values = euler_method(x0, y0, h, xn)

exact_values = [math.tan(x) - x for x in x_values]

print("xk\tyk\tExact")
for i in range(len(x_values)):
     print("{:.1f}\t{:.5f}\t{:.5f}".format(x_values[i], y_values[i], exact_values[i]))

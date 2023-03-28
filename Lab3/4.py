num_elements = 10
a = 265
m = 129
x0 = 122

x_values = [x0]
for i in range(num_elements - 1):
    xi = (a * x_values[i]) % m
    x_values.append(xi)

print(x_values)
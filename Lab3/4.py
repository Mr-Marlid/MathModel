from matplotlib import pyplot as plt


num_elements = 10
a = 265
m = 129
x0 = 122
r = [1]
x_values = [x0]
for i in range(num_elements - 1):
    xi = (a * x_values[i]) % m
    x_values.append(xi)
    r.append(i+2)
print(x_values)
print (r)
plt.plot(r,x_values)   

plt.title("Line graph")   
plt.ylabel('R')   
plt.xlabel('N')   
plt.show()
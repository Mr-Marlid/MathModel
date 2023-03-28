from matplotlib import pyplot as plt
N = 5
R0 = 0.585
g = 927
r = []
y = [0.0] * N
x = R0
for i in range(N):
    y[i] = g * x % 1
    x = y[i]
    r.append(i+1)
    print(y[i])
plt.plot(r,y)   

plt.title("Line graph")   
plt.ylabel('R')   
plt.xlabel('N')   
plt.show()
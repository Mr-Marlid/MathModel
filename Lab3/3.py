N = 5
R0 = 0.585
g = 927

x = R0
for i in range(N):
    y = g * x % 1
    x = y
    print(y)
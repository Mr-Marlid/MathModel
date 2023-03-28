from matplotlib import pyplot as plt

R = 0.583
N = 6
result = []
r = []
for i in range(N):
    R = R ** 2
    R = int(R * 1000) % 1000000
    R /= 1000
    result.append(R)
    r.append(i+1)

print(result)
plt.plot(r,result)   

plt.title("Line graph")   
plt.ylabel('R')   
plt.xlabel('N')   
plt.show()  

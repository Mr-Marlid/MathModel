R = 0.583
N = 6
result = []

for i in range(N):
    R = R ** 2
    R = int(R * 1000) % 1000000
    R /= 1000
    result.append(R)

print(result)
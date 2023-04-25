import math
import random
import numpy as np
from scipy.stats import uniform, expon, norm
import matplotlib.pyplot as plt
import math

def initialization():
    n,a,b,mu,sigma,lam=10,3,9,1,2,1
    return n,a,b,mu,sigma,lam

def uniform_distribution(n, a, b):
    sample = []
    
    for i in range(n):
        x = a + (b - a) * random.random()
        sample.append(x)

    # Вычисляем оценку математического ожидания
    mean = sum(sample) / n

    # Вычисляем оценку дисперсии
    var = sum([(x - mean) ** 2 for x in sample]) / n

    return mean,var,sample

def exponential_distribution(n, lamda):
    sample = []
    for i in range(n):
        x = -1 / lamda * math.log(1 - random.random())
        sample.append(x)

    # Вычисляем оценку математического ожидания
    mean = sum(sample) / n

    # Вычисляем оценку дисперсии
    var = sum([(x - mean) ** 2 for x in sample]) / n
    return mean,var,sample

def normal_distribution(n,mu,sigma):
    # Генерируем выборку
    sample = []
    
    for i in range(n):
        x = mu + sigma * math.sqrt(-2 * math.log(random.random())) * math.cos(2 * math.pi * random.random())
        sample.append(x)

    # Вычисляем оценку математического ожидания
    mean = sum(sample) / n

    # Вычисляем оценку дисперсии
    var = sum([(x - mean) ** 2 for x in sample]) / n
    return mean,var,sample

def task1():
    # Конгруэнтный метод генерации случайных чисел - это алгоритм, который использует
    # простую формулу для генерации последовательности псевдослучайных чисел. Формула имеет следующий вид:
    # Xn+1 = (a*Xn + c) % m
    # где Xn - текущее значение в последовательности, a, c и m - константы,
    # которые определяют параметры генерации случайных чисел.
    # параметры конгруэнтного метода
    m = 2 ** 31 - 1
    a = 7 ** 5
    c = 0
    x = 12
    N = 1000

    for i in range(N):
        x = (a * x + c) % m
        print(x)


def task2():
    # равномерное распределение
    n, a, b, mu, sigma, lam=initialization()
    uniform_mean, uniform_var,_ = uniform_distribution(n,a,b)
    print("Равномерное распределение:")
    print("математическое ожидание:", uniform_mean)
    print("дисперсия:", uniform_var)

    # экспоненциальное распределение
    expon_mean, expon_var,_ = exponential_distribution(n,lam)
    print("Экспоненциальное распределение:")
    print("математическое ожидание:", expon_mean)
    print("дисперсия:", expon_var)

    # нормальное распределение
    norm_mean, norm_var,_ = normal_distribution(n,mu,sigma)
    print("Нормальное распределение:")
    print("математическое ожидание:", norm_mean)
    print("дисперсия:", norm_var)


def task3():
    n, a, b, mu, sigma, lam=initialization()
    n = 1000
    # равномерное распределение
    _,_,sample_uniform=uniform_distribution(n,a,b)
    print("равномерное распределение ",sample_uniform)
    # экспоненциальное распределение
    _,_,sample_expon=exponential_distribution(n,lam)
    print("экспоненциальное распределение ",sample_expon)
    # нормальное распределение
    _, _, sample_norm = normal_distribution(n,mu,sigma)
    print("нормальное распределение ",sample_norm)

def task4():
    # Заданные параметры
    _, a, b, mu, sigma, lam=initialization()
    n=[10, 20, 50, 100, 1000]
    uniform_mean = np.zeros(5)
    uniform_var = np.zeros(5)
    expon_mean = np.zeros(5)
    expon_var = np.zeros(5)
    norm_mean = np.zeros(5)
    norm_var = np.zeros(5)
    for i in range(5):
        uniform_mean[i], uniform_var[i], _ = uniform_distribution(n[i], a, b)
        # экспоненциальное распределение
        expon_mean[i], expon_var[i], _ = exponential_distribution(n[i], lam)
        # нормальное распределение
        norm_mean[i], norm_var[i], _ = normal_distribution(n[i], mu, sigma)

    def plot_(n, means, variances, methode):
        true_mean, true_var, _ = methode
        # Графики оценок
        plt.plot(n, means, label="математическое ожидание 4 задания")
        plt.plot(n, [true_mean] * len(n), label="математическое ожидание 2 задания")
        plt.xlabel("n")
        plt.ylabel("математическое ожидание")
        plt.legend()
        plt.show()

        plt.plot(n, variances, label="дисперсия 4 задания")
        plt.plot(n, [true_var] * len(n), label="дисперсия 2 задания")
        plt.xlabel("n")
        plt.ylabel("дисперсия")
        plt.legend()
        plt.show()
    print("Равномерное распределение:")
    print("N",n)
    print("математическое ожидание:", uniform_mean)
    print("дисперсия:", uniform_var)
    plot_(n, uniform_mean, uniform_var, uniform_distribution(10000,a,b))

    print("Экспоненциальное распределение:")
    print("N",n)
    print("математическое ожидание:", expon_mean)
    print("дисперсия:", expon_var)
    plot_(n, uniform_mean, uniform_var, exponential_distribution(10000,lam))

    print("Нормальное распределение:")
    print("N",n)
    print("математическое ожидание:", norm_mean)
    print("дисперсия:", norm_var)
    plot_(n, uniform_mean, uniform_var, normal_distribution(10000,mu,sigma))

def task5():
    #инициализация параметров
    n, a, b, mu, sigma, lam=initialization()
    _,_,sample_uniform=uniform_distribution(n,a,b)
    _,_,sample_expon=exponential_distribution(n,lam)
    _, _, sample_norm = normal_distribution(n,mu,sigma)
    k=int(1+3.2*math.log(n))
    def build_hist(sample,k):
        # Построение диаграммы накопленных частот
        plt.hist(sample, bins=k, cumulative=True, density=True)
        plt.title('Cumulative frequency diagram')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.show()

        # Построение гистограммы распределения
        plt.hist(sample, bins=k, density=True)
        plt.title('Distribution histogram')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.show()
    build_hist(sample_uniform,k)
    build_hist(sample_expon,k)
    build_hist(sample_norm,k)

def task6():
    # генерация выборки из равномерного распределения
    sample = np.random.normal(0,1, size=1000)

    # задание теоретического распределения
    x=np.linspace(0-3*1,0+3*1,1000)
    pdf = norm.pdf(x, loc=0, scale=1)
    cdf = norm.cdf(x, loc=0, scale=1)
    k = int(1 + 3.2 * math.log(500))
    # построение гистограммы и функции распределения на одном графике
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    ax[0].hist(sample, bins=k, density=True, alpha=0.5)
    ax[0].plot(x, pdf, 'r', linewidth=2)
    ax[0].set_title('PDF')
    ax[1].hist(sample, bins=k, density=True, cumulative=True, alpha=0.5)
    ax[1].plot(x, cdf, 'r', linewidth=2)
    ax[1].set_title('CDF')
    plt.show()

#task1()
#task2()#метод суммирования
#task3()
#task4()
#task5()
#task6()
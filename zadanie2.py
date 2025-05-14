from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Задание 1
mu = 7
sigma = 4
x = np.linspace(mu - 5*sigma, mu + 5*sigma, 1000)
f_x = (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-((x-mu)**2)/(2*sigma**2))
plt.plot(x, f_x)
plt.show()

# Задание 2
mu = 7
sigma = 4
x = np.linspace(mu - 5*sigma, mu + 5*sigma, 1000)
f1 = (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-((x-mu)**2)/(2*sigma**2))
f2 = f1 * 1 + 0.015
plt.plot(x, f1, label='Точная функция')
plt.plot(x, f2, label='Приближенная функция')
plt.legend()
plt.show()

# Задание 3
num_plots = 10
points = 100
for i in range(num_plots):
    y = np.random.uniform(-1, 1, points)
    plt.plot(y, label=f'График {i+1}')
plt.legend()
plt.show()

# Задание 4
data = pd.read_csv('day.csv')
plt.bar(data['Мероприятие'], data['Время'])
plt.title('Распределение времени по мероприятиям')
plt.show()

plt.pie(data['Время'], labels=data['Мероприятие'])
plt.title('Доля времени на каждое мероприятие')
plt.show()

# Задание 5
mu = 0
sigma = 1
size = 100
data = np.random.normal(mu, sigma, size)

plt.subplot(1, 2, 1)
plt.hist(data)

plt.subplot(1, 2, 2)
plt.boxplot(data)
plt.show()

plt.hist(data)
plt.savefig('histogram.png')
plt.close()

# Задание 6
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)
equation = X**2 - 3*X*Y + Y**2 + X + 2*Y + 5
plt.contour(X, Y, equation, levels=[0])
plt.show()

# Задание 7
def f1(value): return value + 3
def f2(value): return value**2 - 2*value + 1
def f3(value): return 0.5*value**3 - 3*value**2 + value + 4
def f4(value): return -0.2*value**4 + value**3 - 2*value + 5
L = [f1, f2, f3, f4]

x = np.linspace(-5, 5, 200)
for i in range(4):
    plt.subplot(2, 2, i+1)
    y = L[i](x)
    plt.plot(x, y)
plt.show()

# Задание 8
matrix = np.random.randint(0,100,size=(50,2))
for i in range(len(matrix)):
    if i % 2 == 0:
        plt.scatter(matrix[i,0], matrix[i,1], color='red')
    else:
        plt.scatter(matrix[i,0], matrix[i,1], color='blue')
plt.show()

# Задание 9
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = X * Y - X**2 + Y

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
plt.show()
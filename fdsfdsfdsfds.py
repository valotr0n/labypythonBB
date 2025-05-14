import numpy as np
# Задание 1

natNumbArray = np.arange(1, 11)
arr2d = natNumbArray.reshape(2, 5)
print("Двумерный массив: \n", arr2d)

# Задание 2

matrix1 = np.array([[2, 1, 1], [2, 1, 5], [2, 3, 3]])
matrix2 = np.array([[1, 3, 4], [2, 4, 6], [2, 5, 1]])
matrix_sum = matrix1 + matrix2
print("\nСумма Матриц:\n", matrix_sum)

# Задание 3

matrix4x4 = np.arange(16).reshape(4, 4)
sliceCols = matrix4x4[:, 1:3]
print("\nСрез столбцов:\n", sliceCols)

# Задание 4

randomArray = np.random.rand(5,5)
meanValue = randomArray.mean()
print("\nСреднее значение:", meanValue)


# Задание 5

matrix5x5 = np.random.rand(5,5)
maxValue = matrix5x5.max()
minValue = matrix5x5.min()
maxIndex = np.unravel_index(matrix5x5.argmax(), matrix5x5.shape)
minIndex = np.unravel_index(matrix5x5.argmin(), matrix5x5.shape)
print("\nMAX:", maxValue, "INDEX", maxIndex)
print("\nMIN:", minValue, "INDEX:", minIndex)

# Задание 6

ark1 = np.array([2, 3, 2, 5, 3, 7, 5])
unArr = np.unique(ark1)
print("\nУникальные:", unArr)

# Задание 7

randomArr = np.random.randint(0, 100, 20)
filtred = randomArr[randomArr > 50]
print("\nЭлементы > 50:", filtred)

# Задание 8

mat1 = np.array([[1,2], [3,2]])
mat2 = np.array([[2,4], [1,5]])
matx = np.dot(mat1, mat2)
det = np.linalg.det(matx)
print("\nОпределитель:", det)

# Задание 9
n,m = 5,6
zeroMatrix = np.zeros((n,m))
zeroMatrix[0, :1] = 1
zeroMatrix[-1, :] = 1
zeroMatrix[:, 0] = 1
zeroMatrix[:, -1] = 1
print("\nМатрица:\n", zeroMatrix)

# Задание 10

marrixxx = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
diag_sum = np.trace(marrixxx)
print("\nСумма диогонали:", diag_sum)

# Задание 11

vector = np.array([0, 5, 0, 2, 0, 1, 0])
nozeroIndex = np.nonzero(vector)
print("\nИндексы ненулевы элементов:", nozeroIndex)

# Задание 12

ar = np.array([2, 5, 7, 3, 9, 4])
rangForArray = (ar > 3) & (ar < 8)
ar[rangForArray] *= -1
print("\nСмена знака:", ar)

# Задание 13

sortedArray = np.sort(ar)
print("\nОтсортированный массив:", sortedArray)

# Задание 14

a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5, 6, 7])
common = np.intersect1d(a,b)
count = len(common)
print("\nОбщие:", common, ", Количество:", count)

# Задание 15

a = np.array([2, 6, 7, 1, 2, 9, 11])
elements = a[(a >= 5) & (a <= 10)]
print("\nЭлементы в диапозоне от 5 до 10:", elements)

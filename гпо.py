import numpy as np
import cv2 as cv
X= cv.imread('C:/imgs/image.jpg')
X=cv.cvtColor(X, cv.COLOR_BGR2GRAY)
#cv.imshow('image', X)
#cv.waitKey()
#h = float(input('введите размер маски = '))  # вводимое значение (нечетное)
#A1 = input('введите коэффициент для подъема = ')  # коэффициент для подъема центральной апертуры
#A2 = input('введите увеличения центрального элемента = ')  # коэффициент для увеличения центрального элемента матрицы на заданное значение

h = 7
A1 = 7
A2 = 7
# —— РЕЦИРКУЛЯТОРЫ —--
t1 = 3  # начальное значение
k = (h - t1) / 2  # разница между полученным и начальным
t1 = t1 + k  # результат строчного рециркулятора
t2 = t1 - 2  # результат кадрового рециркулятора
p = int(t1)
# ---------— ОСНОВНАЯ МАТРИЦА —----------
Y1 = np.ones((1, p))  # Строчный рециркулятор при М=5
i1 = np.size(X, 1)  # количесвто стобцов в Х матрице
j1 = np.size(X, 0) # количество строк в X матрице
i2 = np.size(Y1, 1)  # колчиество столбцов во Y2 матрице
j2 = np.size(Y1, 0)  # количество строк во Y2 матрице
nuliki = np.zeros ((j1, i2-1))
X1 = np.hstack((X, nuliki))
k = j1
m = i1 + (i2 - 1)
y1 = np.zeros((k, m))
for k in range(0, j1):
    for m in range(0, (i1 + (i2 - 1))):
        if m == 0:
            y1[k,m] = X1[k,m]
        if m > 0 and m < i2:
            y1[k,m] = X1[k,m] + y1[k,m-1]
        if m - i2 >= 0:
            y1[k,m] = X1[k,m] - X1[k,m-i2] + y1[k,m-1]
p1 = int(t2)
Y2 = np.ones((1, p1))  # Строчный рециркулятор при М=3
i1 = np.size(y1, 1)  # количесвто стобцов в у2 матрице
j1 = np.size(y1,0)  # количество строк в у2 матрице
i2 = np.size(Y2, 1)  # колчиество столбцов во Y3 матрице
j2 = np.size(Y2, 0)  # количество строк во Y3 матрице
nuliki2 = np.zeros ((j1, i2-1))
X2 = np.hstack((y1, nuliki2))
k = j1
m = i1 + (i2 - 1)
y2 = np.zeros((k, m))
for k in range(0, j1):
    for m in range(0, (i1 + (i2 - 1))):
        if m == 0:
            y2[k,m] = X2[k,m]
        if m > 0 and m < i2:
            y2[k,m] = X2[k,m] + y2[k,m-1]
        if m - i2 >= 0:
            y2[k,m] = X2[k,m] - X2[k,m-i2] + y2[k,m-1]
Y3 = np.ones((p, 1))  # кадровый рециркулятор при М=5
i1 = np.size(y2, 1)  # количесвто стобцов в у3 матрице
j1 = np.size(y2, 0)  # количество строк в у3 матрице
i2 = np.size(Y3, 1)  # колчиество столбцов во Y4 матрице
j2 = np.size(Y3, 0)  # количество строк во Y4 матрице
X3 = np.zeros((j1 + (j2 - 1), i1))  # матрица нулевая
X3 = np.pad(y2, (1, j1-1))
k = j1 + (j2 - 1)
m = i1
y3 = np.zeros((k, m))
for k in range(0, (j1 + (j2 - 1)-1)):  # выбор строки обработки
    for m in range(0, i1-1):  # выбор стлобца обработки
# условие когда выходное изображение еще не сформированно
        if k == 0:
            y3[k,m] = X3[k,m]
# задержка равна 0 имеется только входное и выходное значение
        if k > 0 and k < j2:
            y3[k,m] = X3[k,m] + y3[k-1,m]
# Общее уравнение рциркулятора
        if k - j2 >= 0:
            y3[k,m] = X3[k,m] - X3[k-j2,m] + y3[k-1,m]
Y4 = np.ones((p1, 1))  # Кадровый рециркулятор при М=3
i1 = np.size (y3, 1)  # количесвто стобцов в у4 матрице
j1 = np.size(y3, 0)  # количество строк в у4 матрице
i2 = np.size(Y4, 1)  # колчиество столбцов во Y5 матрице
j2 = np.size(Y4, 0)  # количество строк во Y5 матрице
X4 = np.zeros((j1 + (j2 - 1), i1))  # матрица нулевая
X4 = np.pad(y3, (1,j1-1))
k = j1 + (j2 - 1)
m = i1
y4 = np.zeros((k, m))
for k in range(0, (j1 + (j2 - 1)-1)):  # выбор строки обработки
    for m in range(0, i1-1):  # выбор стлобца обработки
# условие когда выходное изображение еще не сформирова
        if k == 0:
            y4[k,m] = X4[k,m]
# задержка равна 0 имеется только входное и выходное значение
        if k > 0 and k < j2:
            y4[k,m] = X4[k,m] + y4[k-1,m]
# Общее уравнение рециркулятора
        if k - j2 >= 0:
            y4[k,m] = X4[k,m] - X4[k-j2,m] + y4[k-1,m]
S1 = sum(y4)  # сумма каждого столбца первой матрицы
S1 = sum(S1, 2)  # сумма всех элементов первой матрицы
# ----------------------— КОЭФФИЦИЕНТ СДВИГА —-----------
k = h + 1  # приведение к четности

if k % 4 == 0:  # если делится без остатка на 4
    q = k / 4  # то поделить на 4, это будет ответ
else:
    q = (k + 2) / 4  # если не делится на 4, то привести к возможности деления и поделить
q1 = q + 1
# ----------------------— РАЗМЕР ВНУТРЕННЕЙ МАТРИЦЫ —-----
if t2 % 2 == 0:  # если делится без остатка на 2
    p3 = t2 - 1
else:
    p3 = t2  # если не делится на 2, то привести к возможности деления и поделить
# ---------------------СР и КР для внутренней маски---------
k = h + 1  # приведение к четности
if k % 4 == 0:  # если делится без остатка на 4
    t3 = k / 4  # то поделить на 4, это будет ответ
else:
    t3 = (k - 2) / 4  # если не делится на 4, то привести к возможности деления и поделить
# -------------------------ДОП МАТРИЦА---------------------
R = 1
p2 = int(t3)
for u in range(0, 1):
    Y5 = np.ones((1, p2))  # Строчный рециркулятор при М=2
X5 = X * R  # Множитель из структурной схемы к которому Добавляеся коэффициент А1
i1 = np.size(X5, 1)  # количесвто стобцов в Х0 матрице
j1 = np.size(X5, 0)  # количество строк в X0 матрице
i2 = np.size(Y5, 1)  # колчиество столбцов во Y0 матрице
j2 = np.size(Y5, 0)  # количество строк во Y0 матрице
nuliki5 = np.zeros ((j1, i2-1))
X5 = np.hstack((X5, nuliki5)) #Матрица Х0 дополненая нулями с правой стороны
k = j1
m = i1 + (i2 - 1)
y5 = np.zeros((k, m))
for k in range(0, j1):  # выбор строки обработки
    for m in range(0, i1 + (i2 - 1)):  # выбор стлобца обработки
# условие когда выходное изображение еще не сформированно
        if m == 0:
            y5[k,m] = X5[k,m]
# задержка равна 0 имеется только входное и выходное значение
        if m > 0 and m < i2:
            y5[k,m] = X5[k,m] + y5[k,m-1]
# Общее уравнение рециркулятора по строке
        if m - i2 >= 0:
            y5[k,m] = X5[k,m] - X5[k, m-i2] + y5[k,m-1]
Y6 = np.ones((1, p2))  # Строчный рециркулятор при М=2
i1 = np.size(y5, 1)  # количесвто стобцов в Х0 матрице
j1 = np.size(y5, 0)  # количество строк в X0 матрице
i2 = np.size(Y6, 1)  # колчиество столбцов во Y0 матрице
j2 = np.size(Y6, 0)  # количество строк во Y0 матрице
nuliki6 = np.zeros ((j1, i2-1))
X6 = np.hstack((y5, nuliki6)) #Матрица Х0 дополненая нулями с правой стороны
k = j1
m = i1 + (i2 - 1)
y6 = np.zeros((k, m))
for k in range(0, j1):  # выбор строки обработки
    for m in range(0, i1 + (i2 - 1)):  # выбор стлобца обработки
# условие когда выходное изображение еще не сформированно
        if m == 0:
           y6[k,m] = X6[k,m]
# задержка равна 0 имеется только входное и выходное значение
        if m > 0 and m < i2:
           y6[k,m] = X6[k,m] + y6[k,m-1]
# Общее уравнение рециркулятора по строке
        if m - i2 >= 0:
           y6[k,m] = X6[k,m] - X6[k,m-i2] + y6[k,m-1]
Y7 = np.ones((p2, 1))  # Кадровый рециркулятор при М=2
i1 = np.size(y6, 1)  # количесвто стобцов в у0 матрице
j1 = np.size(y6, 0)  # количество строк в у0 матрице
i2 = np.size(Y7, 1)  # колчиество столбцов во Y1 матрице
j2 = np.size(Y7, 0)  # количество строк во Y1 матрице
X7 = np.zeros((j1 + (j2 - 1), i1))  # матрица нулевая
X7 = np.pad(y6, (1, j1-1))
k = j1 + (j2 - 1)
m = i1
y7 = np.zeros((k, m))
for k in range(0, (j1 + (j2 - 1)-1)):  # выбор строки обработки
    for m in range(0, i1-1):  # выбор стлобца обработки
# условие когда выходное изображение еще не сформированно
        if k == 0:
            y7[k,m] = X7[k,m]
# задержка равна 0 имеется только входное и выходное значение
        if k > 0 and k < j2:
            y7[k,m] = X7[k,m] + y7[k-1,m]
# Общее уравнение кадрового рециркулятора
        if k - j2 >= 0:
            y7[k,m] = X2[k,m] - X7[k-j2,m] + y7[k-1,m]
Y8 = np.ones((p2, 1))  # Кадровый рециркулятор при М=2
i1 = np.size(y7, 1)  # количесвто стобцов в у0 матрице
j1 = np.size(y7, 0)  # количество строк в у0 матрице
i2 = np.size(Y8, 1)  # колчиество столбцов во Y1 матрице
j2 = np.size (Y8, 0)  # количество строк во Y1 матрице
X8 = np.zeros((j1 + (j2 - 1), i1))  # матрица нулевая
X8 = np.pad(y7, (1,j1-1))
k = j1 + (j2 - 1)
m = i1
y8 = np.zeros((k, m))
for k in range(0, (j1 + (j2 - 1)-1)):  # выбор строки обработки
    for m in range(0, i1-1):  # выбор стлобца обработки
# условие когда выходное изображение еще не сформированно
        if k == 0:
            y8[k,m] = X8[k,m]
# задержка равна 0 имеется только входное и выходное значение
        if k > 0 and k < j2:
            y8[k,m] = X8[k,m] + y8[k-1,m]
# Общее уравнение кадрового рециркулятора
        if k - j2 >= 0:
            y8[k,m] = X8[k,m] - X8[k-j2,m] + y8[k-1, m]
S0 = sum(y8)  # сумма каждого столбца
S0 = sum(S0, 2)  # сумма всех элементов матрицы
if u == 0:
    A = S1 / S0
A = round(A)
R = A
u = 1
i1 = np.size(y8,1)  # кол-во столбцов в у8
j1 = np.size(y8,0) # кол-во строк в у8
number1 = int(q1 + j1 - 1)
number2 = int(q1 + i1 - 1)
Z1 = np.zeros((number1, number2))  # нулевая матрица размером внешней
Z1 = y8  # итоговая матрица
# -----------------------ПОДЪЕМ ЦЕНТРА---------------------
p4 = int(p3)
Y9 = np.ones((1, p4))  # вид СР
X9 = np.array([[A1], ])
i1 = np.size(X9, 1)   # кол-во столбцов в Х8 матрице
j1 = np.size(X9, 0)  # кол-во строк в X8 матрице
i2 = np.size(Y9, 1)  # кол-во столбцов в Y8 матрице
j2 = np.size(Y9, 0)
nuliki9 = np.zeros ((j1, i2-1))
X9 = np.hstack((X9, nuliki9))
k = j1  # кол-во строк в Y8 матрице
m = i1 + (i2-1)
y9 = np.zeros((k,m))
for k in range(0, j1):  # выбор строки
    for m in range(0, (i1+(i2-1))):  # выбор столбца
        if m == 0:
            y9[k,m] = X9[k,m]
        if m > 0 and m < i2:
            y9[k,m] = X9[k,m] + y9[k,m - 1]
        if m - i2 >= 0:
            y9[k,m] = X9[k,m] - X9[k, m-i2] + y9[k, m-1]
Y10 = np.ones((p4, 1))  # вид КР
i1 = np.size(y9, 1)  # кол-во столбцов в у8 матрице
j1 = np.size(y9, 0)  # кол-во строк в у8 матрице
i2 = np.size(Y10, 1)  # кол-во столбцов в Y9 матрице
j2 = np.size(Y10, 0)  # кол-во строк в Y9 матрице
X10 = np.zeros((j1 + (j2 - 1), i1)) # нулевая матрица
X10 = np.pad(y9, (1, j1-1))
k = j1 + (j2 - 1)
m = i1
y10 = np.zeros((k, m))
for k in range(0, (j1 + (j2 - 1)-1)):  # выбор строки
    for m in range(0, i1-1):  # выбор столбца
        if k == 0:
            y10[k,m] = X10[k,m]
        if k > 0 and k < j2 :
            y10[k,m] = X10[k,m] + y10[k-1,m]
        if k - j2 >= 0:
            y10[k,m] = X10[k,m] - X10[k-j2, m] + y10[k-1, m]
i1 = np.size(y10, 1)  # кол-во столбцов в у9
j1 = np.size(y10, 0)  # кол-во строк в у9
Z3 = np.zeros(h) # нулевая матрица размером внешней
g = int(q1+j1-1)
g1 = int(q1+j1-1)
Z3 = np.pad(y10, (g, g1)) # итоговая матрица
# -----------------------КОНЕЧНЫЕ ВЫЧИСЛЕНИЯ---------------
A3 = S1 - S0
W = X*A2+int(A3)  # Исходное изображение домноженное на цоэффициент А2
i1 = np.size(W,1)  # количесвто стобцов в W матрице
j1 = np.size(W, 0)  # количество строк в W матрице
q2 = t2 + 1
W0 = np.zeros((j1+ (h- 1), i1+ (h- 1)))  # Нулевая матрица
g2 = int(q2+j1-1)
g3 = int(q2+j1-1)
W0 = np.pad(W, (g2, g3)) # матрица W окруженная нулями
rez = (W0+(Z1-y4+Z3))
print(rez)
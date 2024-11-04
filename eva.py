import numpy as np
number = np.array ([2,3,5,7,11])
print(number)

array_ID = np.array([2,4,5,6])
print(array_ID)

array_2D = np.array([[2,4,5,6],[2,4,5,6],[2,4,5,6]])
print(array_2D)

array_3D = np.array([[[2,4,5,6],[2,4,5,6],[2,4,5,6]]])
print(array_3D)

import numpy as np
output = np.array([[x for x in range(2,21,2)],[x for x in range(1,21,2)]])
print(output)

array = np.array([[1,2,3],[4,5,6]])
print(array)
print(array.dtype)
print(array.ndim)
print(array.shape)
print(array.size)
print(array.itemsize)
print(array>5)
print(array<=5)
print(array==5)
grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])
print(grades )
print(grades.max())
print(grades.min())
print(grades.sum())
print(grades.std())
print(grades.mean())
print(grades.var())
print(grades.mean(axis=0))
print(grades.mean(axis=1))
num1 = np.arange(1,6)
print(num1)
num2 = num1.view()
print(num2)
print(id(num1))
print(id(num2))
num2[1]*=5
print(num1)
print(num2)
num1 = np.arange(1,6)
print(num1)
num2 = num1.copy()
print(num2)
num2[2]*=5
print(num2)
print(num1)
array = np.array([1.1,2.1,3.1])
newar = array.astype("f")
print(newar)
print(newar.dtype)
score = [85,90,78,92,88]
score = np.array(score,dtype="f")
print(score)
a_score=score.copy()
print(a_score)
a_score = a_score+5
print(a_score)
shape = score.shape
ndim = score.ndim
itemsize = score.itemsize
dtype = score.dtype
sorted_score = np.sort(score)
include_80_pluse = np.where(score >= 80)
max_score = np.max(score)
min_score = np.min(score)
std_score = np.std(score)
var_score = np.var(score)
sum_score = np.sum(score)
mean_score = np.mean(score)
print("score[:2]:",score[:2])
print("score[3:-1]:",score[3:-1])
print("score[1:4]:",score[1:4])
















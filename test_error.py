import numpy as np
from sklearn import linear_model

import math

A = [11.0, 23.5, 32.8, 42.2, 65.0, 87.7, 103.9, 116.2, 123.8, 102.0, 79.4, 59.7, 45.7, 27.0]
b = [9.8, 16.9, 20.9, 25.4, 34.1, 39.9, 44.9, 57.3, 60.2, 56.9, 48.8, 34.7, 21.5, 12.1]
xx = A
yy = b
#Tính bằng công thức
#Minh đã kiểm tra lại tổng số lỗi
x_min = min(A)
x_max = max(A)

A = np.array([A]).T
b = np.array([b]).T

lr = linear_model.LinearRegression()
lr.fit(A,b)

a = lr.coef_[0][0]
b = lr.intercept_[0]


list_predic = []

for i in range(len(xx)):
	y = xx[i]*a + b
	list_predic.append(y)

intit = 0

for i in range(len(yy)):
	intit += abs(yy[i] - list_predic[i])*10 + 50

print(intit)





# print(lr.coef_[0][0],lr.intercept_[0])
# y0 = x_min*lr.coef_[0][0] + lr.intercept_[0]
# y = x_max*lr.coef_[0][0] + lr.intercept_[0]





# print(a,b)



# A = np.array([x]).T
# b = np.array([y]).T
# x0 = [x_min,y_min]
# ones = np.ones((A.shape[0],1), dtype=np.int8)
# A = np.concatenate((A, ones), axis =1)
# x = 


# print(len(X), len(Y))
# print(x_min,x_max)
# print(x)


import numpy as np
import matplotlib.pyplot as plt

index_list = [70.4, 70, 69.7, 69.5, 69.4, 69.3, 69, 68.7, 68.7, 68.9, 69, 69, 69.3, 69.5, 69.7, 69.7, 69.7, 69.7, 69.8, 69.9, 70.3, 70.7, 70.9, 71, 71.1, 71.3, 71.7, 72.1, 72.4, 72.7, 73.1, 73.3, 73.6, 73.9, 74.2, 
74.3, 74.3, 74.2, 74.1, 74.1, 74.2, 74.3, 74.4, 74.5, 74.6, 75, 75.2, 75.2, 75.1, 75.1, 75.2, 75.2, 75.4, 75.7, 75.9, 76.2, 76.3, 76.5, 76.8, 77.1, 77.6, 78.1, 78.6, 78.8, 78.9, 78.9, 79, 79.2, 79.9, 80.2, 80.3, 80.3, 
80.2, 80, 79.9, 79.5, 79.3, 79.2, 79.2, 79.2, 79.4, 79.7, 80.1, 81, 81.8, 82.5, 84.2, 85.1, 85.6, 86.3, 87.5, 88.1, 88.8, 89.3, 90.1, 91.2, 92.6, 94.1, 95.6, 97, 98.2, 100, 101.5, 103.1, 104.7, 106, 106.9, 107.2, 107.2, 107.1, 107, 107.1, 106.8, 106.6, 106.4, 105.8, 104.8, 103.4]

year_list = list(range(1,119))
il=np.reshape(index_list,(-1,1))
yl=np.reshape(year_list, (-1,1))
print(il)
print(yl)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


lin_reg = LinearRegression()
X_train, X_test, Y_train, Y_test = train_test_split(yl, il, random_state=1)

lin_reg.fit(X_train, Y_train)

print("b:" + str(lin_reg.intercept_[0]))  #편향(절편)
print("w:" + str(lin_reg.coef_[0][0]))       #가중치
print(lin_reg.score(X_train, Y_train)) #train set 점수
print(lin_reg.score(X_test, Y_test)) #test set 점수


line_x = np.arange(min(X_train), max(X_train), 100)
line_y = lin_reg.coef_[0][0] * line_x + lin_reg.intercept_[0]
plt.plot(line_x,line_y)



plt.scatter(yl, il, alpha=0.1)

plt.show()
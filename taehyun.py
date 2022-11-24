import numpy as np
import matplotlib.pyplot as plt

population_list = [51836239, 51744876, 51628117, 51558034, 51500029, 51447504, 51397309, 51348388, 51300095, 51250905, 51199019, 51142848, 51082971, 51018619, 50947857, 50868691, 50774771, 50660209, 50524704, 50368731, 50193281, 49998451, 49784159, 49551362]

year_list = list(range(24))
pl=np.reshape(population_list,(-1,1))
yl=np.reshape(year_list, (-1,1))
print(pl)
print(yl)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


lin_reg = LinearRegression()
X_train, X_test, Y_train, Y_test = train_test_split(yl, pl, random_state=1)

lin_reg.fit(X_train, Y_train)

print("b:" + str(lin_reg.intercept_[0]))  #편향(절편)
print("w:" + str(lin_reg.coef_[0][0]))       #가중치
print(lin_reg.score(X_train, Y_train)) #train set 점수
print(lin_reg.score(X_test, Y_test)) #test set 점수


line_x = np.arange(min(X_train), max(X_train), 10)
line_y = lin_reg.coef_[0][0] * line_x + lin_reg.intercept_[0]
plt.plot(line_x,line_y)



plt.scatter(yl, pl, alpha=0.1)

plt.show()
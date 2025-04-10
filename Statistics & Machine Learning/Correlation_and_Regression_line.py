import numpy as np
from sklearn.linear_model import LinearRegression


physics = [15,12,8,8,7,7,7,6,5,3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

x = np.array(physics).reshape(-1, 1)
y = np.array(history)



model = LinearRegression()
# this expect the input x to be two dimensional 
model.fit(x,y)

print(model.coef_[0])


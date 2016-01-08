import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from pandas.core.frame import DataFrame
from matplotlib.pyplot import plot

def myLine(data):
    size = len(data)
    bb = range(0,size);
    x = np.array(bb);
    y = data
    slope, intercept, r_value, p_value,slope_std_error = stats.linregress(x, y)
    predict_y = intercept + slope * x [size-1]
    pred_error = y[size-1] - predict_y
    degrees_of_freedom = len(x) - 2
    residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)
    return { 'y':predict_y,'k':slope, 'b':intercept,'err':pred_error,'std':residual_std_error }

data=[1,2,3.5,4.3,5.1,6.1]

res = myLine(data)

X = range(len(data))
data1 = X * res['k']+res['b']
print(res)
print(data1)

fig = plt.figure()
ax =  fig.add_subplot(1,1,1)
ax.plot(X,data)
ax.plot(X,data1)
ax.plot(0,res['b'],'o')
plt.grid(True)
plt.show()

    
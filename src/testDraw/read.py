
import numpy as np
import pylab
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.font_manager import FontProperties

fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14) 
plt.xlabel(u"横坐标xlabel",fontproperties=font)
from testDraw.myshow import myShow
data = pd.read_csv('d:/[data]/hs300.csv',index_col=0,parse_dates=True)
myShow(ax,data)
 

bx = fig.add_subplot(2, 1,2 )
data1 = pd.read_csv('d:/[data]/600848.csv',index_col=0,parse_dates=True)
 
myShow(bx,data1)

plt.show()
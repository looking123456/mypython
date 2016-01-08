'''
Created on 2015年11月30日

@author: Administrator
'''
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.font_manager import FontProperties
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14) 
plt.xlabel(u"横坐标xlabel",fontproperties=font)

data = pd.read_csv('d:/[data]/hs300.csv',index_col=0,parse_dates=True)
print(data)
spx = data['open']

spx.plot(ax=ax, style='k-')
'''
crisis_data = [
(datetime(2012,12,5),'Peak of bull market'),
(datetime(2013,12,5),'Bear Stearns Fails'),
(datetime(2014,12,5),'Lehman Bankruptcy')
]
 '''
crisis_data = [
    ('2012-12-05','看见Peak of bull market'),
    ('2013-12-05','Bear Stearns Fails'),
    ('2015-12-13','Lehman Bankruptcy')
]
#print(list(spx.index).index('2012-11-29'))
def get_price(date):
    try:
        return spx.ix[date][0] 
    except: 
        return 0
    
font123 = {'family' : 'serif',  
        'color'  : 'darkred',  
        'weight' : 'normal',  
        'size'   : 16,  
        }      
print(data.index)
for date, label in crisis_data:
    price = get_price(date) #spx.ix[date][0] 
    #aaa = spx.asfreq(date)
    if price == 0:
        continue
    print(date,' ',label,'==>',price)
    ax.annotate(label, xy=(date, price),
        xytext=(date, price+10),
        arrowprops=dict(facecolor='red'),
        horizontalalignment='left', 
        verticalalignment='top',
        fontproperties=font,
        color='darkred')

# Zoom in on 2007-2010
#ax.set_xlim(['1/1/2012', '1/1/2013'])
#ax.set_ylim([600, 1800])

ax.set_title('Important 日期 in 2008-2009 financial crisis',fontproperties=font,fontdict=font123)

plt.show()
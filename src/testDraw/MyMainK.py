import numpy as np
import math 
import pandas as pd
import matplotlib.pyplot as plt
from testDraw.mylinregress import myLine 
 
def GetStockData(code,frameTime):
    data1 = pd.read_csv('d://[data]//'+code+'.csv',index_col=0,parse_dates=True)
    data1 = data1['open']
    data1 = data1[:frameTime]
    return  data1
def Ma(data,period):
    mm = []
    datalen = len(data)
    index = 0 ;
    while index<datalen:
        if index < datalen - period:
            data_line  = data[index:index+period]
            data_line1 = np.array(data_line)
            data_line1 = np.log(data_line1)
            mm.append(np.mean(data_line1))
                     
        else :
            mm.append(np.nan)
            
        index+=1
        
    return mm
 
       
def GetKKLine(data,period):
    kk = []
    yy = []
    log_y = []
    index = 0
    datalen = len(data)
    while index<datalen:
        if index < datalen - period:
            data_line  = data[index:index+period]
            data_line1 = np.array(data_line)
            data_line1 = np.log(data_line1)

            res     = myLine(data_line1);
            yy.append(res['y'])
            detal = (math.atan(res['k'])/3.1415926)*180
            kk.append(detal)
            log_y.append(data_line1[0])
            
        else :
            yy.append(np.nan)
            kk.append(np.nan)
            log_y.append(math.log(data[index]))
        index+=1
        
    return kk,yy,log_y

FRAMETIME = 100 # 30天数据
PERIOD = 10    #  
fig  = plt.figure(figsize=(10,8))

def show_kk(ax,id,bx=0):
    data = GetStockData(id,FRAMETIME)
    mm   = Ma(data,PERIOD)
    X = data.index #range(len)
    kk,yy,log=  GetKKLine(data,PERIOD)
    ax.plot(X,kk,label = 'kk-'+id,marker ='.')
    
    if bx!=0 :
#         X1 = [ i for i in range(len(data))]
#         X1.reverse()
        l1 = bx.plot(X,log,label ='abc',marker ='o')
        l2 = bx.plot(X,yy,marker ='.')
        l3 = bx.plot(X,mm,marker ='.')
        bx.set_title(id+'Frame:%d' %FRAMETIME + 'Period:%d' %PERIOD)
#         fig.legend((l1, l2,l3), ('Line 3', 'Line 4','Line 5'), 'upper right') 
#         bx.text(X[0],log[0],'log')
#         bx.text(X[0],yy[0],'yy')
#         bx.text(X[0],mm[0],'m')

### 准备数据       
# instrumentID_600848 = '600686'
# instrumentID_hs300 = 'hs300'
# import matplotlib.dates as dates
# data_600848 = GetStockData(instrumentID_600848,frameTime)
# kk_600848,yy_600848,log_600848=  GetKKLine(data_600848,PERIOD)
# data_hs300 = GetStockData(instrumentID_hs300,frameTime)
# kk_hs300,yy_hs300,log_hs300 =  GetKKLine(data_hs300,PERIOD)
# 
# kk_hs300_1,yy_hs300_1, log_hs300_1=  GetKKLine(data_hs300,10)


####  显示

###  by date
import matplotlib.dates as dates
ax = fig.add_subplot(3,1,1)
bx = fig.add_subplot(3,1,2)
ex = fig.add_subplot(3,1,3)

ax.xaxis.set_major_locator(dates.MonthLocator()) 
ax.xaxis.set_major_formatter(dates.DateFormatter("%Y-%m-%d"))
bx.xaxis.set_major_locator(dates.MonthLocator()) 
bx.xaxis.set_major_formatter(dates.DateFormatter("%Y-%m-%d"))

ex.xaxis.set_major_locator(dates.MonthLocator()) 
ex.xaxis.set_major_formatter(dates.DateFormatter("%Y-%m-%d"))

show_kk(ex,'600848',ax)
show_kk(ex,'hs300',bx)
plt.legend(loc = 0)
plt.grid(True)
plt.show() 
print('.........end.............')

#ax.set_title(instrumentID_600848+'D:%d' %frameTime)
# ax.set_xlabel("x label")      
# ax.set_ylabel("y label")
#print(data.index)
# X1 = data_600848.index #range(len)
# ax.plot(X1,log_600848,label = 'open',marker ='.')
# ax.plot(X1,yy_600848,label = 'kline-10',marker ='.')
# 
# #ax.xaxis.set_major_locator(dates.MonthLocator()) 
# ax.xaxis.set_major_locator(dates.YearLocator()) 
# ax.xaxis.set_major_formatter(dates.DateFormatter("%Y-%m-%d"))
# #for label in ax.xaxis.get_ticklabels():   
# #    label.set_rotation(45)\
# bx = fig.add_subplot(3,1,2)
# X2 = data_hs300.index #range(len)
# bx.set_title(instrumentID_hs300+'D:%d' %frameTime)
# bx.plot(X2,log_hs300,label = 'open',marker ='.')
# bx.plot(X2,yy_hs300,label = 'kline-10',marker ='.')
# #bx.xaxis.set_major_locator(dates.MonthLocator()) 
# bx.xaxis.set_major_locator(dates.YearLocator()) 
# bx.xaxis.set_major_formatter(dates.DateFormatter("%Y-%m-%d"))
# #for label in ax.xaxis.get_ticklabels():   
# #    label.set_rotation(45)
#  
# ex = fig.add_subplot(3,1,3)
# ex.plot(X1,kk_600848,label = 'kk-600848',marker ='.')
# ex.plot(X2,kk_hs300,label = 'kk-hs300',marker ='.')
# ex.plot(X2,kk_hs300_1,label = 'kk-hs300-1',marker ='.')
# #ex.xaxis.set_major_locator(dates.MonthLocator()) 
# ex.xaxis.set_major_locator(dates.YearLocator()) 
# ex.xaxis.set_major_formatter(dates.DateFormatter("%Y-%m-%d"))
##
##  KK 
##


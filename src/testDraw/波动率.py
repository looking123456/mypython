import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from pandas.core.frame import DataFrame
import numpy as np
from tushare import datayes
 
HS300_NAME = 'd:\\[Data]\\hs300.index.csv'

def mkfilename(id):
    return 'd:\\[Data]\\'+id+'.csv'
'''
波动率  计算  n 天的 变化率情况
'''
def read_year_data(id):
    data = pd.read_csv(mkfilename(id),index_col=0,parse_dates=True)
    data1 = data.loc['20150801' :'20150301','open']
    data1.name= id
    return data1

PERIOD = 10

def diff_ris(a,base):
    if a>0 and base >0:
        return a-base
    if a<0 and base <0:
        return -(a-base)
    if a>0 and base <0:
        return a-base+30
    if a<0 and base >0:
        return a-base-30
    return np.NaN

def 强于基准波动(a,base):
    if a == np.NaN or base == np.NaN :
        return 0
    diff = 0.0
    if base < 0.01:
        diff = (a-base)/0.01
    else :
        diff = (a-base)/base 
#     if diff < 0.2:
#         diff = 0
    return diff

def diff_data(data,base):
    if len(data)!= len(base):
        return np.nan
    size = len(base)
    i = 0
    diff = [] 
    while (i<size):
        d = 强于基准波动(data[i],base[i])
        diff.append(d)
        i+=1
        
    ds =  pd.Series(diff,index=base.index)    
    ds.name = data.name
    return ds
    
        
        
        
    
def load_name(size=10):
    name = pd.read_csv(HS300_NAME,dtype=str)
    return name[0:size]
def rsi(data):
    rsi_data = []
    size = len(data)
    for d  in range(size):
        if d <size - PERIOD:
            flag = (data[d]-data[d+PERIOD])/data[d+PERIOD]
#             print('flag = %f'%flag)
#             if flag > 0:
#                 flag = np.log(flag)
#             else:
#                 flag = -flag
#                 flag = -np.log(flag)
            rsi_data.append(flag)
        else:
            rsi_data.append(np.nan)
    rs =  pd.Series(rsi_data,index=data.index)
    rs.name = data.name
    return rs        
 
        
def Volatility(id1):
    data = read_year_data(id1)
    data = np.log(data)
    rs_data = rsi(data)
#     rs_data.mean()
    return rs_data
# def Show1():    
#     fig = plt.figure()
#     ax =  fig.add_subplot(1,1,1)
#     ax.xaxis.set_major_locator(dates.MonthLocator()) 
#     ax.xaxis.set_major_formatter(dates.DateFormatter("%Y-%m"))
#     # ax.plot(data)
#     
#     
#     lst = load_name(2)
#     for id1 in lst.code:
#         Volatility(id1).plot()
#         
#     Volatility('hs300').plot(linewidth = 4,color = 'red')
#     Volatility('600601').plot()
#     Volatility('601398').plot()
#     
#     # bx =  fig.add_subplot(2,1,2)
#     # 
#     # data.plot()
#     # data1.plot();
#     plt.grid(True)
#     #plt.legend()
#     plt.show()
# 
#  
lst = load_name(1)
data_lst = {}

data_300 = read_year_data('hs300')    
data_stock = read_year_data(lst.code[0])

for id1 in lst.code:
    data = read_year_data(id1)
    rs_data = rsi(data)
    data1 = rs_data.reindex(data_300.index,method='ffill')
    data_lst[id1]= data1

data_300_rsi = rsi(data_300)

# print(data_lst)
for dd  in data_lst:
    print(data_lst[dd])
# 
fig = plt.figure()
ax =  fig.add_subplot(3,1,1)



for id1 in data_lst:
#     data_lst[id1] = diff_data(data_lst[id1],data_300_rsi)
    data_lst[id1].plot(marker='*',linestyle = '')
   
# data_300_rsi =   diff_data(data_300_rsi,data_300_rsi)   
data_300_rsi.plot(linewidth=2,color='red')     

bx = fig.add_subplot(3,1,2)
data_300.plot(linewidth=2,color='red') 

cx = fig.add_subplot(3,1,3)

cx.xaxis.set_major_locator(dates.MonthLocator()) 
cx.xaxis.set_major_formatter(dates.DateFormatter("%Y-%m-%d"))
for label in cx.xaxis.get_ticklabels():   
    label.set_rotation(180)
data_stock.plot()

plt.grid(True)
plt.legend()
plt.show()

# fig = plt.figure()
# ax =  fig.add_subplot(2,1,1)
# data_300 = Volatility('hs300')
# lst = load_name(5)
# for id1 in lst.code:
#     data = Volatility(id1)/data_300
#     data.plot()
#     
# bx =  fig.add_subplot(2,1,2)
# # data_kline = read_year_data('hs300')
# bx.xaxis.set_major_locator(dates.MonthLocator()) 
# bx.xaxis.set_major_formatter(dates.DateFormatter("%Y-%m"))
# # bx.plot(data_kline)
# 
# for id1 in lst.code:
#     data_kline = read_year_data(id1)
#     bx.plot(data_kline)
#     
#     
# 
#  
# # bx =  fig.add_subplot(2,1,2)
# # 
# # data.plot()
# # data1.plot();
# plt.grid(True)
# #plt.legend()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from pandas.core.frame import DataFrame
HS300_NAME = 'd:\\[Data]\\hs300.index.csv'

def mkfilename(id):
    return 'd:\\[Data]\\'+id+'.csv'

def read_year_data(id):
    data = pd.read_csv(mkfilename(id),index_col=0,parse_dates=True)
#     print(data) 
    data1 = data.loc['20151201' :'20150101','open']
    data1.name= id
    return data1

def load_name(size=10):
    name = pd.read_csv(HS300_NAME,dtype=str)
    return name[0:size]

         
list = load_name(20)  
# dates = pd.date_range(start='20151101', end='20151201')
dates_index = []
data_sum  = []
f = 0 ;
for i in list.code:
    data = read_year_data(i)
    if f==0 :
        f+=1
        dates_index = data.index
        data_sum = data
    else:
        data1 = data.reindex(dates_index,method='ffill')
        data_sum+=data1

data_mean = data_sum/len(list.code)
data_mean.name = 'mean'
print(data_mean)


fig = plt.figure(figsize=(14,6))
ax = fig.add_subplot(1,1,1)
ax.xaxis.set_major_locator(dates.MonthLocator()) 
ax.xaxis.set_major_formatter(dates.DateFormatter("%Y-%m"))
ax.set_xlabel("x label")      
ax.set_ylabel("y label")
for label in ax.xaxis.get_ticklabels():   
    label.set_rotation(45)

X = range(len(dates_index))
for i in list.code:
    data = read_year_data(i)
    data1 = data.reindex(dates_index,method='ffill')
    ax.plot(X,data1,'.')
    
data_hs300 = read_year_data('hs300')   
data_hs300 = data_hs300.reindex(dates_index,method='ffill')
    
ax.plot(X,data_mean,color = 'blue',linewidth = 3)

ax.plot(X,data_hs300/70,color = 'yellow',linewidth = 3)
    
# plt.legend(loc = 0)
plt.grid(True)
plt.show()
# print(data_list)

# pieces = []    
# 
# dates = pd.date_range(start='20151101', end='20151201')
# 
# for id in dates:
#     date = id.strftime('%Y-%m-%d')
#     print(date)
#     for  d  in data_list:
# #     print('..............')
#          data  = data_list[d]
#       
# #          print(data[date])
# #         print(id.strftime('%Y-%m-%d')+':['+d+']'+data[date])
#         
# #     print(data.index)
 
 
        
 
    
    
    

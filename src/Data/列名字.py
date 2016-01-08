#coding=utf-8
import tushare as ts
HS300_NAME = 'd:\\[Data]\\hs300.index.csv'

def mkfilename(id):
    return 'd:\\[Data]\\'+id+'.csv'

def save(id):
    cvsfile = "d:\\[Data]\\"+id+".csv"
    np = ts.get_hist_data(id)
    size = len(np)
    if size > 0 :
        np.to_csv(cvsfile)
        print(id+" ... save success! len = %d:" %size +cvsfile )
    else:
        print(id+" ... save faile!")   

def save_300():
    list = ts.get_hs300s()
    print(list)
    list.to_csv(HS300_NAME)
    for id in list.code:
        save(id)
    print('.........end.............')

    
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates

def read_year_data(id):
    data = pd.read_csv(mkfilename(id),index_col=0,parse_dates=True)
#     print(data) 
    data1 = data.loc['20151201' :'20150101','open']
    return data1

def load_name(size):
    name = pd.read_csv(HS300_NAME,dtype=str)
    return name[1:10]
    
def show_300_byYear(ax,list):
    cnt = 0 
    for i in list:
        data = read_year_data(i)
        ax.plot(data.index,data,'.')
        



fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.xaxis.set_major_locator(dates.MonthLocator()) 
ax.xaxis.set_major_formatter(dates.DateFormatter("%Y-%m"))
ax.set_xlabel("x label")      
ax.set_ylabel("y label")
for label in ax.xaxis.get_ticklabels():   
    label.set_rotation(45)

list =  load_name(10)  
print(list) 
show_300_byYear(ax,list.code)

plt.legend(loc = 0)
plt.grid(True)
plt.show()

read_year_data('000001')

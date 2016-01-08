'''
Created on 2015年12月16日

@author: Administrator
'''
import tushare as ts
print("Input Code:")
name = input()
cvsfile = "d:\\[Data]\\"+name+".csv"
print("save "+cvsfile)
print(name)
#np = ts.get_hist_data("\""+name+"\"") #一次性获取全部日k线数据
np = ts.get_hist_data(name)
print(np)
np.to_csv(cvsfile)
print("完成!")

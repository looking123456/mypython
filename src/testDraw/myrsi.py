import numpy as np
import pandas as pd
def GetStockData(code,frameTime):
    data1 = pd.read_csv('d://[data]//'+code+'.csv',index_col=0,parse_dates=True)
    data1 = data1['open']
    data1 = data1[:frameTime]
    return  data1


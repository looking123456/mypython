
import numpy as np
import pylab
from scipy import stats
import pandas as pd
from pandas.core.frame import DataFrame
from matplotlib.pyplot import plot
 

def myLinregree(data):
    bb = range(0,len(data));
    x = np.array(bb);
    y = data
    print("x=",x)
    print("y=",y)
    print(".........................")
    slope, intercept, r_value, p_value,slope_std_error = stats.linregress(x, y)
    predict_y = intercept + slope * x
    pred_error = y - predict_y
    degrees_of_freedom = len(x) - 2
    residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)
     
    # Plotting
    pylab.plot(x, y, '.')
    pylab.plot(x, predict_y, 'k-')
    pylab.show()
    
def showLine(hand,data):
    x = range(len(data))
    print(x)
    print(data)
    hand.plot(x,data,'k-')

        
def myLine(data):
    size = len(data)
    bb = range(0,size);
    x = np.array(bb);
    y = data
#     print("x=",x)
#     print("y=",y)
#     print(".........................")
    slope, intercept, r_value, p_value,slope_std_error = stats.linregress(x, y)
#    print("predict = ", x [size-1])
    predict_y = intercept + slope * x [size-1]
    pred_error = y[size-1] - predict_y
    degrees_of_freedom = len(x) - 2
    residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)
    return { 'y':predict_y,'k':slope, 'b':intercept,'err':pred_error,'std':residual_std_error }
    

if __name__ == '__main__' :    
    
    data1 = pd.read_csv('d://[data]//600848.csv',index_col=0,parse_dates=True)
    data1 = data1['open']
#     data1=  data1[:100]
    len1 = 100 ;
       
    kk=[]
      # print(kk)
    index = 0
    while index<len1:
        data_10 = data1[index:index+10]
        data    = np.array(data_10)
        res     = myLine(data);
    #   print("[",index,"]",res['y'])
        kk.append(res['b'])
        index+=1
      
       
    # showLine(pylab,kk)
    # showLine(pylab,data1)
    # pylab.show()
      
    from testDraw.myShowLine import MiniPlotTool
    baseConfig = {
            'figsize' : (10,4),
            #'axis': [0,10,0,10],
            'title' : 'MyTest',
            'ylabel' : 'price',
            'grid' : True,
            #'xaxis_locator' : 0.5,
            #'yaxis_locator' : 1,
            #'legend_loc' : 'upper right'
        }
    tool = MiniPlotTool(  baseConfig  )
    X = range(len(kk),0,-1)
    print(X)
    lineConf2 = {
            'X' : X,
            'Y' : data1[:100],
            'marker' : '.',
            'color' : 'r',
            'markerfacecolor' : 'r',
            'label' : 'open price',
            'linewidth' : 1,
            'linestyle' : '-'         
        }
      
    lineConf1 = {
            'X' : X,
            'Y' : kk,
            'marker' : '.',
            'color' : 'b',
            'markerfacecolor' : 'b',
            'label' : 'k_10',
            'linewidth' : 1,
            'linestyle' : '-'         
        }
    tool.addline(lineConf2)
    tool.addline(lineConf1)
       
    tool.plot()
    tool.show()

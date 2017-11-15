import numpy as np
import math
import decimal
import time
import matplotlib.pyplot as plt




def dataStatistics(data, statistic):
    result=0
    if statistic == 'Mean Temperature':

        a = np.mean(data,axis=0)
        result= a[0]


    elif statistic == 'Mean Growth rate':
        a = np.mean(data, axis=0)
        result = a[1]
    elif statistic == 'Std Temperature':
        a = np.std(data, axis=0)
        result = a[0]
    elif statistic == 'Std Growth rate':
        a = np.std(data, axis=0)
        result = a[1]
    elif statistic == 'Rows':
        a = np.shape(data)
        result = a[0]
    elif statistic == 'Mean Cold Growth rate':
        sum=0
        n=0

        for i in range(np.shape(data)[0]):
            if data[i][0]<20:
                sum=sum+data[i][1]
                n=n+1
        result=sum/n
    elif statistic == 'Mean Hot Growth rate':
        sum=0
        n=0

        for i in range(np.shape(data)[0]):
            if data[i][0]>50:
                sum=sum+data[i][1]
                n=n+1
        try:
            result=sum/n
        except ZeroDivisionError:
            print("division by zero!")
            result=None

    return result


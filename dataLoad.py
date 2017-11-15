import numpy as np
import math
import decimal
import time
import matplotlib.pyplot as plt





def dataLoad(filename):

    with open(filename) as f:

        new_data=np.array([0,0,0])
        for a_line in f:
            word = a_line.split(' ')
            data = np.array([float(word[0]),float(word[1]),float(word[2])])

            new_data = np.vstack((new_data,data))

    data = new_data

    new_array = np.array([0, 0, 0])
    number_of_rows = data.shape[0]
    for i in range(number_of_rows):
        if data[i][0] < 10 or data[i][0] > 60:
            if  i==0:
                continue

            print("error type: temperature in line", i)
            continue


        if data[i][1] < 0:

            print("error type:  growth rate in line", i)
            continue
        if not (data[i][2]==1 or data[i][2]==2 or data[i][2]==3 or data[i][2]==4):
            print("error type: bacteria type in line",i)
            continue
        else:
            new_array = np.vstack((new_array, data[i]))
    new_array=np.delete(new_array,0,0)
    return new_array
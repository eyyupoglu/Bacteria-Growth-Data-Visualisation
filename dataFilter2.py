import numpy as np
import math
import decimal
import time
import matplotlib.pyplot as plt

from dataLoad import *

def dataFilter2(data, bacteriaFilter, growthRatefilter):

    GrowthRate = data[:,1]
    Bacteria_type = data[:,2]

    logical_vector=np.ones(len(data),dtype=bool)

    if bacteriaFilter != None:
        logical_vector=logical_vector & (Bacteria_type==bacteriaFilter)

    if growthRatefilter!=None:
        logical_vector=logical_vector & (GrowthRate<=growthRatefilter[1]) & (GrowthRate>=growthRatefilter[0])


    return data[logical_vector,:]

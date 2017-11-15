import numpy as np
import math
import decimal
import time
import matplotlib.pyplot as plt
from dataPlot import *
from dataStatistics import *
from dataLoad import *
from dataFilter2 import *
def main():
    def load():
        data=[]
        filename = input("The name of the file name is necessary(with correct extension) :\n>>")
        try:
            data = dataLoad(filename)
        except:
            print("ERROR: Invalid filename or extension\n it should end with \" .txt \"")
            time.sleep(2)
        return data

    ongoing_data = []
    button = ''
    filter_situation = "off"

    while not button=='quit':

        print(" L for loading data---- F for filter data----D for Display Statistic----- G for Generating plots")
        button = input("What would you like to do? \n>>")


        if button=="L":
            ongoing_data= load()

        elif button=="F":
            bacteria_filter =0
            growthRatefilter = [0,1]
            while True:


                filter_option = input("for filtering bacteria type please Press 1 "
                                      "\nfor filtering growth rate please Press 2\n"
                                      "Type q to quitting filter\n>>")
                if filter_option=="1":
                    bacteria_filter = int(input("Which Bacteria type do you want to get? \n\n1 for Salmonella "
                                      "\n2 for Bacillus cereus"
                                      "\n3 for Listeria"
                                      "\n4 for Brochothrix thermosphacta\n>>"))
                elif filter_option =="2":
                    growthRatefilter[0]= float(input("Type the lower bound of the interval"))
                    growthRatefilter[1]= float(input("Type the upper bound of the interval"))
                elif filter_option=="q":
                    break

            print(dataFilter2(ongoing_data,bacteria_filter,growthRatefilter))














main()
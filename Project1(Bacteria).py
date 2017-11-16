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
    data =None
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

        if data==None and np.any(button==np.array(["G","D","F"])):
            print("You need to load data first")

        elif button=="L":
            ongoing_data= load()

        elif button=="F":
            bacteria_filter =0
            growthRatefilter = [0, 1]
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


            ongoing_data= dataFilter2(ongoing_data,bacteria_filter,growthRatefilter)

        elif button=="D" :

            stat_option= input("Which statistic do you want to see\n?"
                               "1 for Mean growth rate\n"
                               "2 for Std Temperature\n"
                               "3 for std Growth Rate\n"
                               "4 for num ber of rows\n"
                               "5 for mean cold growth rate\n"
                               "6 for mean hot growth rate\n>>")

            if stat_option=="1":
                print(dataStatistics(ongoing_data, "Mean Growth rate"))
            elif stat_option=="2":
                print(dataStatistics(ongoing_data, "Std Temperature"))
            elif stat_option=="3":
                print(dataStatistics(ongoing_data, "Std Growth rate"))
            elif stat_option=="4":
                print(dataStatistics(ongoing_data, "Rows"))
            elif stat_option=="5":
                print(dataStatistics(ongoing_data, "Mean Cold Growth rate"))
            elif stat_option=="6":
                print(dataStatistics(ongoing_data, "Mean Hot Growth rate"))

        elif button=="G":
            dataPlot(ongoing_data)
















main()
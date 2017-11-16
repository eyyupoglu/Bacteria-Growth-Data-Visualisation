
import numpy as np
import math
import decimal
import time
import matplotlib.pyplot as plt
from dataPlot import *
from dataStatistics import *
from dataLoad import *
from dataFilter2 import *



def load():
    data = []
    filename = input("The name of the file name is necessary(with correct extension) :\n>>")

    try:
        data = dataLoad(filename)
        print(data)
    except:

        print("ERROR: Invalid filename or extension\n it should end with \" .txt \"")

        time.sleep(2)
    return data




def main():
    ongoing_data = []
    button = ''
    filter_situation = "off"
    bacteria_filter = None
    growthRatefilter = [0, float('inf')]
    data=[]
    data2=[]


    while not button=='quit':

        print(" L for loading data---- F for filter data----D for Display Statistic----- G for Generating plots------Q for quitting the program")
        button = input("What would you like to do? \n>>")


        if (np.any(button == np.array(["F", "G", "D"]))) and ongoing_data==[]:
            print("You gotta load data ")

        elif button=="L":
            ongoing_data= load()
            data=ongoing_data*1
            data2=data*1

        elif button=="F":

            while True:

                if bacteria_filter != 1 and bacteria_filter != 2 and bacteria_filter != 3 and bacteria_filter != 4 and growthRatefilter[0]==0 and growthRatefilter[1]==float('inf'):
                    print("--------------------------------------------------------------------")
                    print("No filter is on")

                elif bacteria_filter ==None:
                    print("bacteria type {} is on".format(bacteria_filter))
                    print("--------------------------------------------------------------------")
                # This is the part where we show the filter settings for growth rate





                filter_option = input("for filtering bacteria type please Press 1 "
                                      "\nfor filtering growth rate please Press 2\n"
                                        "for resetting the data to the raw data please Press 3\n"
                                      "Type q to return the main menu\n>>")
                if filter_option=="1":
                    try:
                        bacteria_filter = int(input("Which Bacteria type do you want to get? \n\n1 for Salmonella "
                                      "\n2 for Bacillus cereus"
                                      "\n3 for Listeria"
                                      "\n4 for Brochothrix thermosphacta\n>>"))
                    except:
                        print("You need to type in a valid bacteria type!")
                elif filter_option =="2":
                    growthRatefilter[0]= float(input("Type the lower bound of the interval"))
                    growthRatefilter[1]= float(input("Type the upper bound of the interval"))

                elif filter_option == "3":
                    bacteria_filter = None
                    growthRatefilter = [0, float('inf')]
                    ongoing_data = dataFilter2(data, bacteria_filter, growthRatefilter)

                    print("Done!\n")

                elif filter_option=="q":
                    break
                # This is the part where we show the filter settings
                if bacteria_filter != 1 and bacteria_filter != 2 and bacteria_filter != 3 and bacteria_filter != 4:
                    print("No filter is on for bacteria type")
                elif True:
                    print("bacteria type {} is on".format(bacteria_filter))
                # This is the part where we show the filter settings for growth rate
                if growthRatefilter[0]==-0.1 and growthRatefilter[1]==float('inf'):
                    print("No filter is on for growth rate")
                elif True:
                    print("growth rate filter is on from {} to {}  ".format(growthRatefilter[0],growthRatefilter[1]))



            ongoing_data= dataFilter2(data,bacteria_filter,growthRatefilter)

        elif button=="D" :

            stat_option= input("Which statistic do you want to see\n?"
                               "1 for Mean growth rate\n"
                               "2 for Std Temperature\n"
                               "3 for std Growth Rate\n"
                               "4 for number of rows\n"
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
        elif button == "Q":
            break

        #This is the part where we show the filter settings
        if bacteria_filter != 1 and bacteria_filter != 2 and bacteria_filter != 3 and bacteria_filter != 4 :
            print("No bacteria filter is on")
        elif True:
            print("bacteria type {} is on".format(bacteria_filter))
        else:
            print("Not a valid input please choose L or G or D or F")

















main()
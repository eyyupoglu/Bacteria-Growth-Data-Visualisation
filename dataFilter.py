import numpy as np
import math
import decimal
import time
import matplotlib.pyplot as plt

from dataLoad import *



def filter(data):
    if data == []:
        print("ERROR: Data has not been loaded yet. You need to load a data first.")
        filtered_data = []

    else:
        filtered_data = data
        # Up to this point we checked the errors. Now we can filter with if else s
        filter_option = input("What kind of filter do you want to use?\n 1 for bacteria type -------2 for "
                              "Growth Rate filter\n>>")
        if filter_option == "1":
            bacteria_type = input("Which Bacteria type do you want to get? \n\n1 for Salmonella "
                                  "\n2 for Bacillus cereus"
                                  "\n3 for Listeria"
                                  "\n4 for Brochothrix thermosphacta\n>>")
            if bacteria_type == "1":

                type_1 = np.array([0, 0, 0])
                counter = 0
                for i in range(len(data[:, 2])):
                    if data[i, 2] == 1:
                        counter = counter + 1
                        type_1 = np.vstack((type_1, data[i]))
                type_1 = np.delete(type_1, 0, 0)
                filtered_data = type_1
            elif bacteria_type == "2":

                type_1 = np.array([0, 0, 0])
                counter = 0
                for i in range(len(data[:, 2])):
                    if data[i, 2] == 2:
                        counter = counter + 1
                        type_1 = np.vstack((type_1, data[i]))
                type_1 = np.delete(type_1, 0, 0)
                filtered_data = type_1
            elif bacteria_type == "3":

                type_1 = np.array([0, 0, 0])
                counter = 0
                for i in range(len(data[:, 2])):
                    if data[i, 2] == 3:
                        counter = counter + 1
                        type_1 = np.vstack((type_1, data[i]))
                type_1 = np.delete(type_1, 0, 0)
                filtered_data = type_1

            elif bacteria_type == "4":

                type_1 = np.array([0, 0, 0])
                counter = 0
                for i in range(len(data[:, 2])):
                    if data[i, 2] == 4:
                        counter = counter + 1
                        type_1 = np.vstack((type_1, data[i]))
                type_1 = np.delete(type_1, 0, 0)
                filtered_data = type_1

    return filtered_data
import numpy as np
import math
import decimal
import time
import matplotlib.pyplot as plt



def dataPlot(data):
#---------------------------------first part-----bar plot- number of bacteri--------------------------------------------
    counter = 0
    counter2=0
    counter3=0
    counter4=0

    type_1= np.array([0,0,0])
    type_2= np.array([0,0,0])
    type_3= np.array([0,0,0])
    type_4= np.array([0,0,0])

    for i in range(len(data[:,2])):
        if data[i,2]==1:
            counter=counter+1
            type_1 = np.vstack((type_1, data[i]))
        if data[i,2]==2:
            type_2 = np.vstack((type_2, data[i]))
            counter2=counter2+1
        if data[i,2]==3:
            type_3 = np.vstack((type_3, data[i]))
            counter3=counter3+1

        if data[i,2]==4:
            type_4 = np.vstack((type_4, data[i]))
            counter4=counter4+1




    plt.bar([1 ], [counter],  label="Type 1", color='g')
    plt.bar([2 ], [counter2], label="Type 2", color='r')
    plt.bar([3 ], [counter3], label="Type 3", color='b')
    plt.bar([4 ], [counter4], label="Type 4", color='y')

    plt.legend()
    plt.xlabel('Bacteria Types')
    plt.ylabel('Number of Bacteria')

    plt.title('Bacteria Type Frequency Graph')

    plt.show()





#---------------------------------second PART-----------Growth rate by temperature--------------------------------------
    try:
        plt.scatter(type_1[:,0],  type_1[:,1], color='g', s=25, marker="*", label="Salmonella enterica" )
    except:
        print("error1")

    try:

        plt.scatter(type_2[:, 0], type_2[:, 1], color='r', s=25, marker="x", label="Bacillus cereus")
    except:
        print("error2")
    try:
        plt.scatter(type_3[:, 0], type_3[:, 1], color='b', s=25, marker="^", label="Listeria")
    except:
        print("error3")
    try:
        plt.scatter(type_4[:, 0], type_4[:, 1], color='y', s=25, marker="o", label="Brochothrix thermosphacta")
    except:
        print("error4")







    plt.title("Growth Rate by Temperature")  # Set the title of the graph
    plt.xlabel("Temperature")  # Set the x-axis label
    plt.ylabel("Growth Rate")  # Set the y-axis label
    plt.axis([10, 60, 0, 1])
    plt.legend()
    plt.show()




#Created by Ertu
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scienceplots

pd.options.display.max_rows = 1000


name = "Static of what?"          #Write the name
#change this values for the wind tunnel alpha, min and max values
min = 10                            #minus value
max = 10
alphaStep = 2

# Environment Conditions
Temp = 26               #C
Pressure = 85           #kPa
Va = 8                  #m/s
rho = 0.98985
q = 0.5*rho*(Va**2)
print(q)

#Wing Calculation                   all in meter
c = 0.1
b = 0.5
WingThickness = 0.0145

S = c*b                             #total lift surfaces
                                    #total surfaces for drag

Lift = []
Drag = []
CL = []
CD = []
CLCD = []
fileiter = range(0,max+alphaStep,alphaStep)
fileiterminus = range(min,0,(-1*alphaStep))

"""
Note: Why 2 for loops ? Tradition in laboratory is 
saving minus alphas as Ae{val}. Not A-{val}. 
"""
foldername = f"{Va}m_s"
staticVal = Va
print(foldername)
for x in fileiterminus:
    df = pd.read_csv(f'Ae{x}-name{staticVal}-1.csv')
    #data_10ms_alpha0.info() #info about columns. 
    dataframe = df.iloc[: , [0, 1]].copy()
    dataframe2 = pd.DataFrame()
    print(dataframe2)
    dataframe2 =  dataframe.abs()
    print(dataframe2)
    newDataframe = dataframe2.mean(axis=0)
    #print(a0_10ms_mean_LiftDrag[0])
    #print(a0_10ms_mean_LiftDrag[1])
    Lift.append(newDataframe[0])
    Drag.append(newDataframe[1])
    DS = WingThickness + math.sin(x*math.pi/180)             # sin(alpha)
    CLval = newDataframe[0]/(q*S)
    CDval = newDataframe[1]/(q*DS)
    CL.append(CLval)
    CD.append(CDval)
    CLCD.append(CLval/CDval)

for x in fileiter:
    df = pd.read_csv(f'A{x}-name{staticVal}-1.csv')
    #data_10ms_alpha0.info() #info about columns. 

    dataframe = df.iloc[: , [0, 1]].copy()
    dataframe2 = dataframe.abs()
    newDataframe = dataframe2.mean(axis=0)
    #print(a0_10ms_mean_LiftDrag[0])
    #print(a0_10ms_mean_LiftDrag[1])
    Lift.append(newDataframe[0])
    Drag.append(newDataframe[1])
    DS = WingThickness + math.sin(x*math.pi/180)             # sin(alpha)
    CLval = newDataframe[0]/(q*S)
    CDval = newDataframe[1]/(q*DS)
    CL.append(CLval)
    CD.append(CDval)
    CLCD.append(CLval/CDval)



xAxis = [-10,-8,-6,-4,-2,0,2,4,6,8,10]                      # also xAxis can be used with range() function but this is better for now. simple and mistake-free. 
#save to CSV File. 
writeData = pd.DataFrame({
    'alpha': xAxis,
    'CL': CL,
    'CD': CD
    })
print(writeData)

SaveCSV = writeData.to_csv('{f'name'}.csv', index=False)
#end of Saving into CSV.

print(f'Lift : {Lift}')
print(f'CL : {CL}')
print("------------------")
print(f'Drag : {Drag}')
print(f'CD : {CD}')


#Plotting 
minAxis = min*-1
xAxis = range(minAxis,max+alphaStep,alphaStep)
print(type(xAxis))
print(xAxis)
print(np.array(CL))
yAxis = CL
yAxis2 = Drag

"""
with plt.style.context(['science','ieee']):
    plt.subplot(1, 2, 1)
    plt.plot(xAxis,yAxis, marker="*")
    plt.grid()
    plt.title(f"CL-alpha Title at {Va}m/s")
    plt.xlabel("alpha")
    plt.ylabel("CL")
    plt.legend(["Wind Tunnel"," XFLR5"])
    #plt.show()

    plt.subplot(1, 2, 2)
    plt.plot(xAxis,yAxis2, marker="*")
    plt.grid()
    plt.title(f"CD-alpha Title at {Va}m/s")
    plt.xlabel("alpha")
    plt.ylabel("CD")
    plt.legend("CD Value")
    plt.show()
"""


plt.subplot(1, 2, 1)
plt.plot(xAxis,yAxis, marker="*")
plt.grid()
plt.title(f"CL-alpha Graph of {name} at {Va}m/s")
plt.xlabel("alpha")
plt.ylabel("CL")
plt.legend(["CL Value"])
#plt.show()

plt.subplot(1, 2, 2)
plt.plot(xAxis,yAxis2, marker="*")
plt.grid()
plt.title(f"CD-alpha Graph of {name} at {Va}m/s")
plt.xlabel("alpha")
plt.ylabel("CD")
plt.legend(["CD Value"])
plt.show()


plt.plot(xAxis,CLCD, marker="*")
plt.grid()
plt.title(f"CL/CD {name} at {Va}m/s")
plt.xlabel("alpha")
plt.ylabel("CD")
plt.legend(["CD Value"])
plt.show()

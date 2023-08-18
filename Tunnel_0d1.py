#Created by Ertu
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 1000

#change this values for the wind tunnel alpha, min and max values
min = 14
max = 16
alphaStep = 2

# Environment Conditions
Temp = 26                 #C
Pressure = 85             #kPa
Va = 10.0                 #m/s
rho = 0.98985
q = 0.5*rho*(Va**2)
print(q)

#Wing Calculation                   all in meter
bw = 0.5                            #span of wing in meter
cw = 0.1                            #chord of wing in meter
bt = 0.176                          #span of the elevator
ct = 0.0855                         #chord of the elevator
br = 0.1                            #height of the rudder
tr = 0.0086                         #thickness of the rudder 
twing = 0.01                        #thickness of the wing
tele = 0                            #thickness of the elevator

S = bw*cw + bt*ct                   #total lift surfaces
DS = bw*twing + tele*bt + tr*br     #total surfaces for drag

Lift = []
Drag = []
CL = []
CD = []

fileiter = range(0,max+alphaStep,alphaStep)
fileiterminus = range(min,0,(-1*alphaStep))

for x in fileiterminus:
    data_10ms_alpha0 = pd.read_csv(f'./10m_s/Ae{x}-NACA6412NACA0012ER-static10-1.csv')
    #data_10ms_alpha0.info() #info about columns. 

    a0_FP = data_10ms_alpha0.iloc[: , [0, 1]].copy()
    a0_FP.abs
    a0_10ms_mean_LiftDrag = a0_FP.mean(axis=0)
    #print(a0_10ms_mean_LiftDrag[0])
    #print(a0_10ms_mean_LiftDrag[1])
    Lift.append(a0_10ms_mean_LiftDrag[0])
    Drag.append(a0_10ms_mean_LiftDrag[1])
    CLval = a0_10ms_mean_LiftDrag[0]/(q*S)
    CDval = a0_10ms_mean_LiftDrag[1]/(q*DS)
    CL.append(CLval)
    CD.append(CDval)

for x in fileiter:
    data_10ms_alpha0 = pd.read_csv(f'./10m_s/A{x}-NACA6412NACA0012ER-static10-1.csv')
    #data_10ms_alpha0.info() #info about columns. 

    a0_FP = data_10ms_alpha0.iloc[: , [0, 1]].copy()
    a0_FP.abs
    a0_10ms_mean_LiftDrag = a0_FP.mean(axis=0)
    #print(a0_10ms_mean_LiftDrag[0])
    #print(a0_10ms_mean_LiftDrag[1])
    Lift.append(a0_10ms_mean_LiftDrag[0])
    Drag.append(a0_10ms_mean_LiftDrag[1])
    CLval = a0_10ms_mean_LiftDrag[0]/(q*S)
    CDval = a0_10ms_mean_LiftDrag[1]/(q*DS)
    CL.append(CLval)
    CD.append(CDval)

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
yAxis = np.array(CL)

plt.plot(xAxis,yAxis)
plt.show()

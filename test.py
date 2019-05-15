import matplotlib.pyplot as plt #library used for plotting
import datetime

fileToOpen = 'scenario-a-cubic.log'
ipAddresses = ['172.16.11.67', '172.16.10.65']
lineValues = []

timeXVals = []
cwndYVals = []
buffYVals = []

#open file and plot cwnd and send buffer occupancy versus time
with open(fileToOpen) as f:
    for idx, line in enumerate(f):
        # lineVals = line.strip().split(",")
        lineValues.line.strip().split(",")

        #print(lineValues[idx])

        # [2] - time 
        # [3] - local host IP address
        # [5] - foreign host address
        # [8] - current cwnd
        # [21] - # of bytes in socket send buffer 

        if idx < 2:
            continue

        if lineValues[3] == ipAddresses[0]
        timeXVals.append(lineValues[2])
        cwndYVals.append(lineValues[8])
        buffYVals.append(lineValues[21])
        
        if not len(lineValues[idx]) < 2:
            if lineValues[idx][3] in ipAddresses and lineValues[idx][5] in ipAddresses:
                plotIdx = len(timeXVals)
                timeXVals.append(lineValues[plotIdx][2])    #time
                cwndYVals.append(lineValues[plotIdx][8])    #cwnd
                buffYVals.append(lineValues[plotIdx][21])   #buffer
                
plt.plot(timeXVals, cwndYVals, '-')
plt.show()
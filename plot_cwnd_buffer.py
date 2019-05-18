import matplotlib
import matplotlib.pyplot as plt #library used for plotting
import datetime

fileToOpen = 'a-cubic.log'
title = 'CUBIC - cwnd and sender buffer occupancy over time - Scenario A'
ipAddresses = ['172.16.11.67', '172.16.10.65']

lineValues = []
timeXVals = []
cwndYVals = []
buffYVals = []

startTime = 0.0

#open file and plot cwnd and send buffer occupancy versus time
with open(fileToOpen) as f:
    for idx, line in enumerate(f):
        lineValues = line.strip().split(",")

        # [2] - time 
        # [3] - local host IP address
        # [5] - foreign host address
        # [8] - current cwnd
        # [21] - # of bytes in socket send buffer 

        #skip commmented out lines
        if lineValues[0].startswith('#'):
            continue
        
        if lineValues[0] == 'o' and lineValues[3] == ipAddresses[0] and lineValues[5] == ipAddresses[1]:
            
            if startTime == 0.0:
                startTime = float(lineValues[2])

            cwndYVals.append(float(lineValues[8]))
            buffYVals.append(float(lineValues[21]))
            timeXVals.append(float(lineValues[2])-startTime)

#print(timeXVals)

# Titles/labels
plt.title(title)
plt.xlabel('Time (seconds)')
plt.ylabel('Size (bytes)')

# make x axis nice
# plt.gcf().autofmt_xdate()

# plot graphs
plt.plot(timeXVals, cwndYVals, '-', label='congestion window')
plt.plot(timeXVals, buffYVals, '-', label='buffer occupancy')

plt.legend(loc='lower right')
plt.show()
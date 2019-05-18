import matplotlib
import matplotlib.pyplot as plt #library used for plotting
import datetime

filesToOpen = ['a-vegas.log', 'c-vegas.log']
ipAddresses = ['172.16.11.67', '172.16.10.65']
title = 'CUBIC - cwnd over time'

timeXVals = []
cwndYVals = []

startTime = 0.0

for index, filePath in enumerate(filesToOpen):
    timeXVals.append([])
    cwndYVals.append([])

    #open file and plot smoothed RTT over time
    with open(filePath, 'r') as f:
        
        startTime = 0.0

        for idx, line in enumerate(f):
            lineValues = line.strip().split(",")

            # [2] - time 
            # [3] - local host IP address
            # [5] - foreign host address
            # [8] - current cwnd

            #skip commmented out lines
            if lineValues[0].startswith('#'):
                continue
            
            if lineValues[0] == 'o' and lineValues[3] == ipAddresses[0]:
                if startTime == 0.0:
                    startTime = float(lineValues[2])

                #timeXVals[index].append(datetime.datetime.fromtimestamp(float(lineValues[2])))
                timeXVals[index].append(float(lineValues[2])-startTime)
                cwndYVals[index].append(float(lineValues[8])) # current cwnd

# Titles/labels
plt.title(title)
plt.xlabel('Time')
plt.ylabel('RTT (secs)')

#print(startTime)

# make x axis nice
#plt.gcf().autofmt_xdate()

# plot graphs
plt.plot(timeXVals[0], cwndYVals[0], '-', label='Scenario A')
plt.plot(timeXVals[1], cwndYVals[1], '-', label='Scenario C')

plt.legend(loc='lower right')
plt.show()
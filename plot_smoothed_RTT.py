import matplotlib
import matplotlib.pyplot as plt #library used for plotting
import datetime

filesToOpen = ['b-vegas.log', 'c-vegas.log']
ipAddresses = ['172.16.11.67', '172.16.10.65']
title = 'Vegas - smoothed RTT over time'

timeXVals = []
RTTYVals = []

startTime = 0.0

for index, filePath in enumerate(filesToOpen):
    timeXVals.append([])
    RTTYVals.append([])

    #open file and plot smoothed RTT over time
    with open(filePath, 'r') as f:
        
        startTime = 0.0

        for idx, line in enumerate(f):
            lineValues = line.strip().split(",")

            # [2] - time 
            # [3] - local host IP address
            # [5] - foreign host address
            # [16] - smoothed RTT estimate

            #skip commmented out lines
            if lineValues[0].startswith('#'):
                continue
            
            if lineValues[0] == 'o' and lineValues[3] == ipAddresses[0] and lineValues[5] == ipAddresses[1]:
                if startTime == 0.0:
                    startTime = float(lineValues[2])

                #timeXVals[index].append(datetime.datetime.fromtimestamp(float(lineValues[2])))
                timeXVals[index].append(float(lineValues[2])-startTime)
                RTTYVals[index].append(float(lineValues[16])/(32 * 1000)) # Smoothed RTT in secs = smoothed RTT / TCP_RTT_SCLAE * HZ from SIFTR man page 

# Titles/labels
plt.title(title)
plt.xlabel('Time')
plt.ylabel('RTT (secs)')

#print(startTime)

# make x axis nice
#plt.gcf().autofmt_xdate()

# plot graphs
plt.plot(timeXVals[0], RTTYVals[0], '-', label='Scenario B')
plt.plot(timeXVals[1], RTTYVals[1], '-', label='Scenario C')

plt.legend(loc='lower right')
plt.show()
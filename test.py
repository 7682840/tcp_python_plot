import matplotlib
import matplotlib.pyplot as plt #library used for plotting
import datetime

fileToOpen = 'scenario-a-cubic.log'
ipAddresses = ['172.16.11.67', '172.16.10.65']
lineValues = []

timeXVals = []
cwndYVals = []
buffYVals = []

prevTime = 0

#open file and plot cwnd and send buffer occupancy versus time
with open(fileToOpen) as f:
    for idx, line in enumerate(f):
        # lineVals = line.strip().split(",")
        lineValues = line.strip().split(",")

        #print(lineValues[idx])

        # [2] - time 
        # [3] - local host IP address
        # [5] - foreign host address
        # [8] - current cwnd
        # [21] - # of bytes in socket send buffer 

        #skip commmented out lines
        if lineValues[0].startswith('#'):
            continue

        if lineValues[0] == 'o' and lineValues[3] == ipAddresses[0]:
            if idx == 1:
                prevTime = float(lineValues[2])
                timeXVals.append(0)
            else:
                timeXVals.append(float(lineValues[2]) - prevTime)
            cwndYVals.append(int(lineValues[8]))
            buffYVals.append(int(lineValues[21]))

print(timeXVals)

# Titles/labels
plt.title('Title')

# make x axis nice
plt.gcf().autofmt_xdate()

# plot graphs
plt.plot(timeXVals, cwndYVals, '-')
plt.plot(timeXVals, buffYVals, '-')
plt.show()
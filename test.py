import matplotlib.pyplot as plt #library used for plotting

fileToOpen = 'scenario-a-cubic.log'
ipAddresses = ['172.16.11.67', '172.16.10.65']
lineValues = []

timeXVals = []
cwndYVals = []
buffYVals = []
plotIdx = 0

#open file and plot cwnd and send buffer occupancy versus time
with open(fileToOpen) as f:
    for idx, line in enumerate(f):
        lineValues.append(line.strip().split(","))

        #print(lineValues[idx])

        # [2] - time 
        # [3] - local host IP address
        # [5] - foreign host address
        # [8] - current cwnd
        # [21] - # of bytes in socket send buffer 
        
        if not len(lineValues[idx]) < 2:
            if lineValues[idx][3] in ipAddresses and lineValues[idx][5] in ipAddresses:
                plotIdx = len(timeXVals)
                timeXVals.append(lineValues[idx][2])    #time
                cwndYVals.append(lineValues[idx][8])    #cwnd
                buffYVals.append(lineValues[idx][21])   #buffer

plt.plot(cwndYVals, 'b', buffYVals, 'r')
plt.show()
import matplotlib.pyplot as plt #library used for plotting

fileToOpen = "test.txt"
ipAddresses = ['172.16.11.67', '172.16.10.65']
lineValues = []
plotValues = []

#open file and plot cwnd and send buffer occupancy versus time
with open(fileToOpen) as f:
    for idx, line in enumerate(f):
        lineValues.append()
        lineValues[idx] = line.split(",")

        # [2] - time 
        # [3] - local host IP address
        # [5] - foreign host address
        # [8] - current cwnd
        # [21] - # of bytes in socket send buffer 
        
        if lineValues[idx][3] in ipAddresses and linValues[idx][5] in ipAddresses:
            plotValues.append(
                lineValues[idx][2],     # time 
                lineValues[idx][8],     # current cwnd
                lineValues[idx][21])    # bytes in socket send buffer




#open file
f = open(fileToOpen, "r")

#print first line
print(f.readline())

#close file
f.close()
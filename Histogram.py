
pointsPerPlot = 1024
maxTime = 1.
minFreq = 50.
maxFreq = 80.

def histogramFromData():
    ''' Creates a histogram of the data stored in data.txt '''

    # store data in a list
    file = open('data.txt')
    data = []
    for line in file.readlines():
        data.append(float(line))
    file.close()

    # model data as overlapping sine waves
    import math
    time = []
    value = []
    for point in range(pointsPerPlot):
        t = point * maxTime / pointsPerPlot
        v = 0.
        for datum in data:
            v += math.sin(t * 2 * math.pi * datum)
        time.append(t)
        value.append(v)

    # adjust min and max 
    global minFreq
    global maxFreq
    minFreq = min(data)
    maxFreq = max(data)

    # perform Fourier transform on wave model
    import Fourier
    frequency, intensity = Fourier.Transform(time, value, minFreq=minFreq, maxFreq=maxFreq)

    # plot the histogram
    import matplotlib.pyplot as plt
    plt.plot(frequency, intensity)
    plt.yticks([])

    def markTimes(times, color = 'blue'):
        for time in times:
            height = intensity[0]
            closest = math.fabs(frequency[0] - time)
            for i in range(len(frequency)):
                if math.fabs(frequency[i] - time) < closest:
                    closest = math.fabs(frequency[i] - time)
                    height = intensity[i]
            plt.plot([time, time], [0, height], color=color)

    ## mark my times
    #myTimes = [60.43,59.496,58.71,66.56,58,56.97]
    #markTimes(myTimes, 'red')
    ## mark Kim's times
    #kimsTimes = [66.831,62.72,62.47,68.69,63.94,62.65]
    #markTimes(kimsTimes, 'green')

    plt.show()

if __name__ == '__main__':
    histogramFromData()
pointsPerPlot = 1024
maxTime = 1.
minFreq = 0.
maxFreq = 100.

def Transform(times, values, minFreq=minFreq, maxFreq=maxFreq, pointsPerPlot=pointsPerPlot):
    ''' Uses the method of Fourier Transform described in the 3 Blue 1 Brown video '''

    frequency = []
    intensity = []
    import math
    for point in range(pointsPerPlot):
        f = minFreq + point * (maxFreq - minFreq) / pointsPerPlot
        frequency.append(f)
        x = 0.
        y = 0.
        for i in range(len(times)):
            x += values[i] * math.cos(times[i] * 2 * math.pi * f)
            y += values[i] * math.sin(times[i] * 2 * math.pi * f)
        intensity.append(math.sqrt(x**2 + y **2))
    return frequency, intensity

if __name__ == '__main__':
    ''' Test function '''

    import math
    time = []
    value = []
    actualFrequency = 15.
    minFreq = 0.
    maxFreq = 2. * actualFrequency
    for point in range(pointsPerPlot):
        t = point * maxTime / pointsPerPlot
        time.append(t)
        value.append(math.sin(t * 2. * math.pi * actualFrequency))

    import matplotlib.pyplot as plt
    timeSpace = plt.subplot(211)
    freqSpace = plt.subplot(212)
    timeSpace.plot(time, value)

    frequency, intensity = Transform(time, value, maxFreq=maxFreq)

    freqSpace.plot(frequency, intensity)
    plt.show()
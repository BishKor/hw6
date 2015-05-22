__author__ = 'BisharaKorkor'

import numpy as np
import matplotlib.pyplot as plt
from kernelgenerator import ggk
from exponentialsmoothing import exposmooth as exsmoo
from blindanomoly import optimalaverageanomoly as optav

cmax = np.genfromtxt('cetMax.txt')
cmin = np.genfromtxt('cetMin.txt')

cmaxy = [np.mean(i[1:13]) for i in cmax]
cminy = [np.mean(i[1:13]) for i in cmin]

bcmax = [np.mean(cmaxy[i:i+5]) for i in range(len(cmaxy)-5)]
bcmin = [np.mean(cminy[i:i+5]) for i in range(len(cmaxy)-5)]

gkmax = np.convolve(cmaxy, ggk(1.5, 7), 'valid')
gkmin = np.convolve(cminy, ggk(1.5, 7), 'valid')

exsmmax = exsmoo(cmaxy, .5)
exsmmin = exsmoo(cminy, .5)

# opt = optav(bcmax, 30)

baseline = np.mean([cmaxy[i] for i in range(90, 120)])
blmax = [i - baseline for i in cmaxy]
blbcmax = [i - baseline for i in bcmax]
blgsmax = [i - baseline for i in gkmax]
blexmax = [i - baseline for i in exsmmax]

# blmxy = [cmaxy[i] - opt[1] for i in range(len(bcmax))]

# blcmaxy = [cmaxy[i] - opt[0] for i in range(len(bcmax))]
#
# rawmax, = plt.plot([i for i in range(1878, 2015)], cmaxy, label="raw max")
# rawmin, = plt.plot([i for i in range(1878, 2015)], cminy, label="raw min")

# print len([i for i in range(1878, 2015)])
# print len(blcmaxy)

rawmax, = plt.plot([i for i in range(1878, 2015)], blmax, label="raw max")
boxcarmax, = plt.plot([i for i in range(1882, 2014)], blbcmax, label="boxcar")
gsmax, = plt.plot([i for i in range(1880, 2011)], blgsmax, label="gaussian")
exmax, = plt.plot([i for i in range(1878, 2015)], blexmax, label="exponential")
# plt.plot([i for i in range(1882, 2014)], blmxy)
plt.plot([1878, 2015], [0, 0])

# boxcarmax, = plt.plot([i for i in range(1882, 2014)], bcmax, label="boxcar")
# boxcarmin, = plt.plot([i for i in range(1882, 2014)], bcmin, label="boxcar")
# gsmax, = plt.plot([i for i in range(1880, 2011)], gkmax, label="gaussian")
# gsmin, = plt.plot([i for i in range(1880, 2011)], gkmin, label="gaussian")
# exmax, = plt.plot([i for i in range(1878, 2015)], exsmmax, label="exponential")
# exmin, = plt.plot([i for i in range(1878, 2015)], exsmmin, label="exponential")

first_legend = plt.legend(handles=[rawmax, boxcarmax, gsmax, exmax], loc=2)

# Add the legend manually to the current Axes.
# ax = plt.gca().add_artist(first_legend)

# Create another legend for the second line.
# plt.legend(handles=[rawmin, boxcarmin, gsmin, exmin], loc=6)

plt.show()
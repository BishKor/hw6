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
gkmin = np.convolve(cmaxy, ggk(1.5, 7), 'valid')

#  Do a sanity check with alpha = 0. It should be identical to original data.
exsmmax = exsmoo(cmaxy, .3)
exsmmin = exsmoo(cminy, .3)

opt = optav(bcmax, 30)

# baseline = np.mean([cmaxy[i] for i in range(90, 120)])
blcmaxy = [bcmax[i] - opt[1] for i in range(len(bcmax))]
blmxy = [cmaxy[i] - opt[1] for i in range(len(bcmax))]

# blcmaxy = [cmaxy[i] - opt[0] for i in range(len(bcmax))]

# plt.plot([i for i in range(1878, 2015)], cmaxy)
plt.plot([i for i in range(1882, 2014)], blcmaxy)
plt.plot([i for i in range(1882, 2014)], blmxy)
plt.plot([1882, 2014], [0, 0])
# plt.plot([i for i in range(1880, 2011)], gkmax)
# plt.plot([i for i in range(1878, 2015)], exsmmax)
plt.show()
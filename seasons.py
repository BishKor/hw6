__author__ = 'BisharaKorkor'

__author__ = 'BisharaKorkor'

import numpy as np
import matplotlib.pyplot as plt
from blindanomoly import optimalaverageanomoly as optav

cmax = np.genfromtxt('cetMax.txt')
cmin = np.genfromtxt('cetMin.txt')

summermax = [np.mean(i[6:9]) for i in cmax]
summermin = [np.mean(i[6:9]) for i in cmin]

wintermax = []
wintermin = []

for i in range(len(cmax)-1):
    wintermax += [np.mean(cmax[i][11:13]+cmax[i+1][1:3])]
    wintermin += [np.mean(cmin[i][11:13]+cmin[i+1][1:3])]

bcsummax = [np.mean(summermax[i:i+5]) for i in range(len(summermax)-5)]
bcsummin = [np.mean(summermin[i:i+5]) for i in range(len(summermin)-5)]
bcwinmax = [np.mean(wintermax[i:i+5]) for i in range(len(wintermax)-5)]
bcwinmin = [np.mean(wintermin[i:i+5]) for i in range(len(wintermin)-5)]

oblsx = optav(bcsummax, 30)
oblsm = optav(bcsummin, 30)
oblwx = optav(bcwinmax, 30)
oblwm = optav(bcwinmin, 30)

optsummax = [bcsummax[i] - oblsx[1] for i in range(len(bcsummax))]
optsummin = [bcsummin[i] - oblsm[1] for i in range(len(bcsummin))]
optwinmax = [bcwinmax[i] - oblwx[1] for i in range(len(bcwinmax))]
optwinmin = [bcwinmin[i] - oblwm[1] for i in range(len(bcwinmin))]

osx, = plt.plot([i for i in range(1882, 2015)], optsummax, label="Summer Max temps")
osm, = plt.plot([i for i in range(1882, 2015)], optsummin, label="Summer Min temps")
wsx, = plt.plot([i for i in range(1882, 2014)], optwinmax, label="Winter Max temps")
wsm, = plt.plot([i for i in range(1882, 2014)], optwinmin, label="Winter Min temps")

plt.plot([1878, 2015], [0, 0])

plt.legend(handles=[osx, osm, wsx, wsm], loc=2)

plt.show()
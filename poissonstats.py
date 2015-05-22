__author__ = 'BisharaKorkor'

from math import exp, pow
import numpy as np

cmin = np.genfromtxt('cetMin.txt')

cminy = [i[1:13] for i in cmin]

total=[]
for i in range(0,80,10):
    thisdecade = 0
    for k in range(i,i+10,1):
        for j in range(12):
            if cminy[k][j] < 0:
                thisdecade += 1
    total += [thisdecade]

avg = np.mean(total)
print avg

prob = exp(-avg)*pow(avg, 0)
print prob
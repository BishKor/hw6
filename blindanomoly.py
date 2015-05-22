__author__ = 'BisharaKorkor'

import random
from numpy import mean
from math import fabs

def optimalaverageanomoly(array, minlength):

    data = []

    for i in range(100):
        begin = random.randint(0, len(array)-minlength)
        end = random.randint(begin + 30, len(array))
        baseline = mean([array[j] for j in range(begin, end)])
        blarray = [array[j] - baseline for j in range(len(array))]
        anomoly = mean([blarray[j] for j in range(-15, -5)]) #  - mean([blarray[j] for j in range(0, len(array)-15)])
        data += [[anomoly, baseline, begin + 1878, end + 1878]]

    standard = 0
    optimal = []
    for i in range(len(data)):
        #  if standard < fabs(data[i][0] - .7):
        if standard < data[i][0]:
            standard = data[i][0]
            optimal = data[i]

    print optimal
    return optimal

__author__ = 'BisharaKorkor'

import random
from numpy import mean, sum
from math import fabs

def optimalaverageanomoly(array, minlength):

    data = []

    for i in range(10000):
        begin = random.randint(0, len(array)-minlength)
        end = random.randint(begin + 30, len(array))
        baseline = mean([array[j] for j in range(begin, end)])
        blarray = [array[j] - baseline for j in range(len(array))]
        anomoly = sum([blarray[j] for j in range(-15, -5)]) - sum([blarray[j] for j in range(0, len(array)-15)])
        data += [[anomoly, baseline, begin + 1878, end + 1878]]

    standard = 0
    optimal = []
    for i in range(len(data)):
        if standard < data[i][0]:
            standard = data[i][0]
            optimal = data[i]

    return optimal

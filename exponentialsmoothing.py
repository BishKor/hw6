__author__ = 'BisharaKorkor'

def exposmooth(array, alpha):

    rar = [array[0]]  #smoothed array

    for i in range(len(array)):
        rar += [alpha * array[i] + (1-alpha) * rar[i]]

    del rar[0]

    return rar
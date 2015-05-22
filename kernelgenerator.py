__author__ = 'BisharaKorkor'

from math import exp, pow, sqrt, pi

def ggk(sigma, width):
    """generate gaussian kernel"""
    return [exp(-pow((width/2 - i) / sigma, 2)/2)/(sigma * sqrt(2 * pi)) for i in range(width)]

import numpy as np


# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    exp = np.exp(L)
    sumL = sum(exp)
    res = []
    for i in exp:
        res.append(i * 1.0 / sumL)
    return res

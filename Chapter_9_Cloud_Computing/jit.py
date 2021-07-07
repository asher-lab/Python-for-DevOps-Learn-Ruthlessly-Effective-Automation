#https://barbagroup.github.io/essential_skills_RRC/numba/2/

def sum_array(inp):
    J, I = inp.shape

    #this is a bad idea
    mysum = 0
    for j in range(J):
        for i in range(I):
            mysum += inp[j, i]

    return mysum

import numpy
arr = numpy.random.random((300, 300))
sum_array(arr)
plain = %timeit -o sum_array(arr)


# now using jit
from numba import jit
sum_array_numba = jit()(sum_array)
sum_array_numba(arr)
jitted = %timeit -o sum_array_numba(arr)
plain.best / jitted.best







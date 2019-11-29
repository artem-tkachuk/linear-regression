import io
import numpy as np

def readFile(fn):
    f = open(fn, 'r')
    #+ 1 because below we add a column of x0, where each entry is 1
    m = int(f.readline()) + 1
    n = int(f.readline())

    #delete all commas
    lines = f.read().replace(",", " ")
    #spent a lot of time on StackOverflow with this line
    data = np.genfromtxt(io.StringIO(lines))
    #add x0
    data = np.insert(data, 0, 1, axis=1)

    return (data, n, m)
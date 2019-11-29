import numpy as np
import matplotlib; matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

frequency = 100000

#plotting the cost function

def init_cost(fn):
    fig = plt.figure(0, figsize=(10, 8))

    ax = fig.add_subplot(1, 1, 1)
    ax.grid()
    ax.set_ylim(-1.0, 1.0)

    # set labels
    plt.xlabel('n Times')
    plt.ylabel('J(Θ)')
    plt.title(f'"{fn}" dataset\'s cost function')

    xdata, ydata = [], []
    # ',' because we do not need the second object
    line, = ax.plot(xdata, ydata, 'r-')

    # return all the objects to train() for replotting later
    return (fig, ax, xdata, ydata, line)


def replot_cost(fig, ax, line, nTimes, xdata, ydata, k, LL):
    # get current limits
    _, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    # properly choose how to adjust the limits on both axes
    if k > xmax:
        xmax = nTimes if 2 * k > nTimes else 2 * k
    if LL > ymax:
        ymax = 1.2 * LL
    if LL < ymin:
        ymin = 1.2 * LL

    # properly adjust the limits
    ax.set_xlim(0, xmax)
    ax.set_ylim(ymin, ymax)

    # update the line datapoints
    xdata.append(k + 1)
    ydata.append(LL)
    line.set_data(xdata, ydata)

    # only replot with certain frequency (defined above)
    if k % (nTimes / frequency) == 0:
        fig.canvas.draw()
        fig.canvas.flush_events()

# Fitting the actual line to the data

def init_line(X, y, thetas):
    fig = plt.figure(1, figsize=(10,8))

    ax = fig.add_subplot(1, 1, 1)
    ax.grid()

    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Data scatterplot and a fitted line')

    xdata = X[:, 1]
    #calculate the fitted values with current parameter values
    ydata = np.matmul(X, thetas)

    #plot initial line
    line, = ax.plot(xdata, ydata, 'r-')
    #scatterplot of the data we have
    data_plot = ax.scatter(xdata, y)

    return (fig, ax, xdata, line)


def replot_line(fig, ax, xdata, line, X, thetas, k, nTimes):
    #recalculate the fitted values
    ydata = np.matmul(X, thetas)
    #update the line
    line.set_data(xdata, ydata)

    #only replot with certain frequency (defined above)
    if k % (nTimes / frequency) == 0:
        fig.canvas.draw()
        fig.canvas.flush_events()



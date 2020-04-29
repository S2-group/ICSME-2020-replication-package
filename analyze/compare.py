import sys
import numpy
import pandas
import seaborn
import matplotlib.pyplot as plt

timeMetrics = [
    'first-contentful-paint',
    'first-meaningful-paint',
    'speed-index',
    'total-blocking-time',
    'estimated-input-latency',
    'time-to-first-byte',
    'first-cpu-idle',
    'time-to-interactive',
    'network-rtt',
    'average-transfer-time',
    'median-transfer-time',
    '90th-percentile-transfer-time',
    '95th-percentile-transfer-time',
    '99th-percentile-transfer-time',
    'lowest-time-to-widget',
    'median-time-to-widget',
]

yAxixMinSize = {
    'first-contentful-paint': 0,
    'first-meaningful-paint': 0,
    'speed-index': 2000,
    'total-blocking-time': 0,
    'time-to-first-byte': 0,
    'first-cpu-idle': 0,
    'time-to-interactive': 2000,
    'lowest-time-to-widget': 0,
    'median-time-to-widget': 0,
    'estimated-input-latency': 0,
    'network-rtt': 0,
    'network-requests': 0,
    'dom-size': 2000,
    'total-transfer-size': 500000,
    'average-transfer-size': 0,
    'median-transfer-size': 0,
    '90th-percentile-transfer-size': 0,
    '95th-percentile-transfer-size': 0,
    '99th-percentile-transfer-size': 0,
    'average-transfer-time': 0,
    'median-transfer-time': 0,
    '90th-percentile-transfer-time': 0,
    '95th-percentile-transfer-time': 0,
    '99th-percentile-transfer-time': 0,
    'number-api-calls': 50,
    'lowest-time-to-widget': 0,
    'median-time-to-widget': 0,
}


# Dictionary of the max limit on the y axis for each column
yAxixMaxSize = {
    'first-contentful-paint': 5000,
    'first-meaningful-paint': 10000,
    'speed-index': 12000,
    'total-blocking-time': 15000,
    'time-to-first-byte': 150,
    'first-cpu-idle': 25000,
    'time-to-interactive': 25000,
    'lowest-time-to-widget': 10000,
    'median-time-to-widget': 10000,
    'estimated-input-latency': 1500,
    'network-rtt': 100,
    'network-requests': 300,
    'dom-size': 20000,
    'total-transfer-size': 800000,
    'average-transfer-size': 5000,
    'median-transfer-size': 1500,
    '90th-percentile-transfer-size': 5000,
    '95th-percentile-transfer-size': 25000,
    '99th-percentile-transfer-size': 50000,
    'average-transfer-time': 500,
    'median-transfer-time': 250,
    '90th-percentile-transfer-time': 500,
    '95th-percentile-transfer-time': 500,
    '99th-percentile-transfer-time': 5000,
    'number-api-calls': 300,
    'lowest-time-to-widget': 7500,
    'median-time-to-widget': 7500,
}

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('This script requires you to specify two .csv files as input. Please do so.')
        exit(1)

    Data1 = pandas.read_csv(sys.argv[1])
    Data2 = pandas.read_csv(sys.argv[2])

    for column in Data1:
        figure, ax = plt.subplots(1, 2)
        plot = seaborn.boxenplot(data=[Data1[column], Data2[column]], ax=ax[0])
        plot.set(xlabel=column, xticklabels=['Before', 'After'], ylim=(yAxixMinSize[column], yAxixMaxSize[column]))

        if column in timeMetrics:
            plot.set(ylabel='Time (ms)')
        else:
            plot.set(ylabel='Quantity')
        plot = seaborn.violinplot(data=[Data1[column], Data2[column]], ax=ax[1])
        plot.set(xlabel=column, xticklabels=['Before', 'After'], ylim=(yAxixMinSize[column], yAxixMaxSize[column]))
        ax[1].set_yticks([])
        seaborn.despine(left=False, right=True, top=True, bottom=False, ax=ax[0])
        seaborn.despine(left=True, right=True, top=True, bottom=False, ax=ax[1])


        plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.1, hspace=0.2)
        figure.savefig('../figures/' + column + '.png')
        figure.clf()
        plt.close()

    print('Done!')

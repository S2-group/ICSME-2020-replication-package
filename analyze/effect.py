from __future__ import division
import sys
import numpy
import pandas

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

metricsToUse = {
    'first-contentful-paint': 'First Contenful Paint',
    'first-meaningful-paint': 'First Meaningful Paint',
    'speed-index': 'Speed Index',
    'total-blocking-time': 'Total Blocking Time',
    'estimated-input-latency': 'Estimated Input Latency',
    'first-cpu-idle': 'First CPU Idle',
    'time-to-interactive': 'Time to Interactive',
    'network-requests': 'Network Requests',
    'dom-size': 'DOM Size',
    'lowest-time-to-widget': 'Lowest Time to Widget',
    'median-time-to-widget': 'Median Time to Widget',
}


# Source: https://github.com/neilernst/cliffsDelta/blob/master/cliffsDelta.py
def cliffsDelta(lst1, lst2, **dull):

    """Returns delta and true if there are more than 'dull' differences"""
    if not dull:
        dull = {'small': 0.147, 'medium': 0.33, 'large': 0.474} # effect sizes from (Hess and Kromrey, 2004)
    m, n = len(lst1), len(lst2)
    lst2 = sorted(lst2)
    j = more = less = 0
    for repeats, x in runs(sorted(lst1)):
        while j <= (n - 1) and lst2[j] < x:
            j += 1
        more += j*repeats
        while j <= (n - 1) and lst2[j] == x:
            j += 1
        less += (n - j)*repeats
    d = (more - less) / (m*n)
    size = lookup_size(d, dull)
    return d, size


# Source: https://github.com/neilernst/cliffsDelta/blob/master/cliffsDelta.py
def lookup_size(delta: float, dull: dict) -> str:
    """
    :type delta: float
    :type dull: dict, a dictionary of small, medium, large thresholds.
    """
    delta = abs(delta)
    if delta < dull['small']:
        return 'negligible'
    if dull['small'] <= delta < dull['medium']:
        return 'small'
    if dull['medium'] <= delta < dull['large']:
        return 'medium'
    if delta >= dull['large']:
        return 'large'


# Source: https://github.com/neilernst/cliffsDelta/blob/master/cliffsDelta.py
def runs(lst):
    """Iterator, chunks repeated values"""
    for j, two in enumerate(lst):
        if j == 0:
            one, i = two, 0
        if one != two:
            yield j - i, one
            i = j
        one = two
    yield j - i + 1, two

if __name__ == "__main__":

    Data = [
        pandas.read_csv(sys.argv[1] + '1.csv'),
        pandas.read_csv(sys.argv[1] + '2.csv'),
        pandas.read_csv(sys.argv[1] + '3.csv'),
        pandas.read_csv(sys.argv[1] + '4.csv'),
        pandas.read_csv(sys.argv[1] + '5.csv'),
        pandas.read_csv(sys.argv[1] + '6.csv'),
        pandas.read_csv(sys.argv[1] + '7.csv'),
        pandas.read_csv(sys.argv[1] + '8.csv'),
        pandas.read_csv(sys.argv[1] + '9.csv'),
        pandas.read_csv(sys.argv[1] + '10.csv'),
        pandas.read_csv(sys.argv[1] + '11.csv'),
        pandas.read_csv(sys.argv[1] + '12.csv'),
        pandas.read_csv(sys.argv[1] + '13.csv'),
        pandas.read_csv(sys.argv[1] + '14.csv'),
    ]

    for i in range(1, len(Data)):
        print("\n")
        print("Intervention " + str(i))
        previous = Data[i - 1]
        current = Data[i]
        for column in previous:
            if column in metricsToUse:
                print(column + ": " + str(
                    cliffsDelta(previous[column], current[column])))

    print('Done!')

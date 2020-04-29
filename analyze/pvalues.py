from __future__ import division
import sys
import numpy
import pandas
from scipy.stats import mannwhitneyu

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

    # Checks if all the entries in both arrays are identical
    def check_if_all_the_same(a, b):
        for i in range(min(len(a), len(b))):
            if a[i] - b[i] != 0:
                return False
        return True


    for i in range(1, len(Data)):
        print("\n")
        print("Intervention " + str(i))
        previous = Data[i - 1]
        current = Data[i]
        for column in previous:
            if column in metricsToUse and not check_if_all_the_same(previous[column], current[column]):
                print(column + ": " + str(
                    mannwhitneyu(x=previous[column], y=current[column], use_continuity=False)))

    print('Done!')


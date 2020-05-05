from __future__ import division
import sys
import numpy
import pandas
from scipy.stats import mannwhitneyu
from statsmodels.stats.multitest import multipletests

metricsToUse = [
    'first-contentful-paint',
    'first-meaningful-paint',
    'speed-index',
    'total-blocking-time',
    'estimated-input-latency',
    'first-cpu-idle',
    'time-to-interactive',
    'network-requests',
    'dom-size',
    'lowest-time-to-widget',
    'median-time-to-widget',
]

# Checks if all the entries in both arrays are identical
def check_if_all_the_same(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] - b[i] != 0:
            return False
    return True


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

    pvals = []


    for i in range(1, len(Data)):
        print("\n")
        print("Intervention " + str(i))
        previous = Data[i - 1]
        current = Data[i]
        for column in previous:
            if column in metricsToUse and not check_if_all_the_same(previous[column], current[column]):
                print(column + ": " + str(
                    mannwhitneyu(x=previous[column], y=current[column], use_continuity=False)))
                _, pval = mannwhitneyu(x=previous[column], y=current[column], use_continuity=False)
                pvals.append(pval)
    
        results = multipletests(pvals, alpha=0.05, method='fdr_bh')
        for j in range(0, len(results[1])):
            pval = results[1][j]
            print(metricsToUse[j] + ': ' + str(pval))
        pvals = []


    print('Done!')


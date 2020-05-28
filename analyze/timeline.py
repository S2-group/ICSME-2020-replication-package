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
    'first-contentful-paint': 4000,
    'first-meaningful-paint': 6000,
    'speed-index': 12000,
    'total-blocking-time': 15000,
    'time-to-first-byte': 150,
    'first-cpu-idle': 20000,
    'time-to-interactive': 20000,
    'lowest-time-to-widget': 5000,
    'median-time-to-widget': 6000,
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
}

colors = [
    '#4FC1F8',
    '#35F2CD',
    '#B943FF',
    '#FF3F85',
    '#7CF642',
    '#FF390F',
    '#F6B42A',
    '#4FC1F8',
    '#35F2CD',
    '#B943FF',
    '#FF3F85',
    '#7CF642',
    '#FF390F',
    '#F6B42A',
    '#4FC1F8',
    '#35F2CD',
    '#B943FF',
    '#FF3F85',
    '#7CF642',
    '#FF390F',
    '#F6B42A',
    '#4FC1F8',
    '#35F2CD',
    '#B943FF',
    '#FF3F85',
    '#7CF642',
    '#FF390F',
    '#F6B42A',
]

metricsToUse = {
    'first-contentful-paint': 'FCP',
    'first-meaningful-paint': 'FMP',
    'speed-index': 'SI',
    'total-blocking-time': 'TBT',
    'estimated-input-latency': 'EIL',
    'first-cpu-idle': 'FCI',
    'time-to-interactive': 'TTI',
    'network-requests': 'NR',
    'dom-size': 'DOM',
    'lowest-time-to-widget': 'LTTW',
    'median-time-to-widget': 'MTTW',
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please specify a folder containing .csv files from which to generate the timeline')
        exit(1)

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

    iterations = 0
    
    figure, ax = plt.subplots(len(metricsToUse), len(Data), figsize=(len(Data) * 1.5, len(metricsToUse) * 2))
    for improvement in Data:
        metricsIndex = 0
        for column in improvement:
            if column in metricsToUse:
                ax[metricsIndex, iterations] = seaborn.boxenplot(data=improvement[column], ax=ax[metricsIndex, iterations], color=colors[metricsIndex])
                ax[metricsIndex, iterations].set(xticklabels=[''], ylim=(yAxixMinSize[column], yAxixMaxSize[column]))
                ax[metricsIndex, iterations].grid(linewidth=0.5)

                if column in timeMetrics:
                    ax[metricsIndex, iterations].set(ylabel='Time (ms)')
                else:
                    ax[metricsIndex, iterations].set(ylabel='Quantity')

                seaborn.despine(left=False, right=False, top=False, bottom=False, ax=ax[metricsIndex, iterations])

                plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.0, hspace=0.5)
                plt.grid(True)

                if iterations == 0:
                    ax[metricsIndex, iterations].annotate(metricsToUse[column], xy=(0, 0.5), xytext=(-ax[metricsIndex, iterations].yaxis.labelpad - 10, 0),
                                xycoords=ax[metricsIndex, iterations].yaxis.label, textcoords='offset points',
                                size='20', ha='right', va='center')
                else:
                    # ax[metricsIndex, iterations].set_yticks([])
                    ax[metricsIndex, iterations].set(ylabel='', yticklabels=[''])


                metricsIndex += 1

        ax[0, iterations].annotate('Baseline' if iterations == 0 else 'I' + str(iterations), xy=(0.5, 1), xytext=(0, 5),
                    xycoords='axes fraction', textcoords='offset points',
                    size='16', ha='center', va='baseline')
        iterations += 1

    figure.tight_layout()
    figure.savefig('../figures/timeline.png')
    figure.clf()
    plt.close()

    print('Done!')

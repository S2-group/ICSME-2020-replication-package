import sys
import numpy
import pandas
import seaborn


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('This script requires you to specify a .csv file as input. Please do so.')
        exit(1)

    Data = pandas.read_csv(sys.argv[1])
    
    for column in Data:
        plot = seaborn.boxenplot(data=Data[column])
        plot.set(xlabel=column)
        figure = plot.get_figure()
        figure.savefig('../figures/' + column + '.jpeg')
        figure.clf()

    print('Done!')
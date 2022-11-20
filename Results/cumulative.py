import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
import pandas
import csv


def count(name):
    success = 0
    failure = 0
    exhaustion = 0
    with open("sfe/" + name + ".csv", 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if row[0] == "0": 
                exhaustion += 1
            if row[0] == "1":
                success += 1
            if row[0] == "-1":
                failure += 1 
    return failure

def plot_vanilla():
    df = pandas.read_csv("sfe.csv")
    print(df.to_string())
    bar_plot = sns.barplot(data=df, x="obstacles", y="failures", hue="alpha")
    fig = bar_plot.get_figure()
    fig.savefig("sfe.png")
    plt.show()



if __name__ == "__main__":
    plot_vanilla()


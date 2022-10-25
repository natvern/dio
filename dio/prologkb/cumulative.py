import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
import pandas
import config
import csv


def plot_vanilla(name):
    ## To plot cumulative failures
    cs = pandas.read_csv('cumulative_rewards/' + name + ".csv")   
    res = sns.lineplot(x="Episode", y="Cumulative", data=cs)
    plt.show()
    f1 = res.get_figure()
    f1.savefig("cumulative_rewards/" + name + ".png")

plot_vanilla(config.config.currentFile)

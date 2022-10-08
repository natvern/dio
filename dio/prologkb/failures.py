import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
import pandas
import config
import csv


def plot_vanilla(name):
    ## To create csv file of cumulative failures
    f2 = open("sfe/" + name + ".csv", 'r')
    f = open('cumulative_failures/' + name + ".csv", 'w')
    writer = csv.writer(f)
    s = 0
    i = 0
    writer.writerow(["Episode", "Failure"]) # Header
    for row in f2: 
        if row == "-1\n":
            s += 1 
        writer.writerow([i,s])
        i += 1
    f.close()

    ## To plot cumulative failures
    cs = pandas.read_csv('cumulative_failures/' + name + ".csv")   
    res = sns.lineplot(x="Episode", y="Failure", data=cs)
    plt.show()
    f1 = res.get_figure()
    f1.savefig("cumulative_failures/" + name + ".png")

plot_vanilla(config.config.currentFile)

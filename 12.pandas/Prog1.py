import pandas
from matplotlib import pyplot

scoresDF = pandas.read_csv("./scores.csv")

print(scoresDF)

scoresDF.fillna(0,inplace=True)

print(scoresDF)

print(scoresDF.loc[0])
#print(scoresDF.loc([0,1]))

print(scoresDF.info())
#print(scoresDF.corr())

scoresDF["Maths"].plot(kind="hist")

pyplot.show()

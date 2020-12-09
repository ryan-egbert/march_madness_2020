import re

digitre = r'\d+(\s+)'
for year in range(2000,2021):
    csvName = "../data/csv/" + str(year) + "_data.csv"
    newCsvName = "../data/csv/" + str(year) + "_data_updated.csv"
    with open(csvName, 'r') as csv:
        with open(newCsvName, 'w') as new:
            for line in csv:
                line = line.replace(" ", ",")
                new.write(line)
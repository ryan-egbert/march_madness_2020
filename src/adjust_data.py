# import pandas as pd
import pickle as pk

KEEPERS = ["SCHOOLNAME", "RPI", "RECORD", "Q1", "1-50", "VTOP100"]
KEEPERSDICT = {"SCHOOLNAME": -1, "RPI": -1, "RECORD": -1, "Q1": -1, "1-50": -1, "VTOP100": -1}
all_years = {}
# for year in range(2000,2021):
for year in range(2000,2021):
    schools = {}
    csvName = "../data/csv/" + str(year) + "_data_updated.csv"
    with open(csvName, 'r') as csv:
        firstLine = True
        for line in csv:
            if firstLine:
                columns = line.split(',')
                for i in range(len(columns)):
                    if columns[i] in KEEPERS:
                        KEEPERSDICT[columns[i]] = i
                firstLine = False
            else:
                columns = line.split(',')
                schools[columns[0].lower().replace(".","").replace("&","").replace("-","").replace("(","").replace(")","").replace("'", "")] = {}
                for key in KEEPERSDICT:
                    if KEEPERSDICT[key] != -1:
                        if key in ["RECORD", "Q1", "1-50", "VTOP100"]:
                            wl = columns[KEEPERSDICT[key]].split('-')
                            print(wl, csvName, KEEPERSDICT[key], key)
                            w = int(wl[0])
                            l = int(wl[1])
                            if w+l != 0:
                                schools[columns[0].lower().replace(".","").replace("&","").replace("-","").replace("(","").replace(")","").replace("'", "")][key] = round(w/(l+w),3)
                            else:
                                schools[columns[0].lower().replace(".","").replace("&","").replace("-","").replace("(","").replace(")","").replace("'", "")][key] = 0.0
                        else:
                            if len(columns) > KEEPERSDICT[key]:
                                schools[columns[0].lower().replace(".","").replace("&","").replace("-","").replace("(","").replace(")","").replace("'", "")][key] = columns[KEEPERSDICT[key]].lower().replace(".","").replace("&","").replace("-","").replace("(","").replace(")","")
    all_years[year] = schools
    KEEPERSDICT = {"SCHOOLNAME": -1, "RPI": -1, "RECORD": -1, "Q1": -1, "1-50": -1, "VTOP100": -1}
print(all_years)
with open("data_all_years.pck", 'wb') as p:
    pk.dump(all_years, p)
        # for year in range(2000,2021):
        #     keepersDict = {}
        #     with open(str(year) + "_data.csv", 'r') as csv:
        #         firstLine = True
        #         columnNums = []
        #         for line in csv:
        #             if firstLine:
        #                 columns = line.split(",")
        #                 for i in range(len(columns)):
        #                     if columns[i] in KEEPERS:
        #                         if columns[i] == "SCHOOLNAME":
        #                             keepersDict[columns[i]] = {}
        #                         columnNums.append(i)
        #                 firstLine = False
        #             else:
        #                 data = line.split(",")
        #                 for i in range(len(data)):
        #                     if i in columnNums:

        # csv = pd.read_csv(csvName, error_bad_lines=False)
        # for c in csv.columns:
        #     if c not in KEEPERS:
        #         csv = csv.drop([c], axis=1)

        # print(csv)
        # with open(str(year) + "_data_pck.pck", 'wb') as p:
        #     pk.dump(csv, p)
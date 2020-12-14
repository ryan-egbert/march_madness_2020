import pandas as pd
import pickle

with open("csv/all_data_combined_r6.csv", 'w') as FINAL:
    FINAL.write("YEAR,ROUND,TEAM1,TEAM1SEED,TEAM1REC,TEAM1RPI,TEAM1TOP50,TEAM1SCORE,TEAM2,TEAM2SEED,TEAM2REC,TEAM2RPI,TEAM2TOP50,TEAM2SCORE,WINNINGTEAM\n")
    with open("../data/csv/2020_MARCH_MADNESS_ROUND6.csv", 'r') as mm:
        with open("pck/all_years_data.pck", 'rb') as pck:
            all_data_dict = pickle.load(pck)
            firstLine = True
            for linemm in mm:
                if firstLine:
                    print("columns done")
                    firstLine = False
                else:
                    for year in range(2020,2021):
                        data = linemm.split(',')
                        year_ = data[0]
                        if year == int(year_):
                            # print(data, year)
                            round_ = int(data[1])
                            seed_team1 = int(data[4])
                            seed_team2 = int(data[9])
                            team1 = data[6].lower().replace(".","").replace("&","").replace("-","").replace("(","").replace(")","").replace(" ","")
                            team2 = data[7].lower().replace(".","").replace("&","").replace("-","").replace("(","").replace(")","").replace(" ","")
                            score_team1 = int(data[5])
                            score_team2 = int(data[8])
                            if score_team1 > score_team2:
                                victory_team = 0
                                opp_vteam = 1
                            else:
                                victory_team = 1
                                opp_vteam = 0

                            rpi_team1 = int(all_data_dict[year][team1]["RPI"])
                            rpi_team2 = int(all_data_dict[year][team2]["RPI"])
                            if "Q1" in all_data_dict[year][team1].keys():
                                top50_team1 = all_data_dict[year][team1]["Q1"]
                            elif "1-50" in all_data_dict[year][team1].keys():
                                top50_team1 = all_data_dict[year][team1]["1-50"]
                            elif "VTOP100" in all_data_dict[year][team1].keys():
                                top50_team1 = all_data_dict[year][team1]["VTOP100"]
                            else:
                                top50_team1 = None
                            
                            if "Q1" in all_data_dict[year][team2].keys():
                                top50_team2 = all_data_dict[year][team2]["Q1"]
                            elif "1-50" in all_data_dict[year][team2].keys():
                                top50_team2 = all_data_dict[year][team2]["1-50"]
                            elif "VTOP100" in all_data_dict[year][team2].keys():
                                top50_team2 = all_data_dict[year][team2]["VTOP100"]
                            else:
                                top50_team2 = None
                            record_team1 = all_data_dict[year][team1]["RECORD"]
                            record_team2 = all_data_dict[year][team2]["RECORD"]
                            new_line = [
                                str(year_),
                                str(round_),
                                str(team1),
                                str(seed_team1),
                                str(record_team1),
                                str(rpi_team1),
                                str(top50_team1),
                                str(score_team1),
                                # str(victory_team1),
                                str(team2),
                                str(seed_team2),
                                str(record_team2),
                                str(rpi_team2),
                                str(top50_team2),
                                str(score_team2),
                                str(victory_team)
                            ]
                            new_line_2 = [
                                str(year_),
                                str(round_),
                                str(team2),
                                str(seed_team2),
                                str(record_team2),
                                str(rpi_team2),
                                str(top50_team2),
                                str(score_team2),
                                # str(victory_team1),
                                str(team1),
                                str(seed_team1),
                                str(record_team1),
                                str(rpi_team1),
                                str(top50_team1),
                                str(score_team1),
                                str(opp_vteam)
                            ]
                            FINAL.write(",".join(new_line))
                            FINAL.write("\n")
                            FINAL.write(",".join(new_line_2))
                            FINAL.write("\n")
                            print(new_line)
                            print(new_line_2)

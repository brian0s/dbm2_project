import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

#print("Café au lait")

with open("../matches_1930_2022.csv", "r", encoding='utf-8', errors='replace') as f:
    data = f.readlines()

#(0)Year,(1)Host,(2)Teams,(3)Champion,(4)Runner-Up,(5)TopScorrer,(6)Attendance,(7)AttendanceAvg,(8)Matches

cleaned_match = ''

#print(data[1])

#for match in data:
    #split_match = match.split(",")
    #cleaned_match = cleaned_match + split_match[0] + ";"
    #cleaned_match = cleaned_match + split_match[1]

match_dic = {}
pk = 0
total_goals = 0
fk = 0

for match in data[1:2]:
    goal_fks = []
    pk += 1
    new_row = match.replace("West Germany", "Germany")
    new_row = new_row.replace("Germany DR", "Germany")
    new_row = new_row.replace("Korea Republic, Japan", "Korea Republic and Japan")
    split_match = new_row.split(",")
    team1 = split_match[0] + "&" + str(split_match[17][:4])
    team2 = split_match[1] + "&" + str(split_match[17][:4])
    with open("../countries/countries_cleaned.csv", "r", encoding='utf-8', errors='replace') as f_countries:
        valid_countries = f_countries.readlines()
        
    with open("../teams/teams_cleaned.csv", "r", encoding='utf-8', errors='replace') as f_teams:
        valid_teams = f_teams.readlines()
        for team in valid_teams:
            name = team.split(":")[0]
            t_fk = team.split(":")[1]
            if split_match[0]
            print(t_fk, name)
    match_name = (team1 + "," + team2 + "," + split_match[17])
    goals = (split_match[23].split("|"))
    goals1 = (split_match[24].split("|"))
    pens = (split_match[30])
    pens1 = (split_match[31])
    date = (split_match[17])
    for goal in goals1:
        if len(goal) > 1:
            goals.append(goal)
            #print(goal)
    pens_split = pens.split("|")
    for pen in pens_split:
        if len(pen) > 1:
            pen = pen.replace("(P) ", "")
            #print(pen)
            goals.append(pen)
    pens1_split = pens1.split("|")
    for pen in pens1_split:
        if len(pen) > 1:
            pen = pen.replace("(P) ", "")
            #print(pen)
            goals.append(pen)
    if len(goals) > 1:
        for goal in goals:
            if len(goal) >= 1:
                fk += 1
                goal_split = goal.split(" · ")
                #print(date)
                scorer = goal_split[0]
                with open("../goals/goals_cleaned.csv", "r", encoding='utf-8', errors='replace') as f_goals:
                    valid_goals = f_goals.readlines()
                    for goal in valid_goals:
                        #print(fk, goal.split(":")[0])
                        if str(fk) == goal.split(":")[0]:
                            goal_fks.append(str(fk))
                            break
    #print(goal_fks)
    if len(goal_fks) > 0:
        cleaned_match = cleaned_match + str(pk) + ":"+ match_name + "," + ";".join(goal_fks)+ "\n"
    else:
        cleaned_match = cleaned_match + str(pk) + ":"+ match_name + "," + "No Goals" + "\n" 



with open("matches_cleaned.csv", "w", encoding='utf-8', errors='replace') as f_write:
    f_write.write(cleaned_match[:-1])
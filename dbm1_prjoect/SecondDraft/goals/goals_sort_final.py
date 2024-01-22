import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

#print("Café au lait")

with open("../matches_1930_2022.csv", "r", encoding='utf-8', errors='replace') as f:
    data = f.readlines()

#(0)Year,(1)Host,(2)Teams,(3)Champion,(4)Runner-Up,(5)TopScorrer,(6)Attendance,(7)AttendanceAvg,(8)goales

cleaned_goals = ''

#print(data[1])

#for goal in data:
    #split_goal = goal.split(",")
    #cleaned_goal = cleaned_goal + split_goal[0] + ";"
    #cleaned_goal = cleaned_goal + split_goal[1]

results = ''
pk = 0
match_id = 0

for match in data[1:]:
    match_id += 1
    found = False
    with open("./matches_in_db.csv", "r", encoding='utf-8', errors='replace') as f_valid:
        valids = f_valid.readlines()
        for valid in valids:
            valid = valid.split(",")
            v_pk = int(valid[0])
            if v_pk == match_id:
                print(v_pk, match_id)
                found = True
                break
    if not found:
        continue
    new_row = match.replace("West Germany", "Germany")
    new_row = new_row.replace("Germany DR", "Germany")
    new_row = new_row.replace("Korea Republic, Japan", "Korea Republic and Japan")
    split_match = new_row.split(",")
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
                goal_split = goal.split(" · ")
                #print(date)
                scorer = goal_split[0]
                with open("./players_cleaned.csv", "r", encoding='utf-8', errors='replace') as f_players:
                    players = f_players.readlines()
                    for player in players:
                        player = player.strip()
                        fk = player.split(":")[0]
                        name = player.split(":")[1]
                        #print(name, captain1, captain2)
                        if scorer == name:
                            scorer = fk
                #print(scorer, goal)
                pk += 1
                if scorer.isnumeric():
                    try:
                        minute = goal_split[1]
                        #print(str(pk) + ":" + scorer + "," + minute)
                        #INSERT INTO GOAL (Player_ID, Match_ID, Minute) VALUES (1, 1, 45);
                        cleaned_goals = cleaned_goals + "INSERT INTO GOAL (Player_ID, Match_ID, Minute) VALUES (" + scorer + "," + str(match_id) + "," + f"'{minute}'" + ");"+ "\n"
                        #cleaned_goals = cleaned_goals + "INSERT INTO GOAL (Player_ID, Match_ID, Minute) VALUES (" + scorer + "," + str(display_match_id) + "," + f"'{minute}'" + "," + f"{date}"+ ");"+ "\n"
                        #cleaned_goals = cleaned_goals + str(match_id) + ":" + scorer + "," + minute + "\n"
                    except IndexError:
                        continue
                else:
                    continue
#print(cleaned_goals)

with open("goals_cleaned.csv", "w", encoding='utf-8', errors='replace') as f_write:
    f_write.write(cleaned_goals[:-1])

#with open("valid.txt", "w", encoding='utf-8', errors='replace') as f_write:
#    f_write.write(results[:-1])
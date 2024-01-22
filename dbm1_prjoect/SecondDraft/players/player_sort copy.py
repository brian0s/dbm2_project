import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

with open("../matches_1930_2022.csv", "r", encoding='utf-8', errors='replace') as f:
    data = f.readlines()

cleaned_players = ''

player_dic = {}

pk = 0

for match in data[1:]:
    new_row = match.replace("West Germany", "Germany")
    new_row = new_row.replace("Germany DR", "Germany")
    new_row = new_row.replace("Korea Republic, Japan", "Korea Republic and Japan")
    new_row = new_row.replace("\xa0", " ")
    split_match = new_row.split(",")
    #9
    captain1 = split_match[9]
    if captain1 not in player_dic:
        pk += 1
        player_dic[captain1] = pk
    #11
    captain2 = split_match[11]
    if captain2 not in player_dic:
        pk += 1
        player_dic[captain2] = pk
    goals = (split_match[23].split("|"))
    goals1 = (split_match[24].split("|"))
    for goal in goals1:
        if len(goal) > 1:
            goals.append(goal)
    if len(goals) > 1:
        for goal in goals:
            if len(goal) >= 1:
                goal_split = goal.split(" · ")
                #print(date)
                scorer = goal_split[0]
                minute = goal_split[1]
                #print(str(pk) + ":" + scorer)
                if scorer not in player_dic:
                    pk += 1
                    player_dic[scorer] = pk


#print(player_dic)

for k, v in player_dic.items():
    cleaned_players = cleaned_players + str(v) + ":" + k + "\n"


with open("players_cleaned.csv", "w", encoding='utf-8', errors='replace') as f_write:
    f_write.write(cleaned_players[:-1])
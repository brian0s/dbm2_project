import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

with open("../matches_1930_2022.csv", "r", encoding='utf-8', errors='replace') as f:
    data = f.readlines()

cleaned_players = ''

player_dic = {}


for match in data[1:]:
    new_row = match.replace("West Germany", "Germany")
    new_row = new_row.replace("Germany DR", "Germany")
    new_row = new_row.replace("Korea Republic, Japan", "Korea Republic and Japan")
    new_row = new_row.replace("\xa0", " ")
    split_match = new_row.split(",")
    date = split_match[17]
    year = date[:4]
    team1 = split_match[0] + "&" + str(year)
    team2 = split_match[1] + "&" + str(year)
    #9
    captain1 = split_match[9]
    #print(captain1)
    if captain1 not in player_dic:
        player_dic[captain1] = team1
    #11
    captain2 = split_match[11]
    if captain2 not in player_dic:
        player_dic[captain2] = team2
    goals = (split_match[23].split("|"))
    goals1 = (split_match[24].split("|"))
    for goal in goals1:
        if len(goal) >= 1:
            goal_split = goal.split(" · ")
            #print(date)
            scorer = goal_split[0]
            minute = goal_split[1]
            #print(str(pk) + ":" + scorer)
            if scorer not in player_dic:
                player_dic[scorer] = team1
    if len(goals) > 1:
        for goal in goals:
            if len(goal) >= 1:
                goal_split = goal.split(" · ")
                #print(date)
                scorer = goal_split[0]
                minute = goal_split[1]
                #print(str(pk) + ":" + scorer)
                if scorer not in player_dic:
                    player_dic[scorer] = team2


#print(player_dic)

for k, v in player_dic.items():
    #print(k)
    k = k.replace("'", "")
    year = v.split("&")[1]
    country = v.split("&")[0]
    print(year, country)
    with open("../teams_cleaned.csv", "r", encoding='utf-8', errors='replace') as f_teams:
        teams = f_teams.readlines()
        for team in teams[:10]:
            team_split = team.split(",")
            if team_split[1].strip():
                scorer = fk
    cleaned_players = cleaned_players + (f"INSERT INTO PLAYER (Player_Name) VALUES ('{k}');") + "\n"


with open("selection_cleaned.csv", "w", encoding='utf-8', errors='replace') as f_write:
    f_write.write(cleaned_players[:-1])
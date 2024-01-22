import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

with open("../matches_1930_2022.csv", "r", encoding='utf-8', errors='replace') as f:
    data = f.readlines()

selection_cleaned = ''

team_dic = {}


for match in data[1:]:
    new_row = match.replace("West Germany", "Germany")
    new_row = new_row.replace("Germany DR", "Germany")
    new_row = new_row.replace("Korea Republic, Japan", "Korea Republic and Japan")
    new_row = new_row.replace("\xa0", " ")
    new_row = new_row.replace("'", "")
    new_row = new_row.replace("United States", "USA")
    split_match = new_row.split(",")
    date = split_match[17]
    year = date[:4]
    team1 = split_match[0] + "&" + str(year)
    team2 = split_match[1] + "&" + str(year)
    #9
    captain1 = split_match[9]
    captain2 = split_match[11]
    #print(captain1)
    if team1 not in team_dic:
        #team_dic[captain1] = team1
        team_dic[team1] = [captain1]
    else:
        tmp = team_dic[team1]
        if captain1 not in tmp:
            tmp.append(captain1)
            team_dic[team1] = tmp
    #11
    if team2 not in team_dic:
        team_dic[team2] = [captain2]
    else:
        tmp = team_dic[team2]
        if captain2 not in tmp:
            tmp.append(captain2)
            team_dic[team2] = tmp
    goals = (split_match[23].split("|"))
    goals1 = (split_match[24].split("|"))
    #print(goals, goals1)
    for goal in goals:
        if len(goal) >= 1:
            goal_split = goal.split(" · ")
            #print(date)
            scorer = goal_split[0]
            minute = goal_split[1]
            #print(str(pk) + ":" + scorer)
            if team1 not in team_dic:
                #team_dic[scorer] = team1
                team_dic[team1] = [scorer]
            else:
                tmp = team_dic[team1]
                if scorer not in tmp:
                    tmp.append(scorer)
                    team_dic[team1] = tmp
    if len(goals1) >= 1:
        for goal in goals1:
            if len(goal) >= 1:
                goal_split = goal.split(" · ")
                #print(goal)
                #print(date)
                scorer = goal_split[0]
                minute = goal_split[1]
                #print(scorer)
                if team2 not in team_dic:
                    team_dic[team2] = [scorer]
                else:
                    tmp = team_dic[team2]
                    if scorer not in tmp:
                        tmp.append(scorer)
                        team_dic[team2] = tmp

print(team_dic)



for k, v in team_dic.items():
    print(k, v)
    selection_cleaned += f"{k}: {v}\n"


with open("selection_cleaned.csv", "w", encoding='utf-8', errors='replace') as f_write:
    f_write.write(selection_cleaned[:-1])
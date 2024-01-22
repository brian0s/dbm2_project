import sys
import io
from unidecode import unidecode

#text_with_accents = "Ángel Di María"
#text_normalized = unidecode(text_with_accents)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

with open("./selection_cleaned.csv", "r", encoding='utf-8', errors='replace') as f:
    data = f.readlines()

with open("./players_cleaned.csv", "r", encoding='utf-8', errors='replace') as f_players:
    players = f_players.readlines()

results = ''

team_dic = {}

for line_raw in data:
    line = line_raw
    line = line.replace("\xa0", " ")
    line = line.replace("'", "")
    line = line.strip()
    line = line.split(":")
    #print(line)
    team = line[0]
    names = line[1]
    #print(team)
    names = names.split(",")
    for name in names:
        name = name.strip()
        name = name.replace("[", "")
        name = name.replace("]", "")
        name = name.replace("'", "")
        name = unidecode(name)
        #print(team, name)
        for player in players:
            player = player.split(":")
            player_name = player[1].strip()
            player_name = unidecode(player_name)
            player_pk = player[0]
            #print(player_name, name)
            if player_name == name:
                #print(f"found {player_name} plays for {team}, replacing with {player_pk}")
                if team not in team_dic:
                    team_dic[team] = [player_pk]
                else:
                    tmp = team_dic[team]
                    if player_pk not in tmp:
                        tmp.append(player_pk)
                        team_dic[team] = tmp


#print(team_dic)

with open("./team_in_db.csv", "r", encoding='utf-8', errors='replace') as f_team_data:
    team_data = f_team_data.readlines()


final_dic = {}

for team in team_data:
    #print(team)
    team = team.split(",")
    team_pk = team[0]
    team_country = team[1]
    team_captain = team[2]
    team_manager = team[3]
    team_year = team[4].strip()
    for k, v in team_dic.items():
        k = k.split("&")
        country = k[0]
        year = k[1]
        if country == team_country and team_year == year:
            if team_captain not in v:
                v.append(team_captain)
            #print(country, team_country, team_year, year, v) 
            for num in v:
                #print(f"INSERT INTO Selection (Team_ID, Player_ID) VALUES ({team_pk}, {num});")
                results += f"INSERT INTO Selection (Team_ID, Player_ID) VALUES ({team_pk}, {num});\n"
            break


with open("final_selected_for.csv", "w", encoding='utf-8', errors='replace') as f_write:
    f_write.write(results[:-1])
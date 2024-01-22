import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

#print("Café au lait")

with open("../matches_1930_2022.csv", "r", encoding='utf-8', errors='replace') as f:
    data = f.readlines()

#(0)Year,(1)Host,(2)Teams,(3)Champion,(4)Runner-Up,(5)TopScorrer,(6)Attendance,(7)AttendanceAvg,(8)Matches

cleaned_teams = ''

team_dic = {}
#print(data[:2])

for row in data[1:]:
    new_row = row.replace("West Germany", "Germany")
    new_row = new_row.replace("Germany DR", "Germany")
    split_teams = new_row.split(",")
    date = split_teams[17]
    year = date[:4]
    manager1 = split_teams[8]
    manager2 = split_teams[10]
    captain1 = split_teams[9]
    captain2 = split_teams[11]
    team1 = split_teams[0] + "&" + str(year)
    team2 = split_teams[1] + "&" + str(year)
    with open("../players/players_cleaned.csv", "r", encoding='utf-8', errors='replace') as f_players:
        players = f_players.readlines()
        for player in players:
            player = player.strip()
            fk = player.split(":")[0]
            name = player.split(":")[1]
            #print(name, captain1, captain2)
            if captain1 == name and (team1 not in team_dic):
                captain1 = fk
            elif captain2 == name and (team2 not in team_dic):
                captain2 = fk
    #print(manager1, manager2)
    details1 = year +  "," + manager1
    details2 = year + "," + manager2
    #print(captain2)
    #print(details1)
    #print(team1, team2, year)
    if team1 not in team_dic:
        details1 = details1 + "," + captain1
        team_dic[team1] = [details1]
    elif team1 in team_dic:
        tmp = team_dic[team1]
        if details1 not in tmp:
            details1 = details1 + "," + captain1
            tmp.append(details1)
            team_dic[team1] = tmp
    if team2 not in team_dic:
        details2 = details2 + "," + captain2
        team_dic[team2] = [details2]
    elif team2 in team_dic:
        tmp = team_dic[team2]
        if details2 not in tmp:
            details2 = details2 + "," + captain2
            tmp.append(details2)
            team_dic[team2] = tmp



#print(team_dic)
#cleaned_teams = cleaned_teams.replace("West Germany", "Germany")
#cleaned_teams = cleaned_teams.replace("...", "")

pk = 0

for k, v in team_dic.items():
    fk = 0
    #pk += 1
    #print(str(pk) + ":" + k + "," + year)
    #cleaned_teams = cleaned_teams + str(pk) + ":" + k + "," + year + "\n"
    split_details = v[0].split(",")
    #print(split_details)
    #print(k + ":" + split_details[1] + "," + split_details[2])
    year = k.split("&")[1]
    country = k.split("&")[0]
    with open("../countries/countries_cleaned.csv", "r", encoding='utf-8', errors='replace') as f_countries:
        countries = f_countries.readlines()
        for c in countries:
            valid_country = c.split(":")[1]
            country_no = c.split(":")[0]
            #print(country, valid_country.strip())
            if country == valid_country.strip():
                fk = country_no
                break
    pk += 1
    cleaned_teams = cleaned_teams + (str(pk) + ":" + year + "," + str(fk) + "," + split_details[1] + "," + split_details[2]) + "\n"
    #cleaned_teams = cleaned_teams + (k + ":" + split_details[1] + "," + split_details[2]) + "\n"


with open("teams_cleaned.csv", "w", encoding='utf-8', errors='replace') as f_write:
    f_write.write(cleaned_teams[:-1])
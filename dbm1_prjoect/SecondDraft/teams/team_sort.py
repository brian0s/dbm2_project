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

#for row in data[1:]:
for row in data[1:]:
    new_row = row.replace("West Germany", "Germany")
    new_row = new_row.replace("Germany DR", "Germany")
    new_row = new_row.replace("United States", "USA")
    new_row = new_row.replace("Côte d'Ivoire", "Côte dIvoire")
    new_row = new_row.replace("\xa0", " ")
    new_row = new_row.replace("M'barek Boussoufa", "Mbarek Boussoufa")
    split_teams = new_row.split(",")
    date = split_teams[17]
    year = date[:4]
    manager1 = split_teams[8]
    manager2 = split_teams[10]
    captain1 = split_teams[9]
    captain2 = split_teams[11]
    #print(captain1, captain2)
    team1 = split_teams[0] + "&" + str(year)
    team2 = split_teams[1] + "&" + str(year)
    # Different format in these years
    if (int(year) > 1994) and (int(year) < 2018):
        num_count = 0
        managers = ''
        for char in new_row:
            if char.isnumeric():
                num_count += 1
            if (num_count == 2):
                managers = managers + char
            elif num_count > 2:
                break
        #print(managers.split(","))
        print(new_row)
        managers = managers.split(",")
        manager1 = ''
        manager2 = ''
        for entry in managers:
            if (len(entry) > 1) and (manager1 == ''):
                manager1 = entry
            elif (len(entry) > 1) and (manager1 != ''):
                manager2 = entry
        print(manager1, manager2)
    with open("../players/players_cleaned.csv", "r", encoding='utf-8', errors='replace') as f_players:
        players = f_players.readlines()
        fk = 0
        for player in players:
            fk += 1
            player = player.strip()
            player = player.replace("INSERT INTO PLAYER (Player_Name) VALUES ('", "")
            player = player.replace("');", "")
            name = player.replace("\xa0", " ")
            #print(name)
            if captain1 == name and (team1 not in team_dic):
                #print(fk, name)
                captain1 = str(fk)
            if captain2 == name and (team2 not in team_dic):
                #print(fk, name)
                captain2 = str(fk)
    #print(manager1, manager2)
    details1 = year +  "," + manager1
    details2 = year + "," + manager2
    #print(captain2)
    #print(details1)
    #print(team1, team2, year)
    #print(team1, team2)
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

seen = {}
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
    pk += 1
    #if fk == 0 and country not in seen:
        #seen[country] = True
        #print(country)
    #cleaned_teams = cleaned_teams + year + "," + country + "," + split_details[1] + "," + split_details[2] + "\n"
    cleaned_teams = cleaned_teams + f"INSERT INTO TEAM (Country_Name, Captain, Manager, Year) VALUES ('{country}', {split_details[2]}, '{split_details[1]}', {year});" + "\n"
    #cleaned_teams = cleaned_teams + f"{split_details[2]},'{country}',{year}" + "\n"
    #cleaned_teams = cleaned_teams + (k + ":" + split_details[1] + "," + split_details[2]) + "\n"


with open("teams_cleaned.csv", "w", encoding='utf-8', errors='replace') as f_write:
    f_write.write(cleaned_teams[:-1])
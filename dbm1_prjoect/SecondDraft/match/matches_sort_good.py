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

for match in data[1:]:
    goal_fks = []
    pk += 1
    new_row = match.replace("West Germany", "Germany")
    new_row = new_row.replace("Germany DR", "Germany")
    new_row = new_row.replace("Korea Republic, Japan", "Korea Republic and Japan")
    split_match = new_row.split(",")
    team1 = split_match[0] + "&" + str(split_match[17][:4])
    team2 = split_match[1] + "&" + str(split_match[17][:4])
    date = split_match[17]
    year = date[:4]
    c1 = split_match[0]
    c2 = split_match[1]
    with open("./countries_cleaned1.csv", "r", encoding='utf-8', errors='replace') as f_countries:
        valid_countries = f_countries.readlines()
        for row in valid_countries:
            valid_country = row.split(":")[1]
            valid_country_no = row.split(":")[0]
            if valid_country.strip() == c1:
                c1 = str(valid_country_no)
            elif valid_country.strip() == c2:
                c2 = str(valid_country_no)
    #print(c1, c2)
    with open("./teams_cleaned1.csv", "r", encoding='utf-8', errors='replace') as f_teams:
        valid_teams = f_teams.readlines()
        for team in valid_teams:
            team_split = team.split(":")
            t1_fk = team_split[0]
            team_details = team_split[1].split(",")
            #print(c1 == team_details[1])
            #print(year == team_details[0])
            if (c1 == team_details[1]) and (year == team_details[0]):
                team1fk = t1_fk
                #print(team1fk)
                break
    with open("./teams_cleaned1.csv", "r", encoding='utf-8', errors='replace') as f_teams:
        valid_teams = f_teams.readlines()
        for team in valid_teams:
            team_split = team.split(":")
            t2_fk = team_split[0]
            team_details = team_split[1].split(",")
            #print(c1 == team_details[1])
            #print(year == team_details[0])
            if (c2 == team_details[1]) and (year == team_details[0]):
                team2fk = t2_fk
                #print(team1fk)
                break
    match_name = (f"INSERT INTO match (Team_1, Team_2, Date, Year) VALUES ({team1fk}, {team2fk}, '{split_match[17]}', {year});")
    #print(goal_fks)
    #cleaned_match = cleaned_match + match_name + "\n"
    cleaned_match = cleaned_match + match_name + "\n"



with open("matches_cleaned.csv", "w", encoding='utf-8', errors='replace') as f_write:
    f_write.write(cleaned_match[:-1])
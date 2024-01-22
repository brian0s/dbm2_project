import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

#print("Café au lait")

with open("../matches_1930_2022.csv", "r", encoding='utf-8', errors='replace') as f:
    data = f.readlines()

#(0)Year,(1)Host,(2)Teams,(3)Champion,(4)Runner-Up,(5)TopScorrer,(6)Attendance,(7)AttendanceAvg,(8)Matches

results = ''

match_dic = {}
pk = 0
total_goals = 0
fk = 0
mid = 0

for match in data[1:]:
    mid += 1
    new_row = match.replace("West Germany", "Germany")
    new_row = new_row.replace("Germany DR", "Germany")
    new_row = new_row.replace("Korea Republic, Japan", "Korea Republic and Japan")
    new_row = new_row.replace("\xa0", " ")
    new_row = new_row.replace("'", "")
    new_row = new_row.replace("United States", "USA")
    split_match = new_row.split(",")
    team1 = split_match[0] + "&" + str(split_match[17][:4])
    team2 = split_match[1] + "&" + str(split_match[17][:4])
    date = split_match[17]
    year = date[:4]
    c1 = split_match[0]
    c2 = split_match[1]
    #print(c1, c2, year, "\n")
    found = 0
    with open("../teams/team_in_db.csv", "r", encoding='utf-8', errors='replace') as f_countries:
        teams = f_countries.readlines()
        for line in teams:
            #print(line)
            line = line.split(",")
            country = line[1]
            y = line[-1].strip()
            if found == 2:
                #print(c1, c2, date)
                pk += 1
                break
            elif c1 == country and year == y and found < 2:
                pk1 = line[0]
                #print(country)
                found += 1
            elif c2 == country and year == y and found < 2:
                pk2 = line[0]
                #print(country)
                found += 1
    if found < 2:
        print(c1, c2)
    if found >= 2:
        #print(team1, team2, date, year)
        #print(pk1, pk2, date, year)
        #results += f"INSERT INTO match (Team_1, Team_2, Date, Year) VALUES ({pk1},{pk2},'{date}',{year});\n"
        results += f"INSERT INTO match (Team_1, Team_2, Date, Year) VALUES ({mid},{pk1},{pk2},'{date}',{year});\n"
        #print(match)


#print(f'fail count = {977 - pk}')


with open("match_cleaned.csv", "w", encoding='utf-8', errors='replace') as f_write:
    f_write.write(results[:-1])
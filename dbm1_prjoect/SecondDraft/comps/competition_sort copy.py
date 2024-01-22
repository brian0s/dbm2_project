import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

#print("Café au lait")

with open("world_cup.csv", "r", encoding='utf-8', errors='replace') as f:
    data = f.readlines()

#(0)Year,(1)Host,(2)NoTeams,(3)Champion,(4)Runner-Up,(5)TopScorrer,(6)Attendance,(7)AttendanceAvg,(8)NoMatches

cleaned_competition = ''

#print(data)

pk = 0

for competition in data[1:]:
    #pk += 1
    competition = competition.replace("West Germany", "Germany")
    competition = competition.replace("...", "")
    competition = competition.replace("Germany DR", "Germany")
    #competition = competition.replace("Korea Republic, ", "")
    split_competition = competition.split(",")
    year = split_competition[0]
    #cleaned_competition = cleaned_competition + str(pk) + ":" + ",".join(split_competition)
    host = split_competition[1]
    #print(host)
    champion = split_competition[3]
    runner_up = split_competition[4]
    with open("../countries/countries_cleaned.csv", "r", encoding='utf-8', errors='replace') as f_countries:
        valid_countries = f_countries.readlines()
        for row in valid_countries:
            valid_country = row.split(":")[1]
            valid_country_no = row.split(":")[0]
            if valid_country.strip() == host:
                host = str(valid_country_no)
            elif valid_country.strip() == champion:
                champion = str(valid_country_no)
            elif valid_country.strip() == runner_up:
                runner_up = str(valid_country_no)
    cleaned_competition = cleaned_competition + year + ":" + host + "," + champion + "," + runner_up +"\n"
    #cleaned_competition = cleaned_competition + split_competition[0] + ":" + ",".join(split_competition[1:])


with open("comps_cleaned.csv", "w", encoding='utf-8', errors='replace') as f_write:
    f_write.write(cleaned_competition)
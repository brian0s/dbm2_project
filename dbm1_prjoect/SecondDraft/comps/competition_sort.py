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
    cleaned_competition = cleaned_competition + (f"INSERT INTO Competitions (year, host, winner, runner_up) VALUES ('{year}', '{host}', '{champion}', '{runner_up}');") + "\n"
    #cleaned_competition = cleaned_competition + split_competition[0] + ":" + ",".join(split_competition[1:])


with open("comps_cleaned.csv", "w", encoding='utf-8', errors='replace') as f_write:
    f_write.write(cleaned_competition)
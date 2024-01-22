import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

#print("Café au lait")

with open("../fifa_ranking_2022-10-06.csv", "r", encoding='utf-8', errors='replace') as f:
    data = f.readlines()

#(0)Year,(1)Host,(2)countries,(3)Champion,(4)Runner-Up,(5)TopScorrer,(6)Attendance,(7)AttendanceAvg,(8)Matches

country_dic = {}

cleaned_countries = ''

pk = 1
#print(data[:2])

for row in data[1:]:
    new_row = row.replace("West Germany", "Germany")
    new_row = new_row.replace("Germany DR", "Germany")
    split_countries = new_row.split(",")
    country = split_countries[0]
    country_dic[country] = True
    #print(country)
    #cleaned_countries = cleaned_countries + country + "\n"


with open("../teams/teams_cleaned.csv", "r", encoding='utf-8', errors='replace') as f2:
    data = f2.readlines()


for row in data:
    new_row = row.replace("West Germany", "Germany")
    new_row = new_row.replace("Germany DR", "Germany")
    split_teams = new_row.split(":")
    country = split_teams[0]
    if country not in country_dic:
        country_dic[country] = True

#print(country_dic)
pk = 0

for k, v in country_dic.items():
    pk += 1
    cleaned_countries = cleaned_countries + str(pk) + ":" + k + "\n"

#cleaned_countries = cleaned_countries.replace("West Germany", "Germany")
#cleaned_countries = cleaned_countries.replace("...", "")

with open("countries_cleaned.csv", "w", encoding='utf-8', errors='replace') as f_write:
    f_write.write(cleaned_countries[:-1])
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

#print("Café au lait")

with open("2022-2023 Football Team Stats.csv", "r", encoding='utf-8', errors='replace') as f:
    data = f.readlines()

#Rk;club;Nation;Pos;Squad;Comp;Age;Born;MP;Starts;Min;90s;Goals;Shots;SoT;SoT%

cleaned = ''

for club in data:
    split_club = club.split(";")
    cleaned_club = split_club[0] + ";" + split_club[1] + ";" + split_club[2] + ";" + split_club[3] + ";" + split_club[4] + ";" + split_club[5] + ";" + split_club[6]
    cleaned_club = cleaned_club + ";" + split_club[7] + ";" + split_club[8] + ";" + split_club[9] + ";" + split_club[11]
    cleaned_club = cleaned_club + ";" + split_club[13] + ";" + split_club[18]
    cleaned_club = cleaned_club + ";" + split_club[19]
    #print(cleaned_club)
    cleaned = cleaned + cleaned_club


with open("clubs_cleaned_22-23.csv", "w", encoding='utf-8', errors='replace') as f_write:
    f_write.write(cleaned)
#(1)Rk;(2)club;(3)Nation;(4)Pos;(5)Squad;(6)Comp;(7)Age;(8)Born;(9)MP;
#(10)Starts;(11)Min;(12)90s;(13)Goals;(14)Shots;(15)SoT

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

#print("Café au lait")

with open("2021-2022 Football Player Stats.csv", "r", encoding='utf-8', errors='replace') as f:
    data = f.readlines()

#Rk;Player;Nation;Pos;Squad;Comp;Age;Born;MP;Starts;Min;90s;Goals;Shots;SoT;SoT%

cleaned = ''

for player in data:
    split_player = player.split(";")
    cleaned_player = split_player[0] + ";" + split_player[1] + ";" + split_player[2] + ";" + split_player[3] + ";" + split_player[4] + ";" + split_player[5] + ";" + split_player[6]
    cleaned_player = cleaned_player + split_player[8] + ";" + split_player[9] + ";" + split_player[10] + ";" + split_player[12] + ";" + split_player[13] + ";" + split_player[14]
    #print(cleaned_player)
    cleaned = cleaned + cleaned_player + "\n" 


with open("players_cleaned_21-22.csv", "w", encoding='utf-8', errors='replace') as f_write:
    f_write.write(cleaned)
#(1)Rk;(2)Player;(3)Nation;(4)Pos;(5)Squad;(6)Comp;(7)Age;(8)Born;(9)MP;
#(10)Starts;(11)Min;(12)90s;(13)Goals;(14)Shots;(15)SoT

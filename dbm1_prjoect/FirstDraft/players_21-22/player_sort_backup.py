import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

#print("Café au lait")

with open("2021-2022 Football Player Stats.csv", "r", encoding='utf-8', errors='replace') as f:
    data = f.readlines()

print(data[0])

#Rk;Player;Nation;Pos;Squad;Comp;Age;Born;MP;Starts;Min;90s;Goals;Shots;SoT;SoT%

for player in data:
    column_count = 0
    to_print = ''
    for char in player:
        to_print = to_print + char
        if char == ';':
            column_count += 1
            if column_count == 1:
                print(f"ID: {to_print[:-1]}")
            elif column_count == 2:
                print(f"Player Name: {to_print[:-1]}")
            elif column_count == 3:
                print(f"Nation: {to_print[:-1]}")
            elif column_count == 4:
                print(f"Position: {to_print[:-1]}")
            elif column_count == 5:
                print(f"Squad: {to_print[:-1]}")
            elif column_count == 6:
                print(f"Competition: {to_print[:-1]}")
            elif column_count == 7:
                print(f"Age: {to_print[:-1]}")
            elif column_count == 9:
                print(f"Matches Played: {to_print[:-1]}")
            elif column_count == 10:
                print(f"Starts: {to_print[:-1]}")
            elif column_count == 11:
                print(f"Minutes: {to_print[:-1]}")
            elif column_count == 13:
                print(f"Goals: {to_print[:-1]}")
            elif column_count == 14:
                print(f"Shots: {to_print[:-1]}")
            elif column_count == 15:
                print(f"Shots on Target: {to_print[:-1]}")
            elif column_count >= 16:
                break
            to_print = ''


#with open("dic.txt", "w", encoding='utf-8') as f_write:
    #f_write.write(corrected)
#(1)Rk;(2)Player;(3)Nation;(4)Pos;(5)Squad;(6)Comp;(7)Age;(8)Born;(9)MP;
#(10)Starts;(11)Min;(12)90s;(13)Goals;(14)Shots;(15)SoT

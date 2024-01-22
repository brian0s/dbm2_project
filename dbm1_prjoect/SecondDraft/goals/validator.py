import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

#print("Café au lait")

with open("./matches_in_db.csv", "r", encoding='utf-8', errors='replace') as f:
    data = f.readlines()

found_no = 0

for line in data:
    #print(line)
    line = line.split(",")
    db_pk = line[0]
    #print(db_pk)
    found = False
    with open("./valid.txt", "r", encoding='utf-8', errors='replace') as f_valid:
        valids = f_valid.readlines()
        for valid in valids:
            valid = valid.strip()
            #print(valid)
            if valid == db_pk:
                found_no += 1
                #print(valid)
                found = True
                break
    if not found:
        print(db_pk)
print("found no: " + str(found_no))
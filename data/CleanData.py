original_data = open('scopus_5.csv',"r",encoding="utf-8").read()
file = open('scopus_5_cleaned.csv',"w+",encoding="utf-8")
file.write(original_data)
file.close()

average_size = 0
counter = 0
sum = 0

with open('scopus_5_cleaned.csv', encoding="utf-8") as reader, open('scopus_5_cleaned.csv', 'r+', encoding="utf-8") as writer:
    for line in reader:
        if (line.strip() and line[0] == "\"") or counter == 0:
            writer.write(line)
            counter += 1
            sum += len(line)
    writer.truncate()

average_size = int(sum/counter)
counter = 0

with open('scopus_5_cleaned.csv', encoding="utf-8") as reader, open('scopus_5_cleaned.csv', 'r+', encoding="utf-8") as writer:
    for line in reader:
        if len(line) > average_size/8 or counter == 0:
            if (line[0] != "\"" and counter != 0): line = "\"" + line
            writer.write(line)
            counter += 1
    writer.truncate()

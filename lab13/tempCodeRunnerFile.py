# c
import csv
file = open("data-1 (1).csv", "r")
reader = csv.reader(file)
for row in reader:
    print(row)
file.close()

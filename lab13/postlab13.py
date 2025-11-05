# a. Count lines, words, and characters in a file
file = open("ex.txt", "r")
lines = file.readlines()
num_lines = len(lines)
num_words = 0
num_chars = 0
for line in lines:
    words = line.split()
    num_words += len(words)
    num_chars += len(line)

print("Lines:", num_lines)
print("Words:", num_words)
print("Characters:", num_chars)

file.close()


# b
file = open("file.txt", "r")
lines = []
for line in file:
    lines.append(line.strip())
file.close()
print(lines)



# c
import csv
file = open("data-1 (1).csv", "r")
reader = csv.reader(file)
for row in reader:
    print(row)
file.close()


# d
file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")
merged = open("merged.txt", "w")
for line in file1:
    merged.write(line)
for line in file2:
    merged.write(line)
file1.close()
file2.close()
merged.close()
print("Files merged successfully!")

file1 = open(r"D:\ict\sem3\PWP\lecture code\labs\lab13\ict (1).txt")

f1 = open(r"D:\ict\sem3\PWP\lecture code\labs\lab13\ict (1).txt")
# This will print every line one by one in the file
for each in f1:
    print (each)


# Python code to illustrate read() mode
f1 = open(r"D:\ict\sem3\PWP\lecture code\labs\lab13\ict (1).txt")
print (f1.read())

with open(r"D:\ict\sem3\PWP\lecture code\labs\lab13\ict (1).txt") as f1:  
    data = f1.read() 
print(data)

f1 = open(r"D:\ict\sem3\PWP\lecture code\labs\lab13\ict (1).txt")
print (f1.read(5))


with open(r"D:\ict\sem3\PWP\lecture code\labs\lab13\ict (1).txt") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)

file = open("ict1 (1).txt",'w')
file.write("ICT ICT ICT\n")
file.write("ICT ICT ICT ICT ICT")
file.close()


with open("file.txt", "w") as f: 
    f.write("Hello World!!!") 
    f.close()


with open(r"D:\ict\sem3\PWP\lecture code\labs\lab13\a (2).tif", 'rb') as file:
    binary_data = file.read()
with open('c.tif', 'wb') as f:
    f.write(binary_data)
    f.close()


import csv
# Reading from a CSV file
with open('data-1 (1).csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


import csv
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Subject', 'Mark'])
    writer.writerow(['Aansh', 'PWP', 9])
    writer.writerow(['Ashutosh', 'PWP', 10])
    file.close()
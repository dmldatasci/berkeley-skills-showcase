import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal_bonus.csv")

cereal_csv = "../Resources/cereal_bonus.csv"

# read = open(cereal_csv, "r")

# read.close()

# r = read only - if the file not exists create it
# w = write only - if the file not exists create it
# a = append - if the file not exists create it
with open(cereal_csv, "r") as read:
    csv_read = csv.reader(read, delimiter=",")
    # print(csv_read)
    for row in csv_read:
        if float(row[3])>100:
            print(float(row[3]))

    # a = 1


print("Hi")



import csv

with open("weather.txt") as file_local:
    reader = list(csv.reader(file_local))

city = input("Enter a city: ")

for row in reader[1:]:
    if row[0] == city:
        print(row[1])
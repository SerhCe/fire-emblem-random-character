import csv
import json

csvfile = open("..\Heroes.csv", 'r')
csvfile = csvfile.readlines()[1:]
jsonfile = open("..\Heroes.json", 'w')

fieldnames = ("id","CharId","GameId","Game","isMale","isFemale")

reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
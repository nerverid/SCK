#Draft templates for export - import files for tests or lists
import csv

def open_quiz_file(filename):
    with open(filename, "r") as f:
        r = csv.reader(f, delimiter=",")
        for row in r:
            print(",".join(row))

def write_quiz_file(filename):
    with open(filename, "w") as f:
        w = csv.writer(f, delimiter=",")
        w.writerow(["test1","answer1","answer2","answer3","answer4"])
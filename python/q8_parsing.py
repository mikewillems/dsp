#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

import csv

def minvaldif(fname,lab1,lab2):
    with open(fname) as f:
        reader = csv.DictReader(f)
        firstrow = next(reader)
        mindif = abs(int(firstrow[lab1])-int(firstrow[lab2]))
        for row in reader:
            dif = abs(int(row[lab1])-int(row[lab2]))
            if dif < mindif:
                mindif = dif
        return mindif

minvaldif('football.csv','Goals','Goals Allowed')

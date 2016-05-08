# Q1

import csv
from collections import defaultdict

def read_dict_list(csvf):
    reader = csv.DictReader(csvf)
    csvl = []
    for i, row in enumerate(reader):
        csvl.append({})
        for k, v in row.iteritems():
            csvl[i][k.strip()] = v.strip()
    return csvl

def get_from_dict_list(key_name, dict_list):
    item_list = []
    for dic in dict_list:
        item_list.append(dic[key_name])
    return item_list


def find_deg_combs():
    with open('faculty.csv') as fac:
    #     get list of dictionaries, one for each faculty member.
        fac_list = read_dict_list(fac)
    #     extract degree field and create list
        degrees = get_from_dict_list('degree',fac_list)
    #     turn into dictionary with values representing count
        counts = defaultdict(int)
        for deg in degrees:
            counts[deg] += 1
        print counts

def find_degrees():
    with open('faculty.csv') as fac:
        fac_list = read_dict_list(fac)
        members = get_from_dict_list('degree',fac_list)
        split_degrees = []
        for m in members:
            split_degrees.append(m.split())
        degrees = []
        for m in split_degrees:
            if len(m)>0:
                for d in m:
                    degrees.append(d)
            else:
                degrees.append(m)
        counts = defaultdict(int)
        for deg in degrees:
            counts[deg] += 1
        return counts

degs = find_degrees()
print degs
print len(degs) #13


# Q2
def find_titles():
    with open('faculty.csv') as fac:
        fac_list = read_dict_list(fac)
        titles = get_from_dict_list('title',fac_list)
        counts = defaultdict(int)
        for t in titles:
            counts[t] += 1
        return counts

titles = find_titles()
print titles
print len(titles) # 4

#Q3 / 4
def find_emails():
    with open('faculty.csv') as fac:
        emails = get_from_dict_list('email', read_dict_list(fac))
        return emails
emails = find_emails()
print emails

domain_counts = defaultdict(int)
for s in emails:
    domain_counts[s.split('@')[1]] += 1
print domain_counts
print len(domain_counts) #4

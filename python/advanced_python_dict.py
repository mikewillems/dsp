# Q6

fac = defaultdict(list)

with open('faculty.csv') as f:
    reader = csv.DictReader(f)
    for m in reader:
        fac[m['name'].split()[-1]].append([
                m[' degree'],
                m[' title'].split(' of')[0],
                m[' email']])

for k,v in fac.items()[:3]:
    print k
    for m in v:
        print m

# Q7

fac = defaultdict(list)

with open('faculty.csv') as f:
    reader = csv.DictReader(f)
    for m in reader:
        names = m['name'].split()
        fac[(names[0],names[-1])] = [
                m[' degree'],
                m[' title'].split(' of')[0],
                m[' email']]

for k,v in fac.items()[:3]:
    print k
    print v
    
# Q8


from operator import itemgetter

for name in sorted(fac.keys(), key=itemgetter(1)):
    print name
    print fac[name]
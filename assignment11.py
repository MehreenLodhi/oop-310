#ASSIGNMENT 11:
#CHAPTER NO. 9:
     #DICTIONARIES
#EXERCISE:

#QUESTION NO.1:

w = dict()
file = open("words.txt")
for line in file :
    words = line.split()
    for word in words :
        if word not in w :
            w[word] = 1
        else :
            w[word] = w[word] + 1
print(w)

#QUESTION NO.2:      

dictionary_days = dict()                       # Initializes the dictionary
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dictionary_days:
            dictionary_days[words[2]] = 1       # First entry
        else:
            dictionary_days[words[2]] += 1      # Additional counts

print(dictionary_days)

#QUESTION NO.3:

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}

#QUESTION NO.5:

dictionary_domains = dict()     
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        atpos = words[1].find('@')               # Position of '@'
        domain = words[1][atpos+1:]              # Store characters after '@'
        if domain not in dictionary_domains:
            dictionary_domains[domain] = 1       # First entry
        else:
            dictionary_domains[domain] += 1      # Additional counts

print(dictionary_domains)
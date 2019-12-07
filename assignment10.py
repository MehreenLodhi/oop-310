#CHAPTER NO. 8
   #LISTS
#EXERCISE:
#QUESTION NO.1:
nom=[1,2,3,4,5,6,7,8,9,10]
def chop(nom):
    del nom[0]
    del nom[-1]
    print(nom)
print chop(nom)
def middle(nom):
    t=nom[1:-1]
    return tell
print middle(nom)

#QUESTION NO.4:
fname = input("Enter file name: ")
fh = open(fname)
lst = list()                       
for line in fh:                    
    word= line.rstrip().split()    
    for element in word:           
        if element in lst:         
            continue               
        else :                     
            lst.append(element)    
lst.sort()                       
print(lst)

#QUSTION NO.5:
fn=input('enter:')
fhand = open(fn)
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'from':
        continue
    print(words[1])
    count += 1
print('There were %d lines in the file with From as the first word' % count)
   
#QUESTION NO.6:         
while True:
    number = 0.0
    input_number
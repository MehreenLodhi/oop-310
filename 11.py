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

#QUESTION NO.2:
f=input()
fhand=open(f)
weekdays = ['Sun','Mon','Tues','Wed','Thu','Fri','Sat']
count=0
for line in fhand:
    words = line.split()
    #print'Debug:'words
    if len(words) == 0: continue
    if words[0]!='From': continue
    if words[2] in weekdays[:]:
     print(words[2])

#QUESTION NO.3:
g=input('file')
fright = open(g)
count = 0
for line in fright:
    words = line.split()
    #print 'Debug:',words
    if (len(words)>0) and (words[0] == 'From'):
      print(words[2])

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
    input_number = input('Enter a number: ')
    if input_number == 'done':
        break

    try:
        number = float(input_number)
    except ValueError:
        print('Invalid input')
        quit()

    my_list.append(input_number)

print('Maximum: ', max(my_list))
print('Minimum: ', min(my_list))

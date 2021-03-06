import os
import string
#Ask the user a file direction
directory= input('Select a directory (with double \): ')
try:
    os.chdir(directory)
except:
    print('Can not find', directory, 'pathway')
    exit()
#Ask the user for the exact file they want to open
name=input('Por favor, introduzca el nombre del fichero: ')
try:
    txt=open(name)
except:
    print('Can not find', name, 'in', directory)
    exit()
d=dict()
#loops to obtain a dictionary with this format: {'letter':'frequency'}
for line in txt:
    line_strip=line.strip()
    line_punc=line_strip.translate(str.maketrans('','' ,string.punctuation)) #eliminates every symbol except for letters and numbers
    line_lower=line_punc.lower() #transforms capital letters into lower letters
    words=line_lower.split() #create a list of word for every line
    for word in words:
        for letter in word: #2 loops to reach letter level
            d[letter]=d.get(letter,0)+1 #if the letter is already in the dictionary ads 1 to the actual value, else enter the letter in the dictionary as a key and the value is now 1
lista=list()
counter=0
for (letter,number) in d.items():
    if letter>'9': #eliminates numeric entries
        lista.append((number,letter))
        counter=counter+number #total of letters in the text
lista.sort(reverse=True) #sort the list from the most frequent letter to the least
for frequency,letter in lista:
    print(letter, 'Total frequency: ', frequency, 'Relative frequency: ', frequency/counter)
    if frequency == 1358: #An easter egg, like a signature.
        print('That is my number, go get one yourself!')
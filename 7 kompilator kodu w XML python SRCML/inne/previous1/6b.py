# -*- coding: cp1250 -*-
import locale,urllib2
locale.setlocale(locale.LC_ALL, '')

onlineNames = urllib2.urlopen('https://hackz.googlecode.com/svn/szuku/imiona.txt').read().strip()
onlineNames = onlineNames.split('\n')
onlinesurNames = urllib2.urlopen('https://hackz.googlecode.com/svn/szuku/nazwiska.txt').read().strip()
onlinesurNames = onlinesurNames.split('\n')

print "Liczba imion: "+str(len(onlineNames))
print "Liczba nazwisk: "+str(len(onlinesurNames))

lista = []
indexName = len(onlineNames);
print indexName
for i in range(len(onlinesurNames)):
    if indexName >= len(onlineNames)-1:
        indexName = 0
    else:
        indexName +=1
    lista.append([i+1, onlinesurNames[i], onlineNames[indexName]])

f = open('db6b.txt', 'w')
fileBuffer = []
for p in lista:
    fileBuffer.append(str(p[0])+' '+p[1]+' '+p[2])
f.write('\n'.join(fileBuffer))
f.close()


print str(len(lista))
'''onlineNames.sort(key=lambda x: locale.strxfrm(x))
for i in range(len(onlineNames)):
    print onlineNames[i]

onlinesurNames.sort(key=lambda x: locale.strxfrm(x))
for i in range(len(onlinesurNames)):
    #print onlinesurNames[i]
    pass
'''




'''
Z danych pobranych w zadaniu 6a wygenerowac liste w postaci:
Numer, Imie, Naziwsko
Liste zapisac do pliku. Po "wykorzystaniu" wszystkich imion nalezy zaczac od
poczatku listy imion. Wpisow w pliku ma byc tyle ile jest nazwisk.
'''

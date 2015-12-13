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
    lista.append([i+1, onlinesurNames[i].decode('utf-8', 'ignore'), onlineNames[indexName].decode('utf-8', 'ignore')])

for i in range(50):
    print str(lista[i][0])+' '+lista[i][1]+' '+lista[i][2]

f = open('db6f.txt', 'w')
fileBuffer = []
for p in lista:
    fileBuffer.append(str(p[0])+' '+p[1].encode("utf8")+' '+p[2].encode("utf8"))
f.write('\n'.join(fileBuffer))
f.close()


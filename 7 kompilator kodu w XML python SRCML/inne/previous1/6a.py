# -*- coding: cp1250 -*-
import locale,urllib2
locale.setlocale(locale.LC_ALL, '')


onlineNames = urllib2.urlopen('https://hackz.googlecode.com/svn/szuku/imiona.txt').read().strip()
onlineNames = onlineNames.split('\n')
onlinesurNames = urllib2.urlopen('https://hackz.googlecode.com/svn/szuku/nazwiska.txt').read().strip()
onlinesurNames = onlinesurNames.split('\n')

onlineNames.sort(key=lambda x: locale.strxfrm(x))
for i in range(len(onlineNames)):
    print onlineNames[i]


onlinesurNames.sort(key=lambda x: locale.strxfrm(x))
for i in range(len(onlinesurNames)):
    #print onlinesurNames[i]
    pass

print "Liczba imion: "+str(len(onlineNames))
print "Liczba nazwisk: "+str(len(onlinesurNames))



'''
W skrypcie prosze pobrac imiona z linku ponizej, posorotowac, wystwietlic
posortowana liste i liczbe rekordow. To samo nalezy zrobic z lista nazwisk.
Imiona:
https://hackz.googlecode.com/svn/szuku/imiona.txt
Nazwiska:
https://hackz.googlecode.com/svn/szuku/nazwiska.txt
'''

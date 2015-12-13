# -*- coding: cp1250 -*-
import locale, urllib, urllib2
import string, re
locale.setlocale(locale.LC_ALL, '')

of = urllib2.urlopen('http://mmajchr.kis.p.lodz.pl/pwjs/hack.txt').read()
lista = of.split()
najdluzszy = ""
for slowo in lista:
    if len(slowo) > len(najdluzszy):
        litera = re.compile('([^aeiou]){1}', re.IGNORECASE)
        if litera.search(slowo):
            p = re.compile("^([aeiou])*((["+litera.search(slowo).group(1)+"])*([aeiou])*)*$", re.IGNORECASE)
            if p.search(slowo):
                najdluzszy = slowo

print of
print "Najdłuższy ciąg modulacyjny: "+najdluzszy

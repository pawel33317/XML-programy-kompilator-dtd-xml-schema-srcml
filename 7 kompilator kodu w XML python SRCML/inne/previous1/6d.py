# -*- coding: cp1250 -*-
import locale
import urllib
import urllib2
import string
locale.setlocale(locale.LC_ALL, '')

of = urllib2.urlopen('http://mmajchr.kis.p.lodz.pl/pwjs/hack.txt').read()
lista = of.split()
lista_bez_znakow = []
licznikSlowaKomputer = 0
licznikPokrewnych = 0
for slowo in lista:
    if slowo.strip(string.punctuation) == 'komputer':
        licznikSlowaKomputer +=1
    if slowo.strip(string.punctuation).startswith('komputer'):
        licznikPokrewnych +=1

print "Slowo komputer wystepuje: "+str(licznikSlowaKomputer)+" razy"
print "Slowa zaczynajace sie od komputer wystepuja "+str(licznikPokrewnych)+" razy"

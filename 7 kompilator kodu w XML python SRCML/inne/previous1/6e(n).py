# -*- coding: cp1250 -*-
import locale, urllib2
locale.setlocale(locale.LC_ALL, '')
of = urllib2.urlopen('http://mmajchr.kis.p.lodz.pl/pwjs/hack.txt').read()
najdluzszy=''
temp=''
lastChar=''
lastCount=0
for i in xrange(len(of)):
    if of[i] in [' ','i','o','u','a','e','p']:
        temp +=of[i]
        if lastChar == of[i]:
            lastCount+=1;
        else:
            lastChar = of[i];
            lastCount=0;
        if lastCount >=3:
            temp=''
    else:
        lastChar = of[i];
        if len(temp)>len(najdluzszy):
            najdluzszy=temp;
            print najdluzszy
        temp=''
print najdluzszy
print "Dlugosc: "+str(len(najdluzszy))


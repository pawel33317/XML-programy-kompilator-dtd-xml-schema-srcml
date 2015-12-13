# -*- coding: cp1250 -*-
from xml.dom import minidom
from xml.dom.minidom import *
import operator


#wykonuje p�tl� while
def whilee(func_name, xmlObject):
    #pobieramy blok z warunkami p�tli
    cond = xmlObject.getElementsByTagName('condition')[0]
    #ilo�� obrot�w p�tli -> sv[func_name][cond.getElementsByTagName('expr')[0].getElementsByTagName('name')[0].childNodes[0].nodeValue]
    #operator wyst�puj�cy w p�tli
    oper = cond.getElementsByTagName('expr')[0].getElementsByTagName('operator')[0].childNodes[0].nodeValue
    #prawa warto�� operatora
    rightVal = int(cond.getElementsByTagName('expr')[0].getElementsByTagName('literal')[0].childNodes[0].nodeValue)
    #lista z funkcjiami operator�w od pythona
    ops = {"==": operator.eq,"!=": operator.ne,"<>": operator.ne,"<": operator.lt,"<=": operator.le,">": operator.gt,">=": operator.ge}
    #p�tla wykonuje sw�j blok
    while ops[oper](sv[func_name][cond.getElementsByTagName('expr')[0].getElementsByTagName('name')[0].childNodes[0].nodeValue],rightVal):
        block_operation(func_name,xmlObject.getElementsByTagName('block')[0])
        #warunek p�cli lewyOperator --- prawyOperator sv[func_name][cond.getElementsByTagName('expr')[0].getElementsByTagName('name')[0].childNodes[0].nodeValue]+" --- "+rightVal


#wywo�uje funkcj�, je�eli wypisz to obs�uguje i wy�wietla wynik
def call_func(func_name, xmlObject):
    #czy nazwa funkcji == wypisz
    if xmlObject.getElementsByTagName('name')[0].childNodes[0].nodeValue == 'wypisz':
        print "Wynik funkcji wypisz: "+str(sv[func_name][xmlObject.getElementsByTagName('argument_list')[0].getElementsByTagName('expr')[0].getElementsByTagName('name')[0].childNodes[0].nodeValue])
    else:
        print "Inna funkcja"



#wykonuje operacj� na zmiennej / wywo�uje funkcje
def expr_stmt(func_name, xmlObject):
    #pobiera blok exp z operacj� na zmiennej
    exp = xmlObject.getElementsByTagName('expr')[0]
    if len(exp.getElementsByTagName('call')) > 0:
        call_func(func_name, exp.getElementsByTagName('call')[0])
        return 
        
    #zmienna na eementy operacji na zmiennej
    exp_parm = {}
    #zmienna sprawdzaj�ca poprawno��
    z = 0
    #lista z funkcjiami operator�w od pythona
    ops = {"opp": operator.add,"opm": operator.sub,"*": operator.mul,"/": operator.div}
    #wpisuje operatory i operandy w tablicy
    for i in xrange(len(exp.childNodes)):
        #je�eli to nie b��d tylko prawdziwy tag xml
        if str(exp.childNodes[i].nodeValue).strip() != "":
            #sprawdzamy czy to warto�� czy nazwa zmiennej z tablicy symboli
            #jak nazwa zmiennej to wypisz jej warto�� z tablicy symboli
            #pierwszym parametrem musi by� nazwa zmiennej do kt�ej chcemy przypisa� wynik operacji do zmiennej 
            if exp.childNodes[i].nodeName == 'name' and z>0:
                exp_parm[z]=sv[func_name][exp.childNodes[i].childNodes[0].nodeValue]
            #je�eli warto�� przypisz do zmienej
            else:        
                exp_parm[z]=exp.childNodes[i].childNodes[0].nodeValue
            z+=1
    #wymagane python nie chce wywo�a� listy po jednym znaku nie literze
    if z == 5:
        if exp_parm[3] == '-':
            exp_parm[3] = "opm"
        if exp_parm[3] == '+':
            exp_parm[3] = "opp"
        #wykonuje operacj� na zmiennej
        sv[func_name][exp_parm[0]]=ops[str(exp_parm[3])](int(exp_parm[2]),int(exp_parm[4]))
    


#przechodzi przez wszystkie operacje w bloku i wywo�uje odpowiednie funkcje   
def block_operation(func_name, blockXmlObject):
    for i in xrange(len(blockXmlObject.childNodes)):
        if str(blockXmlObject.childNodes[i].nodeValue).strip() != "":
            #print blockXmlObject.childNodes[i].nodeName
            if blockXmlObject.childNodes[i].nodeName == 'decl_stmt':
                decl_stmt(func_name,blockXmlObject.childNodes[i])
            if blockXmlObject.childNodes[i].nodeName == 'while':
                whilee(func_name,blockXmlObject.childNodes[i])
            if blockXmlObject.childNodes[i].nodeName == 'expr_stmt':
                expr_stmt(func_name,blockXmlObject.childNodes[i]);
            if blockXmlObject.childNodes[i].nodeName == 'return':
                pass


#deklaracjie w funkcji przydziela zmienn� do odpowiedniej tablicy symboli
def decl_stmt(func_name, xmlObject):
    #pobiera obiekt xml z deklacj�
    dec = xmlObject.getElementsByTagName('decl')[0]
    #typ deklaracji -->  dec.getElementsByTagName('type')[0].getElementsByTagName('name')[0].childNodes[0].nodeValue
    #pobiera nazw� zmiennej kt�r� wrzuci do tablicy symboli
    varName = dec.getElementsByTagName('name')[1].childNodes[0].nodeValue
    #inicjuje warto�ci� 0
    sv[func_name][varName] = 0
    #je�eli by�a warto�� inicjuj�ca zmieniamy na ni�
    if len(dec.getElementsByTagName('init')) > 0:
        sv[func_name][varName]=int(dec.getElementsByTagName('init')[0].getElementsByTagName('expr')[0].getElementsByTagName('literal')[0].childNodes[0].nodeValue)



#tablice symboli dla wszystkich funkcji osobno 
global sv
sv={}


#wczytuje plik i pobiera unit z xml'a powinien by� 1
doc = minidom.parse("msilnia.xml")
unit = doc.getElementsByTagName('unit')
unit = unit[0]


#wyswietla liste funkcji w pliku i tworzy tablice symboli tla ka�dej funkcji
print "Liczba funkcji: "+str(len(unit.getElementsByTagName('function')))
f=unit.getElementsByTagName('function')
#dla ka�dej funkcji tw�rz tablic� symboli
for i in xrange(len(f)):
    sv[str(f[i].getElementsByTagName('name')[1].childNodes[0].nodeValue)]={}
    #wypisz nzaw� funkcji
    print "Nazwa funkcji ["+str(i+1)+"]: "+str(f[i].getElementsByTagName('name')[1].childNodes[0].nodeValue)


#wywoluje kod funkcji (caly blok w pliku xml)
block_operation(f[0].getElementsByTagName('name')[1].childNodes[0].nodeValue,f[0].getElementsByTagName('block')[0])


#wy�wietla tablic� symboli
print sv

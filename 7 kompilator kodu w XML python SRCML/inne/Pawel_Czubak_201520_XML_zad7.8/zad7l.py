# -*- coding: cp1250 -*-
from xml.dom import minidom
from xml.dom.minidom import *
import operator


#wykonuje p�tl� while
def whilee(func_name, xmlObject):
    if DEBUG:
        print "["+str(func_name)+"] Wchodz� do whilee"
        
    #je�eli zosta� rzucony return wyjd�
    if sv[func_name][0] != 'brak':
        if DEBUG:
            print "["+str(func_name)+"] Wychodz� z whilee bo Return"
        return
 
    #pobieramy blok z warunkami p�tli
    cond = xmlObject.getElementsByTagName('condition')[0]
    #sprawdzamy czy operand jest zmienn� czy litera�em
    op={}
    #warto�ci do sprawdzenia warunku p�tli
    value={}
    #licznik operand�w/litera��w
    z=0;

  
    #przelatuje przez warunek i sprawdza czy jest tam warto�� czy zmienna
    for i in xrange(len(cond.getElementsByTagName('expr')[0].childNodes)):
        if str(cond.getElementsByTagName('expr')[0].childNodes[i].nodeValue).strip() != "":
            #je�eli zmienna
            if str(cond.getElementsByTagName('expr')[0].childNodes[i].nodeName) == 'name':
                op[z]=True
                #nazwa zmiennej
                value[z]=cond.getElementsByTagName('expr')[0].childNodes[i].childNodes[0].nodeValue
                z+=1
            #je�eli warto��
            if str(cond.getElementsByTagName('expr')[0].childNodes[i].nodeName) == 'literal':
                op[z]=False
                #warto��
                value[z]=cond.getElementsByTagName('expr')[0].childNodes[i].childNodes[0].nodeValue
                z+=1   


    #operator wyst�puj�cy w p�tli
    oper = cond.getElementsByTagName('expr')[0].getElementsByTagName('operator')[0].childNodes[0].nodeValue
    #lista z funkcjiami operator�w od pythona
    ops = {"==": operator.eq,"!=": operator.ne,"<>": operator.ne,"<": operator.lt,"<=": operator.le,">": operator.gt,">=": operator.ge}


    #je�eli pierwsze to zmienna i drugie te�
    if op[0] and op[1]:
        #p�tla wykonuje sw�j blok
        while ops[oper](sv[func_name][value[0]],sv[func_name][value[1]]):
            block_operation(func_name,xmlObject.getElementsByTagName('block')[0])
            #je�eli return przerwij
            if sv[func_name][0] != 'brak':
                return
            
    #je�eli pierwsze to zmienna a drugie warto��
    elif op[0] and not(op[1]):
        #p�tla wykonuje sw�j blok
        while ops[oper](sv[func_name][value[0]],int(value[1])):
            #je�eli return przerwij
            if sv[func_name][0] != 'brak':
                return
            block_operation(func_name,xmlObject.getElementsByTagName('block')[0]) 
    else:
        print "nie obsluzone"
    
            

#obs�uguje wywo�anie funkcji wypisz (obs�ugiwanej przez pythona do wy�wietlenia wyniku)
def call_func(func_name, xmlObject):
    if DEBUG:
        print "["+str(func_name)+"] Wchodz� do call_func"
        
    #je�eli zosta� rzucony return wyjd�
    if sv[func_name][0] != 'brak':
        if DEBUG:
            print "["+str(func_name)+"] Wychodz� z call_func bo Return"
        return

    #czy nazwa funkcji == wypisz
    if xmlObject.getElementsByTagName('name')[0].childNodes[0].nodeValue == 'wypisz':
        print "Wynik funkcji wypisz: "+str(sv[func_name][xmlObject.getElementsByTagName('argument_list')[0].getElementsByTagName('expr')[0].getElementsByTagName('name')[0].childNodes[0].nodeValue])
    else:
        #pocz�tkowo call_func mia�� obs�ugiwa� wywo�anie ka�dej funkcji ale okaza�o si� to zb�dne
        #print "Inna funkcja: "+xmlObject.getElementsByTagName('name')[0].childNodes[0].nodeValue
        pass


def returnn(func_name, xmlObject):
    if DEBUG:
        print "["+str(func_name)+"] Wchodz� do returnn"
        
    #je�eli zosta� rzucony return wyjd�
    if sv[func_name][0] != 'brak':
        if DEBUG:
            print "["+str(func_name)+"] Wychodz� z returnn bo Return"
        return

    #rzuca return czyli ustawia w danej fujkcji sv[func][0] wrto��
    if(len(xmlObject.getElementsByTagName('expr')[0].getElementsByTagName('name'))>0):
        sv[func_name][0]=xmlObject.getElementsByTagName('expr')[0].getElementsByTagName('name')[0].childNodes[0].nodeValue
    return


#wykonuje operacj� na zmiennej / wywo�uje funkcje
def expr_stmt(func_name, xmlObject):
    if DEBUG:
        print "["+str(func_name)+"] Wchodz� do expr_stmt"
        
    #je�eli zosta� rzucony return wyjd�
    if sv[func_name][0] != 'brak':
        if DEBUG:
            print "["+str(func_name)+"] Wychodz� z expr_stmt bo Return"
        return

    
    #pobiera blok exp z operacjami na zmiennej litera�y, zmienne, operator
    exp = xmlObject.getElementsByTagName('expr')[0]


    #je�eli jest to jedynie wywo�anie funkcji wywi�uje j� (wypisz)
    if len(exp.getElementsByTagName('call')) > 0:
        call_func(func_name, exp.getElementsByTagName('call')[0])
        return 

        
    #zmienna na elementy operacji na zmiennej
    exp_parm = {}
    #zmienna sprawdzaj�ca poprawno��
    z = 0

    
    #lista z funkcjiami operator�w od pythona
    ops = {"opp": operator.add,"opm": operator.sub,"opw": operator.mul,"/": operator.div,"%": operator.mod}

    
    #wpisuje operatory i operandy do tablicy exp_parm
    for i in xrange(len(exp.childNodes)):
        
        #je�eli to nie b��d tylko prawdziwy tag xml
        if str(exp.childNodes[i].nodeValue).strip() != "":

            
            #sprawdzamy czy to warto�� czy nazwa zmiennej z tablicy symboli
            #jak nazwa zmiennej to wypisz jej warto�� z tablicy symboli
            #pierwszym parametrem musi by� nazwa zmiennej do kt�ej chcemy przypisa� wynik operacji na zmiennej (z>0)
            if exp.childNodes[i].nodeName == 'name' and z>0:
                exp_parm[z]=sv[func_name][exp.childNodes[i].childNodes[0].nodeValue]
                
            #je�eli tablica wpisz jej nazw�
            elif exp.childNodes[i].nodeName == 'array_name':
                #wartosc indeksu tablicy --> print sv[func_name][exp.childNodes[i].getElementsByTagName('name')[0].childNodes[0].nodeValue][sv[func_name][exp.childNodes[i].getElementsByTagName('index')[0].childNodes[0].nodeValue]]
                exp_parm[z]=sv[func_name][exp.childNodes[i].getElementsByTagName('name')[0].childNodes[0].nodeValue][sv[func_name][exp.childNodes[i].getElementsByTagName('index')[0].childNodes[0].nodeValue]]

            #je�eli warto�� przypisz do zmienej
            else:
                exp_parm[z]=exp.childNodes[i].childNodes[0].nodeValue
            z+=1

            
    #wymagane python nie chce wywo�a� listy po jednym znaku nie literze
    #czyli zamiana np * na opw �eby mo�na by�o wyci�gn�� z tablicy
    if z == 5:
        if exp_parm[3] == '-':
            exp_parm[3] = "opm"
        if exp_parm[3] == '+':
            exp_parm[3] = "opp"
        if exp_parm[3] == '*':
            exp_parm[3] = "opw"
            
        #wykonuje operacj� na zmiennej konwertuje operandy do typu zmiennej do kt�rej zostan� przypisane
        if svTypes[func_name][exp_parm[0]] == 'double':
            sv[func_name][exp_parm[0]]=ops[str(exp_parm[3])](float(exp_parm[2]),float(exp_parm[4]))
        else:
            sv[func_name][exp_parm[0]]=ops[str(exp_parm[3])](int(exp_parm[2]),int(exp_parm[4]))


#obs�uguje wywo�anie if�w  
def iff(func_name, xmlObject):
    if DEBUG:
        print "["+str(func_name)+"] Wchodz� do iff"
        
    #je�eli zosta� rzucony return wyjd�
    if sv[func_name][0] != 'brak':
        if DEBUG:
            print "["+str(func_name)+"] Wychodz� z iff bo Return"
        return

    
    value={}
    z=0
    #lista z funkcjiami operator�w od pythona
    ops = {"==": operator.eq,"!=": operator.ne,"<>": operator.ne,"<": operator.lt,"<=": operator.le,">": operator.gt,">=": operator.ge}
    #wyci�ga operator w ifie
    oper=str(xmlObject.getElementsByTagName('condition')[0].getElementsByTagName('expr')[0].getElementsByTagName('operator')[0].childNodes[0].nodeValue)

    #dla ka�dego wyra�enia w ifie (szuka operand�w i operator�w)
    for i in xrange(len(xmlObject.getElementsByTagName('condition')[0].getElementsByTagName('expr')[0].childNodes)):
        #pomija spam
        if str(xmlObject.getElementsByTagName('condition')[0].getElementsByTagName('expr')[0].childNodes[i].nodeValue).strip() != "":

            #skrocenie
            ifob=xmlObject.getElementsByTagName('condition')[0].getElementsByTagName('expr')[0].childNodes[i]

            #je�eli w ifie jest wywo�anie funkcji
            if str(ifob.nodeName) == 'call':
                #pobiera nazw� parametru funkcji do kt�rego ma przes�a� warto��
                func2parm=unit.getElementsByTagName('function')[1].getElementsByTagName('parameter_list')[0].getElementsByTagName('parameter')[0].getElementsByTagName('decl')[0].getElementsByTagName('name')[1].childNodes[0].nodeValue

                #pobiera kod blokowy do wykonania wywo�ywanej funkcji
                func2block=unit.getElementsByTagName('function')[1].getElementsByTagName('block')[0]

                #do parametru funkcji przypisuje warto�� kt�ra ma zosta� przekazana
                sv[ifob.getElementsByTagName('name')[0].childNodes[0].nodeValue][func2parm]=sv[func_name][ifob.getElementsByTagName('name')[1].childNodes[0].nodeValue]
                sv[ifob.getElementsByTagName('name')[0].childNodes[0].nodeValue][0]='brak'

                ##########wywoluje funkcje################
                block_operation(ifob.getElementsByTagName('name')[0].childNodes[0].nodeValue, func2block)
                #funkcja powinna zwr�ci� wynik w sv[nazwa_funkcji][0]

                #do operandu ifa wrzuca wynik funkcji
                value[z]=sv[unit.getElementsByTagName('function')[1].getElementsByTagName('name')[1].childNodes[0].nodeValue][0]
                #print "funnkcja zwr�ci�a: "+str(value[z])

                #zwi�ksza na kolejny operand/operator
                z+=1

            #je�li w operandzie ifa by�a nazwa zmiennej a nie litera� lub true/false
            if str(ifob.nodeName) == 'name':
                if str(ifob.childNodes[0].nodeValue).strip() == 'true':
                    value[z]=ifob.childNodes[0].nodeValue
                elif str(ifob.childNodes[0].nodeValue).strip() == 'false':
                    value[z]=ifob.childNodes[0].nodeValue
                else:
                    value[z]=sv[func_name][ifob.childNodes[0].nodeValue]
                #zwi�ksza na kolejny operand/operator
                z+=1
            
            #je�eli warto�� (litera�)
            if str(ifob.nodeName) == 'literal':
                value[z]=ifob.childNodes[0].nodeValue
                #zwi�ksza na kolejny operand/operator
                z+=1

    #konwertuje na inta je�eli nie by�o true lub false
    if str(value[0]) != "false" and value[1] != 'true' and  value[0] != 'true' and value[1] != 'false':
        value[0]=int(value[0])
        value[1]=int(value[1])

    #je�eli wynik ofa ok wykonuje jego blok
    if ops[oper](value[0],value[1]):
        block_operation(func_name, xmlObject.getElementsByTagName('then')[0].getElementsByTagName('block')[0])


#koncepcja return b�dzie zapisywa� w funkcji wywo��nej sv[func][0]to co ma zwroci� a finkcja ktora ja wywolala sobie odczyta
#przechodzi przez wszystkie operacje w bloku i wywo�uje odpowiednie funkcje   
def block_operation(func_name, blockXmlObject):
    if DEBUG:
        print "["+str(func_name)+"] Wchodz� do block_operation"
        
    #je�eli zosta� rzucony return wyjd�
    if sv[func_name][0] != 'brak':
        if DEBUG:
            print "["+str(func_name)+"] Wychodz� z block_operation bo Return"
        return

    #przechodzi przez wszyskie operacje w bloku i wywo�uje odpowiedni� metod�
    for i in xrange(len(blockXmlObject.childNodes)):
        if str(blockXmlObject.childNodes[i].nodeValue).strip() != "":
            if blockXmlObject.childNodes[i].nodeName == 'decl_stmt':
                decl_stmt(func_name,blockXmlObject.childNodes[i])
            if blockXmlObject.childNodes[i].nodeName == 'while':
                whilee(func_name,blockXmlObject.childNodes[i])
            if blockXmlObject.childNodes[i].nodeName == 'expr_stmt':
                expr_stmt(func_name,blockXmlObject.childNodes[i]);
            if blockXmlObject.childNodes[i].nodeName == 'if':
                iff(func_name,blockXmlObject.childNodes[i]);
            if blockXmlObject.childNodes[i].nodeName == 'return':
                returnn(func_name,blockXmlObject.childNodes[i]);


#deklaracjie w funkcji przydziela zmienn� do odpowiedniej tablicy symboli
def decl_stmt(func_name, xmlObject):
    if DEBUG:
        print "["+str(func_name)+"] Wchodz� do decl_stmt"
        
    #je�eli zosta� rzucony return wyjd�
    if sv[func_name][0] != 'brak':
        if DEBUG:
            print "["+str(func_name)+"] Wychodz� z decl_stmt bo Return"
        return

    #pobiera obiekt xml z deklacj�
    dec = xmlObject.getElementsByTagName('decl')[0]


    #pobiera nazw� zmiennej kt�r� wrzuci do tablicy symboli danej funkcji
    varName = dec.getElementsByTagName('name')[1].childNodes[0].nodeValue
    #wrzuca do tablicy symboli nazw� zmiennej
    svTypes[func_name][varName] = dec.getElementsByTagName('name')[0].childNodes[0].nodeValue


    #inicjacja pocz�tkowej warto�ci zmiennej
    
    #je�eli to tablica a nie zmienna
    if len(dec.getElementsByTagName('name')[1].getElementsByTagName('index')) > 0:

        
        #je�eli to jest tablica nazwa jest gdzie indziej to zmie�
        varName = dec.getElementsByTagName('name')[1].getElementsByTagName('name')[0].childNodes[0].nodeValue
        #ustawia �e tablica
        sv[func_name][varName] = {}
    
        z = 0
        #dla kazdgo elementu tablicy w xml
        for i in xrange(len(dec.getElementsByTagName('init')[0].getElementsByTagName('expr')[0].getElementsByTagName('block')[0].childNodes)):
            
            #pobiera warto�� kolejnego indeksu
            ob=dec.getElementsByTagName('init')[0].getElementsByTagName('expr')[0].getElementsByTagName('block')[0].childNodes[i]
            
            #je�eli to nie b��d tylko prawdziwy tag xml
            if str(ob.nodeValue).strip() != "":
                #przypisuje warto�� kolejnego indeksu
                sv[func_name][varName][z]=ob.getElementsByTagName('literal')[0].childNodes[0].nodeValue
                z+=1
        z-=1

    #je�eli zwyk�a zmianna
    else:    
        #inicjuje warto�ci� 0
        sv[func_name][varName] = 0
        #je�eli by�a warto�� inicjuj�ca zmieniamy na ni�
        if len(dec.getElementsByTagName('init')) > 0:
            sv[func_name][varName]=int(dec.getElementsByTagName('init')[0].getElementsByTagName('expr')[0].getElementsByTagName('literal')[0].childNodes[0].nodeValue)
    

#w��cza debugowanie
global DEBUG
DEBUG=False
#tablice symboli dla wszystkich funkcji osobno 
global sv
sv={}
#tablica z typami zmiennych dla funkcji
global svTypes
svTypes={}



#wczytuje plik i pobiera unit z xml'a powinien by� 1
FILE="msrednia.xml"
print "Wczytany plik: "+FILE
doc = minidom.parse(FILE)
unit = doc.getElementsByTagName('unit')
global unit
unit = unit[0]


#wyswietla liste funkcji w pliku i tworzy tablice symboli tla ka�dej funkcji
print "Liczba funkcji: "+str(len(unit.getElementsByTagName('function')))
funkcja=unit.getElementsByTagName('function')
#dla ka�dej funkcji tw�rz tablic� symboli
for i in xrange(len(funkcja)):
    sv[str(funkcja[i].getElementsByTagName('name')[1].childNodes[0].nodeValue)]={}
    svTypes[str(funkcja[i].getElementsByTagName('name')[1].childNodes[0].nodeValue)]={}
    sv[str(funkcja[i].getElementsByTagName('name')[1].childNodes[0].nodeValue)][0]='brak'
    #wypisz nzaw� funkcji
    print "Nazwa funkcji ["+str(i+1)+"]: "+str(funkcja[i].getElementsByTagName('name')[1].childNodes[0].nodeValue)
print "-----------------------------------"

#wywoluje pierwsz� funkcj� w pliku
block_operation(funkcja[0].getElementsByTagName('name')[1].childNodes[0].nodeValue,funkcja[0].getElementsByTagName('block')[0])


#wy�wietla na koniec tablice symboli
print "-----------------------------------"
print "Tablica symboli: "+str(sv)
print "Tablica z typami zmiennych: "+str(svTypes)

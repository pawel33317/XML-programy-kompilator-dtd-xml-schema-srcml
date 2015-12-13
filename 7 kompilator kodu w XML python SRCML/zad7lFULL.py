# -*- coding: cp1250 -*-
from xml.dom import minidom
from xml.dom.minidom import *
import operator


#wykonuje pętlę while
def whilee(func_name, xmlObject):
    if DEBUG:
        print "["+str(func_name)+"] Wchodzę do whilee"
        
    #jeżeli został rzucony return wyjdź
    if sv[func_name][0] != 'brak':
        if DEBUG:
            print "["+str(func_name)+"] Wychodzę z whilee bo Return"
        return
 
    #pobieramy blok z warunkami pętli
    cond = xmlObject.getElementsByTagName('condition')[0]
    #sprawdzamy czy operand jest zmienną czy literałem
    op={}
    #wartości do sprawdzenia warunku pętli
    value={}
    #licznik operandów/literałów
    z=0;

  
    #przelatuje przez warunek i sprawdza czy jest tam wartość czy zmienna
    for i in xrange(len(cond.getElementsByTagName('expr')[0].childNodes)):
        if str(cond.getElementsByTagName('expr')[0].childNodes[i].nodeValue).strip() != "":
            #jeżeli zmienna
            if str(cond.getElementsByTagName('expr')[0].childNodes[i].nodeName) == 'name':
                op[z]=True
                #nazwa zmiennej
                value[z]=cond.getElementsByTagName('expr')[0].childNodes[i].childNodes[0].nodeValue
                z+=1
            #jeżeli wartość
            if str(cond.getElementsByTagName('expr')[0].childNodes[i].nodeName) == 'literal':
                op[z]=False
                #wartość
                value[z]=cond.getElementsByTagName('expr')[0].childNodes[i].childNodes[0].nodeValue
                z+=1   


    #operator występujący w pętli
    oper = cond.getElementsByTagName('expr')[0].getElementsByTagName('operator')[0].childNodes[0].nodeValue
    #lista z funkcjiami operatorów od pythona
    ops = {"==": operator.eq,"!=": operator.ne,"<>": operator.ne,"<": operator.lt,"<=": operator.le,">": operator.gt,">=": operator.ge}


    #jeżeli pierwsze to zmienna i drugie też
    if op[0] and op[1]:
        #pętla wykonuje swój blok
        while ops[oper](sv[func_name][value[0]],sv[func_name][value[1]]):
            block_operation(func_name,xmlObject.getElementsByTagName('block')[0])
            #jeżeli return przerwij
            if sv[func_name][0] != 'brak':
                return
            
    #jeżeli pierwsze to zmienna a drugie wartość
    elif op[0] and not(op[1]):
        #pętla wykonuje swój blok
        while ops[oper](sv[func_name][value[0]],int(value[1])):
            #jeżeli return przerwij
            if sv[func_name][0] != 'brak':
                return
            block_operation(func_name,xmlObject.getElementsByTagName('block')[0]) 
    else:
        print "nie obsluzone"
    
            

#obsługuje wywołanie funkcji wypisz (obsługiwanej przez pythona do wyświetlenia wyniku)
def call_func(func_name, xmlObject):
    if DEBUG:
        print "["+str(func_name)+"] Wchodzę do call_func"
        
    #jeżeli został rzucony return wyjdź
    if sv[func_name][0] != 'brak':
        if DEBUG:
            print "["+str(func_name)+"] Wychodzę z call_func bo Return"
        return

    #czy nazwa funkcji == wypisz
    if xmlObject.getElementsByTagName('name')[0].childNodes[0].nodeValue == 'wypisz':
        print "Wynik funkcji wypisz: "+str(sv[func_name][xmlObject.getElementsByTagName('argument_list')[0].getElementsByTagName('expr')[0].getElementsByTagName('name')[0].childNodes[0].nodeValue])
    else:
        #początkowo call_func miałą obsługiwać wywołanie każdej funkcji ale okazało się to zbędne
        #print "Inna funkcja: "+xmlObject.getElementsByTagName('name')[0].childNodes[0].nodeValue
        pass


def returnn(func_name, xmlObject):
    if DEBUG:
        print "["+str(func_name)+"] Wchodzę do returnn"
        
    #jeżeli został rzucony return wyjdź
    if sv[func_name][0] != 'brak':
        if DEBUG:
            print "["+str(func_name)+"] Wychodzę z returnn bo Return"
        return

    #rzuca return czyli ustawia w danej fujkcji sv[func][0] wrtość
    if(len(xmlObject.getElementsByTagName('expr')[0].getElementsByTagName('name'))>0):
        sv[func_name][0]=xmlObject.getElementsByTagName('expr')[0].getElementsByTagName('name')[0].childNodes[0].nodeValue
    return


#wykonuje operację na zmiennej / wywołuje funkcje
def expr_stmt(func_name, xmlObject):
    if DEBUG:
        print "["+str(func_name)+"] Wchodzę do expr_stmt"
        
    #jeżeli został rzucony return wyjdź
    if sv[func_name][0] != 'brak':
        if DEBUG:
            print "["+str(func_name)+"] Wychodzę z expr_stmt bo Return"
        return

    
    #pobiera blok exp z operacjami na zmiennej literały, zmienne, operator
    exp = xmlObject.getElementsByTagName('expr')[0]


    #jeżeli jest to jedynie wywołanie funkcji wywiłuje ją (wypisz)
    if len(exp.getElementsByTagName('call')) > 0:
        call_func(func_name, exp.getElementsByTagName('call')[0])
        return 

        
    #zmienna na elementy operacji na zmiennej
    exp_parm = {}
    #zmienna sprawdzająca poprawność
    z = 0

    
    #lista z funkcjiami operatorów od pythona
    ops = {"opp": operator.add,"opm": operator.sub,"opw": operator.mul,"/": operator.div,"%": operator.mod}

    
    #wpisuje operatory i operandy do tablicy exp_parm
    for i in xrange(len(exp.childNodes)):
        
        #jeżeli to nie błąd tylko prawdziwy tag xml
        if str(exp.childNodes[i].nodeValue).strip() != "":

            
            #sprawdzamy czy to wartość czy nazwa zmiennej z tablicy symboli
            #jak nazwa zmiennej to wypisz jej wartość z tablicy symboli
            #pierwszym parametrem musi być nazwa zmiennej do któej chcemy przypisać wynik operacji na zmiennej (z>0)
            if exp.childNodes[i].nodeName == 'name' and z>0:
                exp_parm[z]=sv[func_name][exp.childNodes[i].childNodes[0].nodeValue]
                
            #jeżeli tablica wpisz jej nazwę
            elif exp.childNodes[i].nodeName == 'array_name':
                #wartosc indeksu tablicy --> print sv[func_name][exp.childNodes[i].getElementsByTagName('name')[0].childNodes[0].nodeValue][sv[func_name][exp.childNodes[i].getElementsByTagName('index')[0].childNodes[0].nodeValue]]
                exp_parm[z]=sv[func_name][exp.childNodes[i].getElementsByTagName('name')[0].childNodes[0].nodeValue][sv[func_name][exp.childNodes[i].getElementsByTagName('index')[0].childNodes[0].nodeValue]]

            #jeżeli wartość przypisz do zmienej
            else:
                exp_parm[z]=exp.childNodes[i].childNodes[0].nodeValue
            z+=1

            
    #wymagane python nie chce wywołać listy po jednym znaku nie literze
    #czyli zamiana np * na opw żeby można było wyciągnąć z tablicy
    if z == 5:
        if exp_parm[3] == '-':
            exp_parm[3] = "opm"
        if exp_parm[3] == '+':
            exp_parm[3] = "opp"
        if exp_parm[3] == '*':
            exp_parm[3] = "opw"
            
        #wykonuje operację na zmiennej konwertuje operandy do typu zmiennej do której zostaną przypisane
        if svTypes[func_name][exp_parm[0]] == 'double':
            sv[func_name][exp_parm[0]]=ops[str(exp_parm[3])](float(exp_parm[2]),float(exp_parm[4]))
        else:
            sv[func_name][exp_parm[0]]=ops[str(exp_parm[3])](int(exp_parm[2]),int(exp_parm[4]))


#obsługuje wywołanie ifów  
def iff(func_name, xmlObject):
    if DEBUG:
        print "["+str(func_name)+"] Wchodzę do iff"
        
    #jeżeli został rzucony return wyjdź
    if sv[func_name][0] != 'brak':
        if DEBUG:
            print "["+str(func_name)+"] Wychodzę z iff bo Return"
        return

    
    value={}
    z=0
    #lista z funkcjiami operatorów od pythona
    ops = {"==": operator.eq,"!=": operator.ne,"<>": operator.ne,"<": operator.lt,"<=": operator.le,">": operator.gt,">=": operator.ge}
    #wyciąga operator w ifie
    oper=str(xmlObject.getElementsByTagName('condition')[0].getElementsByTagName('expr')[0].getElementsByTagName('operator')[0].childNodes[0].nodeValue)

    #dla każdego wyrażenia w ifie (szuka operandów i operatorów)
    for i in xrange(len(xmlObject.getElementsByTagName('condition')[0].getElementsByTagName('expr')[0].childNodes)):
        #pomija spam
        if str(xmlObject.getElementsByTagName('condition')[0].getElementsByTagName('expr')[0].childNodes[i].nodeValue).strip() != "":

            #skrocenie
            ifob=xmlObject.getElementsByTagName('condition')[0].getElementsByTagName('expr')[0].childNodes[i]

            #jeżeli w ifie jest wywołanie funkcji
            if str(ifob.nodeName) == 'call':
                #pobiera nazwę parametru funkcji do którego ma przesłać wartość
                func2parm=unit.getElementsByTagName('function')[1].getElementsByTagName('parameter_list')[0].getElementsByTagName('parameter')[0].getElementsByTagName('decl')[0].getElementsByTagName('name')[1].childNodes[0].nodeValue

                #pobiera kod blokowy do wykonania wywoływanej funkcji
                func2block=unit.getElementsByTagName('function')[1].getElementsByTagName('block')[0]

                #do parametru funkcji przypisuje wartość która ma zostać przekazana
                sv[ifob.getElementsByTagName('name')[0].childNodes[0].nodeValue][func2parm]=sv[func_name][ifob.getElementsByTagName('name')[1].childNodes[0].nodeValue]
                sv[ifob.getElementsByTagName('name')[0].childNodes[0].nodeValue][0]='brak'

                ##########wywoluje funkcje################
                block_operation(ifob.getElementsByTagName('name')[0].childNodes[0].nodeValue, func2block)
                #funkcja powinna zwrócić wynik w sv[nazwa_funkcji][0]

                #do operandu ifa wrzuca wynik funkcji
                value[z]=sv[unit.getElementsByTagName('function')[1].getElementsByTagName('name')[1].childNodes[0].nodeValue][0]
                #print "funnkcja zwróciła: "+str(value[z])

                #zwiększa na kolejny operand/operator
                z+=1

            #jeżli w operandzie ifa była nazwa zmiennej a nie literał lub true/false
            if str(ifob.nodeName) == 'name':
                if str(ifob.childNodes[0].nodeValue).strip() == 'true':
                    value[z]=ifob.childNodes[0].nodeValue
                elif str(ifob.childNodes[0].nodeValue).strip() == 'false':
                    value[z]=ifob.childNodes[0].nodeValue
                else:
                    value[z]=sv[func_name][ifob.childNodes[0].nodeValue]
                #zwiększa na kolejny operand/operator
                z+=1
            
            #jeżeli wartość (literał)
            if str(ifob.nodeName) == 'literal':
                value[z]=ifob.childNodes[0].nodeValue
                #zwiększa na kolejny operand/operator
                z+=1

    #konwertuje na inta jeżeli nie było true lub false
    if str(value[0]) != "false" and value[1] != 'true' and  value[0] != 'true' and value[1] != 'false':
        value[0]=int(value[0])
        value[1]=int(value[1])

    #jeżeli wynik ofa ok wykonuje jego blok
    if ops[oper](value[0],value[1]):
        block_operation(func_name, xmlObject.getElementsByTagName('then')[0].getElementsByTagName('block')[0])


#koncepcja return będzie zapisywał w funkcji wywołąnej sv[func][0]to co ma zwrocić a finkcja ktora ja wywolala sobie odczyta
#przechodzi przez wszystkie operacje w bloku i wywołuje odpowiednie funkcje   
def block_operation(func_name, blockXmlObject):
    if DEBUG:
        print "["+str(func_name)+"] Wchodzę do block_operation"
        
    #jeżeli został rzucony return wyjdź
    if sv[func_name][0] != 'brak':
        if DEBUG:
            print "["+str(func_name)+"] Wychodzę z block_operation bo Return"
        return

    #przechodzi przez wszyskie operacje w bloku i wywołuje odpowiednią metodę
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


#deklaracjie w funkcji przydziela zmienną do odpowiedniej tablicy symboli
def decl_stmt(func_name, xmlObject):
    if DEBUG:
        print "["+str(func_name)+"] Wchodzę do decl_stmt"
        
    #jeżeli został rzucony return wyjdź
    if sv[func_name][0] != 'brak':
        if DEBUG:
            print "["+str(func_name)+"] Wychodzę z decl_stmt bo Return"
        return

    #pobiera obiekt xml z deklacją
    dec = xmlObject.getElementsByTagName('decl')[0]


    #pobiera nazwę zmiennej którą wrzuci do tablicy symboli danej funkcji
    varName = dec.getElementsByTagName('name')[1].childNodes[0].nodeValue
    #wrzuca do tablicy symboli nazwę zmiennej
    svTypes[func_name][varName] = dec.getElementsByTagName('name')[0].childNodes[0].nodeValue


    #inicjacja początkowej wartości zmiennej
    
    #jeżeli to tablica a nie zmienna
    if len(dec.getElementsByTagName('name')[1].getElementsByTagName('index')) > 0:

        
        #jeżeli to jest tablica nazwa jest gdzie indziej to zmień
        varName = dec.getElementsByTagName('name')[1].getElementsByTagName('name')[0].childNodes[0].nodeValue
        #ustawia że tablica
        sv[func_name][varName] = {}
    
        z = 0
        #dla kazdgo elementu tablicy w xml
        for i in xrange(len(dec.getElementsByTagName('init')[0].getElementsByTagName('expr')[0].getElementsByTagName('block')[0].childNodes)):
            
            #pobiera wartość kolejnego indeksu
            ob=dec.getElementsByTagName('init')[0].getElementsByTagName('expr')[0].getElementsByTagName('block')[0].childNodes[i]
            
            #jeżeli to nie błąd tylko prawdziwy tag xml
            if str(ob.nodeValue).strip() != "":
                #przypisuje wartość kolejnego indeksu
                sv[func_name][varName][z]=ob.getElementsByTagName('literal')[0].childNodes[0].nodeValue
                z+=1
        z-=1

    #jeżeli zwykła zmianna
    else:    
        #inicjuje wartością 0
        sv[func_name][varName] = 0
        #jeżeli była wartość inicjująca zmieniamy na nią
        if len(dec.getElementsByTagName('init')) > 0:
            sv[func_name][varName]=int(dec.getElementsByTagName('init')[0].getElementsByTagName('expr')[0].getElementsByTagName('literal')[0].childNodes[0].nodeValue)
    

#włącza debugowanie
global DEBUG
DEBUG=False
#tablice symboli dla wszystkich funkcji osobno 
global sv
sv={}
#tablica z typami zmiennych dla funkcji
global svTypes
svTypes={}



#wczytuje plik i pobiera unit z xml'a powinien być 1
FILE="msrednia.xml"
print "Wczytany plik: "+FILE
doc = minidom.parse(FILE)
unit = doc.getElementsByTagName('unit')
global unit
unit = unit[0]


#wyswietla liste funkcji w pliku i tworzy tablice symboli tla każdej funkcji
print "Liczba funkcji: "+str(len(unit.getElementsByTagName('function')))
funkcja=unit.getElementsByTagName('function')
#dla każdej funkcji twórz tablicę symboli
for i in xrange(len(funkcja)):
    sv[str(funkcja[i].getElementsByTagName('name')[1].childNodes[0].nodeValue)]={}
    svTypes[str(funkcja[i].getElementsByTagName('name')[1].childNodes[0].nodeValue)]={}
    sv[str(funkcja[i].getElementsByTagName('name')[1].childNodes[0].nodeValue)][0]='brak'
    #wypisz nzawę funkcji
    print "Nazwa funkcji ["+str(i+1)+"]: "+str(funkcja[i].getElementsByTagName('name')[1].childNodes[0].nodeValue)
print "-----------------------------------"

#wywoluje pierwszę funkcję w pliku
block_operation(funkcja[0].getElementsByTagName('name')[1].childNodes[0].nodeValue,funkcja[0].getElementsByTagName('block')[0])


#wyświetla na koniec tablice symboli
print "-----------------------------------"
print "Tablica symboli: "+str(sv)
print "Tablica z typami zmiennych: "+str(svTypes)

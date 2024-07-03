import csv
import pandas as pd
import os, time
import datetime as dt
import os.path
"""

Projekt: Banksystem

Klass Person
-kunder
-personal(extra)

"""
#skapa class Person med kunder och personalser som deltagande class
class Person:
    def __init__(self, namn, pnum, adress):
        self.namn = namn
        self.pnum = pnum
        self.adress = adress
        
    
    def sub_namn(self):
        return self.namn
    
    def sub_nummer(self):
        return self.pnum
    
    def sub_adress(self):
        return self.adress
    
class Kund(Person):
    def __init__(self, namn, pnum, adress):
        Person.__init__(self, namn, pnum, adress)
        
    def skapa_fil(self):
        while True:
            self.reader = bank.nummer_reader()
            if self.reader != bank.generator():
                fil.csv_wo_header()
                os.system("clear")
                header = ["Användarnamn", "Kontonummer", "Saldo", "Historik", "Datum"]
                pengar_skap = [namn, reader, 0, "Skapas", bank.datum()]
                with open(namn + ".csv", "a") as individ:
                    skapa = csv.writer(individ)
                    skapa.writerow(header)
                    skapa.writerow(pengar_skap)
                break
            else:
                bank.generator()
                os.system("clear")
                break
    #skapa individuella konto
    
class Personal(Person):
    def __init__(self, namn, pnum, adress):
        Person.__init__(self, namn, pnum, adress)
      
        
    def skapa_pers(self):
        with open("Personal.csv", "a", newline= "") as personal_konto:
            
        
    def personal_s(self):
        header = ["Användarnamn", "Kontonummer", "Saldo", "Historik", "Datum"]
        pengar_skap = [namn, reader, 0, "Skapas", bank.datum()]
        with open(namn + ".csv", "a") as individ:
            skapa = csv.writer(individ)
            skapa.writerow(header)
            skapa.writerow(pengar_skap)


    def csv_läs(self):
        self.read_list = pd.read_csv("Kund.csv")
        return self.read_list
    
"""

Registration(Filhantering)
(kontonummer)

"""

#Registerings funktion
class Fil_hand:
    def __init__(self):
        self.lib = {
            "Namn": [],
            "Personnummer": [],
            "Address": [],
            "Kontonummer": []
        }  
     
    def dataframe(self):
        self.data_frame = pd.DataFrame(self.lib) 
          
    #def csv(self):
        #self.data_frame.to_csv("Kund.csv", mode ="a", index = False)
        #print(self.data_frame)
        
    def csv_wo_header(self):
        self.data_frame.to_csv("Kund.csv", mode ="a", index = False, header = False)
        
    def csv_läs(self):
        self.read_list = pd.read_csv("Kund.csv")
        
        return self.read_list
    
    
#class skapa_konto(Fil_hand):
    
    
        
           


"""

Skapa funktion som adderar information in csv
Status: Clear

"""
      
      
"""

Banksystem
Status: På arbete

"""  


class Bankkonto:
    def __init__(self, pengar, namn):
        self.pengar = pengar
        self.namn = namn
        self.k1 = []
        self.k2 = []
        self.pengar_list = []
    #genererar 2 grupp av nummer   
    def generator(self):
        import random
        for num in range(0, 4):
            self.num_list = random.randint(0, 9)
            self.k1.append(self.num_list)
        
        for num2 in range(0, 6):
            self.num_list = random.randint(0, 9)
            self.k2.append(self.num_list)
        #funktionen finns för att ett grupp av nummer står ihop utan "," komma
        self.kb1 =""
        self.kb2 =""
        for q in self.k1:
            self.kb1 = self.kb1+""+str(q)
            
        for w in self.k2:
            self.kb2 = self.kb2+""+str(w)
        #returnerar till Registration funktion 
        self.kontonums = self.kb1 +"-"+self.kb2
        return self.kontonums
            

    def nummer_reader(self):
        self.tag = set()
        self.tag_list = []
        self.readnum = open("Kund.csv", "r")
        self.line = csv.DictReader(self.readnum)
        for row in self.line:
            self.tag_list.append(row["Kontonummer"])
        
        self.readnum.close()
        for self.i in self.tag_list:
            self.tag.add(self.i)
        
        if self.tag == self.kontonums:
            return False
        
        else:
            return self.kb1 +"-"+self.kb2
           
       
        
        
    def datum(self):
        self.dt = dt.datetime.now()
        self.year = self.dt.year
        self.month = self.dt.month
        self.day = self.dt.day
        self.hour = self.dt.hour
        self.minutes = self.dt.minute
        self.second = self.dt.second
        
        self.realtime = str(self.year)+"/"+str(self.month)+"/"+str(self.day) +" "+str(self.hour)+":"+str(self.minutes)+":"+str(self.second)
        return self.realtime
    def sal_read(self):
        
        read_saldo = open(self.namn + ".csv", "r")
        self.saldo_reader = csv.DictReader(read_saldo)
        for row in self.saldo_reader:
            self.pengar_list.append(row["Saldo"])
            
        return self.pengar_list[-1]
    #funktion för att visa uttag eller intag historik
    def sal_read_historik(self):
        
        self.data = pd.read_csv(self.namn + ".csv")
        
        return self.data
    #tar ut funktionen
    def tag_ut(self):
        self.dt = dt.datetime.now()
        self.realtime = str(self.dt.year)+"/"+str(self.dt.month)+"/"+str(self.dt.day) +" "+str(self.dt.hour)+":"+str(self.dt.minute)+":"+str(self.dt.second)
        self.minus = int(self.pengar_list[-1]) - self.pengar
        #tag ut finns if funktionen för att blockera när man vill ta ut mer än pengar som finns i banken
        if int(self.pengar_list[-1]) >= self.pengar:
            with open(self.namn + ".csv", "a", newline = "") as tagin_m:
               fieldnames = ["Användarnamn","Kontonummer", "Saldo", "Historik", "Datum"]
               self.tagin = csv.DictWriter(tagin_m, fieldnames=fieldnames)
               self.pengars = str(self.pengar)
               self.tagin.writerow({"Användarnamn": self.namn, "Kontonummer": "None", "Saldo": self.minus, "Historik": self.pengars + "kr är utsatt", "Datum": self.realtime})
               
        else:
            return False
    #tar in funktionen
    def tag_in(self):
        self.dt = dt.datetime.now()
        self.realtime = str(self.dt.year)+"/"+str(self.dt.month)+"/"+str(self.dt.day) +" "+str(self.dt.hour)+":"+str(self.dt.minute)+":"+str(self.dt.second)
        self.plus = int(self.pengar_list[-1]) + self.pengar
        #tänker att ändra pengar värde i csv fil med write
        with open(self.namn + ".csv", "a", newline = "") as tagin_m:
            fieldnames = ["Användarnamn","Kontonummer", "Saldo", "Historik", "Datum"]
            self.tagin = csv.DictWriter(tagin_m, fieldnames=fieldnames)
            self.pengars = str(self.pengar)
            self.tagin.writerow({"Användarnamn": self.namn, "Kontonummer": "None", "Saldo": self.plus, "Historik": self.pengars + "kr är insatt", "Datum": self.realtime})
                
"""

Registration meny

"""
def Registration():
    #skriver information för registrering
    namn = input("Namn och efternamn: ")
    try:
       pnum = int(input("Personnummer: "))
    
    except ValueError:
        os.system("clear")
        Registration()
    adress = input("Address: ")
    k = Kund(namn, pnum, adress)
    bank = Bankkonto(None, None)
    fil = Fil_hand()
    #adderar information som skriven ovan och tar slumpmässigt kontonummer från bankkonto class
    fil.lib["Namn"].append(k.sub_namn())
    fil.lib["Personnummer"].append(k.sub_nummer())
    fil.lib["Address"].append(k.sub_adress())
    fil.lib["Kontonummer"].append(bank.generator())
    fil.dataframe()
    #letar fil om det inte finns och skapar
    file_search = os.path.exists("Kund.csv")
    if file_search == False:
        header = ["Namn", "Personnummer", "Address", "Kontonummer"]
        with open("Kund.csv","w") as opener:
            op = csv.writer(opener)
            op.writerow(header)
    else:
        pass
    
    
    while True:
        
        reader = bank.nummer_reader()
        if reader != bank.generator():
           fil.csv_wo_header()
           os.system("clear")
           header = ["Användarnamn", "Kontonummer", "Saldo", "Historik", "Datum"]
           pengar_skap = [namn, reader, 0, "Skapas", bank.datum()]
           with open(namn + ".csv", "a") as individ:
                skapa = csv.writer(individ)
                skapa.writerow(header)
                skapa.writerow(pengar_skap)
           break
        else:
           bank.generator()
           os.system("clear")
           break
    #skapa individuella konto
    
        
    print("Konto", bank.nummer_reader())
    
    front()
        
def inlog():
    #logga in meny
    namn = input("Ange namn: ")
    pnum = input("Ange personnummer: ")
    
    namn_list = []
    pnum_list = []
    log_in = open("Kund.csv", "r")
    reader0 = csv.reader(log_in)
    reader = csv.DictReader(log_in)
    #Tar ut hela info av Namn och Personnummer och jämföra namn och personnummer med index
    for row in reader:
        namn_list.append(row["Namn"])
        pnum_list.append(row["Personnummer"])
    
    for line in reader0:
        line.append(namn)
        
    print(namn_list, pnum_list)
    log_in.close()
    while True:
       if namn in namn_list and pnum in pnum_list:
          eq = namn_list.index(namn)
          if str(pnum) == pnum_list[eq]:
             os.system("clear")
             meny(namn)
          else:
             print("Användarnamn och personnummer matchar inte")
             time.sleep(1)
             os.system("clear")
             front()
       elif namn not in namn_list and pnum not in pnum_list:
           print("Det finns inte information av användarnamn och lösenord")
           time.sleep(1)
           os.system("clear")
           front()
       else:
           print("Användarnamn och personnummer matchar inte")
           time.sleep(1)
           os.system("clear")
           front()   
def front():
    #Huvudsida av banken
    print("Välkommen till bank")
    
    print("Väljer metod här: ")
    print("1. Registrering")
    print("2. Logga in")
    print("3. Avsluta")
    
    try:
      alt = int(input("Ange nummer: "))
    except ValueError:
      print("Endast nummer")
      time.sleep(1)
      os.system("clear")
      front()
    #väljer alternativ
    while True:
        if alt == 1:
            os.system("clear")
            Registration()
        elif alt == 2:
            os.system("clear")
            inlog()
        elif alt == 3:
            #tvingar stoppa programmet
            exit()
        else:
            os.system("clear")
            #återkomma sidan
            front()
            
def meny(namn):
    #menyn efter man lycklig loggat in
    print("Välkommen", namn)
    bank = Bankkonto(None, namn)
    print("Din saldo:", bank.sal_read()) 
    print()
    print("Väljer metod här: ")
    print("1. Se Historik")
    print("2. Uttag")
    print("3. Intag")
    print("4. Logga ut")
    print()
    #anger alternativ
    try:
      välj = int(input("Anger ditt alternativ: "))
    except ValueError:
      print("Endast nummer")
      time.sleep(1)
      os.system("clear")
      meny(namn)
    if välj == 4:
        time.sleep(1)
        os.system("clear")
        front()   
    elif välj == 2:
        time.sleep(1)
        os.system("clear")
        uttag(namn)
    elif välj == 3:
        time.sleep(1)
        os.system("clear")
        intag(namn)    
        
    elif välj == 1:
        os.system("clear")
        #läser historik med pandas från csv
        while True:
           print(bank.sal_read_historik())
           fråga = input("Tillbaka? ")
           if fråga == "Ja" or fråga == "ja":
              print("svar")
              os.system("clear")
              meny(namn)
           else:
              continue
    else:
        #återkomma sidan
        meny(namn)

#sätter in pengar med funktionen   
def intag(namn):
    print("Anger nummer: Intag")
    pengar = int(input("Sätta in pengar: "))
    bank = Bankkonto(pengar, namn)
    choice = input("Vill du fortsätta genomförandet? ")
    if choice == "Ja" or choice == "ja":
       os.system("clear")
       bank.sal_read()
       bank.tag_in()
    else:
       os.system("clear")
       
def personal_inlog(namn):
    fil = Fil_hand()
    print("Personalkonto: ", namn)
    print()
    print("1. Visa kundlist")
    print("2. Logga ut")
    print()
    personal_välj = int(input("Ange nummer: "))
    if personal_välj == 1:
        while True:
            os.system("clear")
            print(fil.csv_läs())
            fråga = input("Tillbaka? ")
            if fråga == "Ja" or fråga == "ja":
                print("svar")
                os.system("clear")
                personal_inlog()
            else:
                continue
    if personal_välj == 2:
        os.system("clear")
        front()
        

def uttag(namn):
    print("Anger nummer: Uttag")
    pengar = int(input("Sätta in pengar: "))
    bank = Bankkonto(pengar, namn)
    choice = input("Vill du fortsätta genomförandet? ")
    if choice == "Ja" or choice == "ja":
       bank.sal_read()
       col = bank.tag_ut()
       if col == False:
          print("Du har otillräckligt pengar")
          time.sleep(1)
          os.system("clear")
          
       else:
          os.system("clear")
          
        
        
        
front()
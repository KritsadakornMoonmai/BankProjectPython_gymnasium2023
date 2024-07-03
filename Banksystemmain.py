import csv

class Bankkonto:
    def __init__(self, pengar):
        self.pengar = pengar    
        
    def pengar_list(self):
        self.peng_list = []
        
    def pengar_read(self):    
        with open("Kund1.csv", "r") as self.reader_m:
            self.read_m = csv.reader(self.reader_m)
    
    def peng_app(self):
        self.read_m.append(self.peng_list)
        
    
        
#class saldo(Bankkonto):
    #def __init__(self):
        #with open("Kund.csv", "r") as read_saldo:
           #salldo = saldo.reader(read_saldo)
           #salldo.readline()
    
class uttag(Bankkonto):
    def __init__(self, pengar):
        Bankkonto.__init__(self, pengar)
        
    def tag(self):
        self.minus = peng_list - self.pengar
        
    def tag_ut(self):
        #tänker att ändra pengar värde i csv fil med write
        with open("Kund1.csv", "w") as tagut_m:
            self.tagut = csv.writer(tagut_m)
            self.tagut.writerow(self.minus)
            
#class Intag(Bankkonto):
    #def __init__(self):
        #Bankkonto
        
    #def tar_in(self):
        #self.plus = (gamla pengar)+(matas pengar)
        
    #def tag_in(self):
        #tänker att ändra pengar värde i csv fil med write
        #with open("Kund.csv", "w") as tagut:
            #tagut = csv.writer(pengar)
            #tagut.write(self.plus)(ersätter gamla med nya värde)
            
            
           
fråga = input("uttag?: ")

if fråga == "Ja":
    u = uttag()
    num = int(input("antal: "))
    u.tag(num)
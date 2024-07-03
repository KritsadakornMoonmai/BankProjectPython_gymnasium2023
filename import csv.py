import csv
import pandas as pd


class Bankkonto:
    def __init__(self, pengar):
        self.pengar = pengar
        self.k1 = []
        self.k2 = [] 
        
    def generator(self):
        import random
        for num in range(0, 4):
            self.num_list = random.randint(0, 9)
            self.k1.append(self.num_list)
        
        for num2 in range(0, 6):
            self.num_list = random.randint(0, 9)
            self.k2.append(self.num_list)
            
        return str(self.k1) + "-" + str(self.k2)

    def nummer_reader(self):
        self.tag = set()  
        self.readnum = open("Kund.csv", "r")
        self.line = csv.DictReader(self.readnum)
        for row in self.line:
            self.tag.add(row["Namn"])
           
        self.readnum.close()
        return self.tag
    
 
pengar = int(input("Pengar: "))   
bk = Bankkonto(pengar)
print(bk.generator())

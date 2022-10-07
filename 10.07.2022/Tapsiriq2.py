class isciler():
    
    def __init__(self,ad,soyad,no,maas,diller,invest,):
        
        self.ad=ad
        self.soyad=soyad
        self.no=no
        self.maas=maas
        self.diller=diller
        self.invest=invest
        
        
               
    def informasiya_goster(self):
        print("""
              
              Ad:{}
              Soyad:{}
              No:{}
              Maas:{}
              """.format(self.ad,self.soyad,self.no,self.maas,))
             
    def informasiya_goster_proqramist(self):
              print("""
                    
                    Ad:{}
                    Soyad:{}
                    No:{}
                    Maas:{}
                    Diller:{}
                    """.format(self.ad,self.soyad,self.no,self.maas,self.diller,))
    
    def informasiya_goster_investor(self):
              print("""
                    
                    Ad:{}
                    Soyad:{}
                    No:{}
                    Maas:{}
                    Investisiya:{}
                    """.format(self.ad,self.soyad,self.no,self.maas,self.invest,))
                    
class direktorlar(isciler):
    
    def maas_artir(self,zam_miqdari,):
        
        print("Maaş artırıldı")
        
        self.maas += zam_miqdari

class proqramistler(isciler):
    
    def dil_artir(self,yenidil,):
        
        print("Yeni dil elave olundu")
        
        self.diller.append(yenidil)

class investorlar(isciler):
    def invest_et(self,invest,):
        self.invest+=invest
        print("Investisiya tamamlandi")
        
"""
proq1 = proqramistler("Ali", "Sahibcanov", 1, 1000, [""],0)
proq1.dil_artir("Python")
proq1.informasiya_goster_proqramist()

dir1 = direktorlar("Ali", "Sahibcanov", 1, 1000, [""],0)
dir1.maas_artir(500)
dir1.informasiya_goster()

inv1 = investorlar("Ali", "Sahibcanov", 1, 1000, [""],0)
inv1.invest_et(1000)
inv1.informasiya_goster_investor()
"""
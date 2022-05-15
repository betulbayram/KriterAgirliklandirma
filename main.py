import numpy as np
import math

class Lab2:
    def __init__(self):
        self.aday_sayisi=0
        self.kriter_sayisi=0
        self.kriterMax = 0
        self.kararMatrisi = []
        self.normalizeMatris = []
        self.birlestirme_sayaci=0
        self.sutunToplami = 0
        self.sutun_sayaci = 0
        self.normalize_sayaci = 0
        self.ejMatris = []
        self.entropiMatrisi = []
        self.djToplam = 0
        self.djMatris = []
        self.wjMatris = []
        self.sonucMatris = []
        self.sonucToplam = 0
        self.toplamMatris = []
        self.toplam_sayaci = 0
        self.sawMatris = []
 
    def main(self):
        self.adaySayisiBelirle()
        self.kriterSayisiBelirle()
        self.kriterMaxBelirle()
        self.gosterMatris()
        self.Entropi()
        self.SAW()
        self.siralaSonucu()
    
    def Entropi(self):
        self.normalizeKararMatrisi()
        self.hesaplaEntropiDegeri()
        self.hesaplaAgirlikMatris()
    
    def normalizeKararMatrisi(self):
        for k in range(self.kriter_sayisi):
            self.sutunToplami = 0
            for i in range(self.aday_sayisi):
                self.sutunToplami = self.sutunToplami + self.kararMatrisi[i,self.sutun_sayaci]
            
            for j in range(self.aday_sayisi):
                self.normalizeMatris[j,self.sutun_sayaci] = (self.kararMatrisi[j, self.sutun_sayaci]/self.sutunToplami)
            
            self.sutun_sayaci = self.sutun_sayaci + 1

    def hesaplaEntropiDegeri(self):
        self.entropiMatrisi = np.zeros((self.aday_sayisi,self.kriter_sayisi), dtype=float)
        self.ejMatris = np.zeros(self.kriter_sayisi, dtype=float)
        self.sutun_sayaci = 0
        for k in range(self.kriter_sayisi):
            for j in range(self.aday_sayisi):
                value = self.normalizeMatris[j, self.sutun_sayaci]
                if(value!=0):
                    self.entropiMatrisi[j,self.sutun_sayaci] = (value*(math.log(value)))
                else:
                    self.entropiMatrisi[j,self.sutun_sayaci] = 0
            self.sutun_sayaci = self.sutun_sayaci + 1
        self.sutunToplami = 0
        self.sutun_sayaci = 0
        for a in range(self.kriter_sayisi):
            for i in range(self.aday_sayisi):
                self.sutunToplami = self.sutunToplami + self.entropiMatrisi[i,a] 
            
            self.ejMatris[self.sutun_sayaci] = -(self.sutunToplami*(1/math.log(self.aday_sayisi)))
            self.sutun_sayaci = self.sutun_sayaci + 1

    def hesaplaAgirlikMatris(self):
        self.djMatris = np.zeros(self.kriter_sayisi, dtype=float)
        self.wjMatris = np.zeros(self.kriter_sayisi, dtype=float)

        for j in range(self.kriter_sayisi):
            self.djMatris[j] = 1 - self.ejMatris[j]
        for i in range(self.kriter_sayisi):
            self.djToplam = self.djToplam + self.djMatris[i]
        for k in range(self.kriter_sayisi):
            self.wjMatris[k] = self.djMatris[k] / self.djToplam

    def SAW(self):
        #indeks,sonuc
        self.sonucMatris = np.zeros((self.aday_sayisi,self.kriter_sayisi), dtype=float)
        self.toplamMatris = np.zeros((self.aday_sayisi,2), dtype=float)

        for i in range(self.aday_sayisi):
            for j in range(self.kriter_sayisi):
                self.sonucMatris[i,j]=self.kararMatrisi[i,j]*self.wjMatris[j]
        
        for i in range(self.aday_sayisi):
            self.sonucToplam = 0
            for j in range(self.kriter_sayisi):
                self.sonucToplam = self.sonucToplam + self.sonucMatris[self.toplam_sayaci,j]
            self.toplam_sayaci = self.toplam_sayaci + 1
            self.toplamMatris[i] = (self.toplam_sayaci, self.sonucToplam)

    def siralaSonucu(self):
        self.sawMatris=self.toplamMatris[self.toplamMatris[:, 1].argsort()]
        print("siralanmiş matris")
        print(self.sawMatris)

    def gosterMatris(self):
        print("===============================\nkarar matris")

        print(self.kararMatrisi)

    def olusturRandomSayi(self):
        kriter_matrisi=np.random.randint(self.kriterMax, size=self.aday_sayisi)
        self.olusturKararMatrisi(kriter_matrisi)
    
    def olusturKararMatrisi(self, array):
        for i in range(self.aday_sayisi):
            self.kararMatrisi[i, self.birlestirme_sayaci] = array[i]
            
        self.birlestirme_sayaci = self.birlestirme_sayaci + 1

    def adaySayisiBelirle(self):
        self.aday_sayisi=int(input("aday sayisini girin: "))
        pass

    def kriterSayisiBelirle(self):
        self.kriter_sayisi=int(input("kriter sayisini girin: "))
        self.aday_sayisi = 4
        self.kriter_sayisi = 4
        self.kararMatrisi = np.zeros((self.aday_sayisi,self.kriter_sayisi), dtype=int)

        self.kararMatrisi=([[600,20,-70,20],[800,30,-40,50],[500,15,-80,30],[1500,40,-30,10]])
        self.normalizeMatris = np.zeros((self.aday_sayisi,self.kriter_sayisi), dtype=float)
        
    def kriterMaxBelirle(self):
        count=0
        for i in range(self.kriter_sayisi):
            self.kriterMax = int(input(f"{count+1}. kriter icin max deger belirle: "))
            count=count+1
            self.olusturRandomSayi()

if __name__ == "__main__":
    l=Lab2()
    l.main()
    
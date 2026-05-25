
import string

class PlakaTuringMakinesi:
    def __init__(self, plaka):
        self.bant = list(plaka) + ['_']
        self.kafa = 0
        self.durum = 'q0'
        
        
        self.gecisler = {}
        
        rakamlar = string.digits       
        harfler = string.ascii_uppercase  
        
        for r in rakamlar:
            self.gecisler[('q0', r)] = ('q1', r, 'R')
            
        
        for r in rakamlar:
            self.gecisler[('q1', r)] = ('q2', r, 'R')
            
        
        for h in harfler:
            self.gecisler[('q2', h)] = ('q3', h, 'R')
            
        
        for h in harfler:
            self.gecisler[('q3', h)] = ('q4', h, 'R')
            
        
        for r in rakamlar:
            self.gecisler[('q4', r)] = ('q5', r, 'R')
            
        
        for r in rakamlar:
            self.gecisler[('q5', r)] = ('q6', r, 'R')
            
        
        for r in rakamlar:
            self.gecisler[('q6', r)] = ('q7', r, 'R')
            
    def adim_yazdir(self, okunan, yon):
        bant_icerigi = "".join(self.bant)
        print(f"Durum: {self.durum:2} | Okunan: {okunan:1} | Yön: {yon} | Bant: {bant_icerigi}")

    def calistir(self):
        print("-" * 40)
        while True:
            if self.kafa >= len(self.bant):
                okunan_sembol = '_'
            else:
                okunan_sembol = self.bant[self.kafa]
            
            
            if self.durum == 'q7':
                if okunan_sembol == '_':
                    self.adim_yazdir('boşluk', 'Dur') 
                    print("\nSonuç: KABUL\n") 
                    return True
                else:
                    self.durum = 'RED'
                    
            
            if self.durum == 'RED':
                print("\nSonuç: RED\n") 
                return False
                
            
            anahtar = (self.durum, okunan_sembol)
            
            if anahtar in self.gecisler:
                yeni_durum, yazilacak, yon = self.gecisler[anahtar]
                self.adim_yazdir(okunan_sembol, yon)
                self.bant[self.kafa] = yazilacak
                self.durum = yeni_durum
                if yon == 'R':
                    self.kafa += 1
                elif yon == 'L':
                    self.kafa -= 1
            else:
                self.adim_yazdir(okunan_sembol, 'Dur')
                self.durum = 'RED'


if __name__ == "__main__":
    girdi = input("Lütfen kontrol edilecek plakayı girin: ")
    makine = PlakaTuringMakinesi(girdi)
    makine.calistir()
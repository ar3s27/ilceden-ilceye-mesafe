import pandas as pd
df = pd.read_csv("ilcelerDonusturuldu.csv")

def mesafeGetir(k_il, k_ilce, v_il, v_ilce):
    veri = df[(df['k_il'] == k_il) & (df['k_ilce'] == k_ilce) & 
              (df['v_il'] == v_il) & (df['v_ilce'] == v_ilce)]
    
    mesafe = veri["Toplam Uzunluk(km)"].sum()
    return mesafe

#Değerler
konum_il = 'SİİRT'
konum_ilce = 'TİLLO'
varis_il = 'HAKKARİ'
varis_ilce = 'YÜKSEKOVA'

# Fonksiyonu çağır ve sonucu yazdır
sonuc = mesafeGetir(konum_il,konum_ilce,varis_il,varis_ilce)
print(f"Karşılık gelen toplam uzunluk: {sonuc} km")
print(f"{konum_il} İlinin {konum_ilce} İlçesinden {varis_il} İlinin {varis_ilce} İlçesine Olan Mesafe: {sonuc} km")
# -*- coding: utf-8 -*-

import pandas as pd
df = pd.read_csv("ilcelerDonusturuldu.csv")

def mesafeGetir(k_il, k_ilce, v_il, v_ilce):
    veri = df[(df['k_il'] == k_il) & (df['k_ilce'] == k_ilce) & 
              (df['v_il'] == v_il) & (df['v_ilce'] == v_ilce)]
    
    mesafe = veri["Toplam Uzunluk(km)"].sum()
    return mesafe

konum_il = 'MARDİN'
konum_ilce = 'MERKEZ'
varis_il = 'MARDİN'
varis_ilce = 'MİDYAT'

# Fonksiyonu çeker ve sonucu yazdır
sonuc = mesafeGetir(konum_il,konum_ilce,varis_il,varis_ilce)
print(f"karşılık gelen toplam uzunluk: {sonuc} km")
print(f"{konum_il.upper()} İLİNİN {konum_ilce.upper()} İLÇESİNDEN {varis_il.upper()} İLİNİN {varis_ilce.upper()} İLÇESİNE OLAN MESAFE: {sonuc} KM")
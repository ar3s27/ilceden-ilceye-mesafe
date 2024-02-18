#-*- coding: utf-8 -*-
import pandas as pd
k_il = "siirt"
k_ilce = "merkez"
v_il = "mardin"
v_ilce = "midyat"
df = pd.read_csv("ilcelerDonusturuldu_kucukharf.csv")


veri = df[(df['k_il'] == k_il) & (df['k_ilce'] == k_ilce) & 
          (df['v_il'] == v_il) & (df['v_ilce'] == v_ilce)]
mesafe = veri["Toplam Uzunluk(km)"].sum()

# Mesafeyi metin olarak biçimlendir
mesafe_metni = f"{k_il} İLİNİN {k_ilce} İLÇESİNDEN {v_il} İLİNİN {v_ilce} İLÇESİNE OLAN MESAFE: {int(mesafe)} KM"
print(mesafe_metni)
#-*- coding: utf-8 -*-
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import unquote

app = FastAPI(title="Mesafe")
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)
# Türkçe karakterleri büyük harfe çevirmek için bir işlev
def turkce_buyuk_harf_cevir(metin):
    harf_cevir = {
        'i': 'İ',
        'ı': 'I',
        'ğ': 'Ğ',
        'ü': 'Ü',
        'ş': 'Ş',
        'ö': 'Ö',
        'ç': 'Ç'
    }

    return ''.join(harf_cevir.get(harf, harf.upper()) for harf in metin)

df = pd.read_csv("ilcelerDonusturuldu_kucukharf.csv")
@app.get('/mesafe/{k_il}/{k_ilce}/{v_il}/{v_ilce}')
def mesafeGetir(k_il: str, k_ilce: str, v_il: str, v_ilce: str):
    try:
        # Girişleri büyük harfe çevirin
        #k_il = turkce_buyuk_harf_cevir(k_il)
        #k_ilce = turkce_buyuk_harf_cevir(k_ilce)
        #v_il = turkce_buyuk_harf_cevir(v_il)
        #v_ilce = turkce_buyuk_harf_cevir(v_ilce)
        veri = df[(df['k_il'] == k_il) & (df['k_ilce'] == k_ilce) & 
                  (df['v_il'] == v_il) & (df['v_ilce'] == v_ilce)]
        mesafe = veri["Toplam Uzunluk(km)"].sum()

        # Mesafeyi metin olarak biçimlendir
        mesafe_metni = f"{k_il} İLİNİN {k_ilce} İLÇESİNDEN {v_il} İLİNİN {v_ilce} İLÇESİNE OLAN MESAFE: {int(mesafe)} KM"
        return {"mesafe": mesafe_metni}
    except Exception as e:
        return {"error": str(e)}
# -*- coding: utf-8 -*-
import uvicorn
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Mesafe")
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

df = pd.read_csv("ilcelerDonusturuldu.csv")

@app.get('/mesafe/{k_il}/{k_ilce}/{v_il}/{v_ilce}')
def mesafeGetir(k_il: str, k_ilce: str, v_il: str, v_ilce: str):
    try:
        k_il = k_il.upper()
        k_ilce = k_ilce.upper()
        v_il = v_il.upper()
        v_ilce = v_ilce.upper()
        veri = df[(df['k_il'] == k_il) & (df['k_ilce'] == k_ilce) & 
                  (df['v_il'] == v_il) & (df['v_ilce'] == v_ilce)]
        mesafe = veri["Toplam Uzunluk(km)"].sum()

        # Mesafeyi metin olarak biçimlendir
        mesafe_metni = f"{k_il} İLİNİN {k_ilce} İLÇESİNDEN {v_il} İLİNİN {v_ilce} İLÇESİNE OLAN MESAFE: {int(mesafe)} KM"
        return {mesafe_metni}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=6060)

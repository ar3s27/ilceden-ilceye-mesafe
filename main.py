import pandas as pd
df = pd.read_csv("ilcelerMesafeDonusturulmus.csv")

def getir(k_il, k_ilce, v_il, v_ilce):
    veri = df[(df['k_il'] == k_il) & (df['k_ilce'] == k_ilce) & 
              (df['v_il'] == v_il) & (df['v_ilce'] == v_ilce)]
    if(veri == True):
        
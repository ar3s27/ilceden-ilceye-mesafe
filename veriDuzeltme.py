import pandas as pd
df = pd.read_csv('ilcelerMesafeDonusturulmus.csv')
df['Toplam Uzunluk(km)'] = df['Toplam Uzunluk(km)'].astype(int)
print("dönüşüm tamamlandı")
df.to_csv('donusmus_veri.csv', index=False)
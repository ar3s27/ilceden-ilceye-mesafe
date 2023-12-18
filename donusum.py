import pandas as pd

# CSV dosyasını oku
df = pd.read_csv("ilcelerDonusturuldu.csv")

# Tüm sütunlardaki verileri küçük harfe çevir
df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

# Sonucu yeni bir CSV dosyasına yaz
df.to_csv("ilcelerDonusturuldu_kucukharf.csv", index=False)
print("bitti")
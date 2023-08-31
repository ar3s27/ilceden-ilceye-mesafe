import pandas as pd

def get_total_length(data_file, k_il, k_ilce, v_il, v_ilce):
    # CSV dosyasını yükle
    data = pd.read_csv(data_file)

    # Belirtilen değerlere göre veriyi filtrele
    filtered_data = data[(data['k_il'] == k_il) & (data['k_ilce'] == k_ilce) &
                         (data['v_il'] == v_il) & (data['v_ilce'] == v_ilce)]

    # Toplam uzunluğu al
    total_length = filtered_data['Toplam Uzunluk(km)'].sum()

    return total_length

# CSV dosyasının adı
csv_file = 'ilcelerDonusturuldu.csv'

# Değerler
k_il = 'ADANA'
k_ilce = 'ALADAĞ'
v_il = 'ADANA'
v_ilce = 'CEYHAN'

# Fonksiyonu çağır ve sonucu yazdır
result = get_total_length(csv_file, k_il, k_ilce, v_il, v_ilce)
print(f"Karşılık gelen toplam uzunluk: {result} km")

stock_telur = {
    "Telur Ayam": 100,
    "Telur Bebek": 50,
}
for jenis_telur, jumlah in stock_telur.items():
    print(f"- {jenis_telur}: {jumlah}")

jenis_telur = input("Masukkan jenis telur: ")
jumlah_tambah = int(input("Masukkan jumlah telur yang ditambahkan: "))

stock_telur[jenis_telur] += jumlah_tambah

print("\nData Stock Terbaru:")
for jenis_telur, jumlah in stock_telur.items():
    print(f"- {jenis_telur}: {jumlah}")
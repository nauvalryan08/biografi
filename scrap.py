import requests
from bs4 import BeautifulSoup

# URL website yang telah kamu buat (jika dijalankan secara lokal, gunakan localhost, misalnya http://localhost:8000/index.html)
url = 'http://127.0.0.1:5500/'

# Mengambil konten halaman menggunakan requests
response = requests.get(url)

if response.status_code == 200:
    # Parsing HTML menggunakan BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Contoh 1: Mengambil heading utama (h1)
    h1 = soup.find('h1')
    print('Heading Utama:', h1.get_text() if h1 else 'Tidak ditemukan')

    # Contoh 2: Mengambil semua heading (h1 hingga h6)
    for level in range(1, 7):
        for heading in soup.find_all(f'h{level}'):
            print(f'H{level}:', heading.get_text())

    # Contoh 3: Mengambil semua paragraf dalam <article id="tentang">
    tentang = soup.find('article', id='tentang')
    if tentang:
        paragraphs = tentang.find_all('p')
        for idx, p in enumerate(paragraphs, 1):
            print(f'Paragraf {idx} dalam Tentang:', p.get_text())

    # Contoh 4: Mengambil semua link dalam navigasi
    nav = soup.find('nav')
    if nav:
        links = nav.find_all('a')
        for link in links:
            print('Link Navigasi:', link.get('href'), '-', link.get_text())

    # Contoh 5: Mengambil input pada formulir di footer
    footer = soup.find('footer')
    if footer:
        inputs = footer.find_all('input')
        for inp in inputs:
            tipe = inp.get('type')
            nama = inp.get('name')
            print('Input Form:', nama, 'Tipe:', tipe)
else:
    print("Gagal mengambil halaman. Status Code:", response.status_code)
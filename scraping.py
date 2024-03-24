from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)

oto_link = "https://www.oto.com/mobil-bekas"

driver.get(oto_link)
time.sleep(5)

driver.save_screenshot("home.png")
content = driver.page_source
driver.quit()

data = BeautifulSoup(content,'html.parser')

list_nama, list_gambar, list_harga, list_dp, list_lokasi = [],[],[],[],[]

i=1
for area in data.find_all('li',class_="card splide__slide shadow-light filter-listing-card used-car-card"):
    print(i)
    nama = area.find('a', class_="vh-name").get_text()
    gambar = area.find('img')['src']
    harga = area.find('div', class_="vh-price").get_text()
    dp = area.find('span', class_="f-11 block emi-txt")
    if dp != None:
        dp = dp.get_text()
    lokasi = area.find('li', class_="f-10 m-xs-r").get_text()
    print(nama)
    print(gambar)
    print(harga)
    print(dp) 
    print(lokasi)

    list_nama.append(nama)
    list_gambar.append(gambar)
    list_harga.append(harga)
    list_dp.append(dp)
    list_lokasi.append(lokasi)

    i+=1
    print("====================================")

df = pd.DataFrame({'Nama':list_nama,'Gambar':list_gambar,'Harga':list_harga,'DP':list_dp,'Lokasi':list_lokasi})
print(df)
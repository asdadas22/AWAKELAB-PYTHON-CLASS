import requests
import bs4
import json
import time
import datetime
import os
from grupal2 import settings

verduras_lider = requests.get("https://www.lider.cl/supermercado/category/Frutas-y-Verduras/_/N-1vsgxxq")
dom = bs4.BeautifulSoup(verduras_lider.text)
#for elemento in dom.select('span'):

elementos_precios = dom.find_all('span', attrs={'class' : 'price-sell'})
elementos_nombres = dom.find_all('span', attrs={'class' : 'product-name'})

lista_verduras = []
for index, nombre in enumerate(elementos_nombres):
    print(nombre.text, elementos_precios[index].text.strip("$").replace(".",""))
    lista_verduras.append((nombre.text, elementos_precios[index].text.strip("$").replace(".","")))

ruta = '/app_grupal2/static/app_grupal2/data/verduras.csv'

archivo = open(str(settings.BASE_DIR)+ ruta, 'w')
for verdura_nombre, verdura_precio in lista_verduras:
    archivo.write(verdura_nombre + "," + verdura_precio + "\n")
archivo.close()

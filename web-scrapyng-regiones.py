#se importa las librerias necesarias
from bs4 import BeautifulSoup
import requests
import pandas as pd 


#del sitio elegido traemos el contenido
website = 'http://www.iris.washington.edu/latin_am/evlist.phtml?region=mundo'
result = requests.get(website)
content = result.text

#parseamos el contenido en formato XML
soup = BeautifulSoup(content, 'lxml')

#identicamos la tabla, el body de la tabla y la fila
rows = soup.find('table', class_='tablesorter').find('tbody').find_all('tr')

#creamos una lista ppor columna de datos 
region =[]

#recorremos cada fila de la tabla y guardamos las regiones agrupados en una lista
for row in rows:
    region.append(row.find_all('td')[5].get_text())

#generamos un data frame para tabular los datos a mostrar e imprimo
dframe = pd.DataFrame(data={'Region': region})
dframe.to_excel('regiones.xlsx', index=False)
dframe.to_csv('regiones.csv',index=False,encoding='latin1')
print(dframe)

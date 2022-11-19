#se importa las librerias necesarias
from bs4 import BeautifulSoup
import requests
import pandas as pd 
import lxml

#del sitio elegido traemos el contenido
website = 'http://www.iris.washington.edu/latin_am/evlist.phtml?region=mundo'
result = requests.get(website)
content = result.text

#parseamos el contenido en formato XML
soup = BeautifulSoup(content, 'lxml')

#identicamos la tabla, el body de la tabla y la fila
rows = soup.find('table', class_='tablesorter').find('tbody').find_all('tr')

#prueba para imprimir por fila
#print(rows[0].find_all('td')[0].get_text())
#print(rows[0].find_all('td')[1].get_text())

#prueba para identificar en la fila el 1er dato
#for row in rows:
#    print(row.find_all('td')[0].get_text())
#    break

#creamos una lista ppor columna de datos 
fecha =[]
latitud =[]
longitud =[]
magnitud = []
profundidad =[]

#recorremos cada fila de la tabla y guardamos los datos agrupados por cada lista
for row in rows:
    fecha.append(row.find_all('td')[0].get_text())
    latitud.append(row.find_all('td')[1].get_text())
    longitud.append(row.find_all('td')[2].get_text())
    magnitud.append(row.find_all('td')[3].get_text())
    profundidad.append(row.find_all('td')[4].get_text()) 

#generamos un data frame para tabular los datos a mostrar e imprimo
df = pd.DataFrame(data={'Fecha': fecha, 'Latitud': latitud, 'Longitud': longitud, 'Magnitud': magnitud, 'Profundidad': profundidad})
#print(df)

#generamos dos archivos en excel y csv, (sin columna de indice) nos muetra columna Fecha, latitud, longitud y profundidad
df.to_excel('C:/Users/USUARIO/Documents/GitHub/VVVVV.5/salida/sismos.xlsx', index=False)

df.to_csv('C:/Users/USUARIO/Documents/GitHub/VVVVV.5/salida/sismos.csv',index=False,encoding='latin1')


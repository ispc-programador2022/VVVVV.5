from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'http://www.iris.washington.edu/latin_am/evlist.phtml?region=mundo'
pagina = requests.get(url)
soup = BeautifulSoup(pagina.content, 'html.parser')

# regiones donde ocurrieron ultimos sismos
#lugar = soup.find_all('td', class_ = 'region')
#print(lugar)

#lugares = list()

#for i in lugar:
 #lugares.append(i.text)
#print(lugares)


#resultados de la escala de magnitudes
#magnit = soup.find_all('td', class_ ='mag')

#magnitud = list()

#for i in magnit:
    #magnitud.append(i.text)

#print(magnitud)    




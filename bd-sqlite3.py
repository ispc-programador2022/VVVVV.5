#importamos librería para utilizar Sql lite
import sqlite3
#creamos BD, inicializamos la conexión y creamos la tabla Sismos
conn = sqlite3.connect('Proyecto.db')
c = conn.cursor()
c.execute("""CREATE TABLE SISMOS(
  Id INTEGER,
  FECHA DATE,  
  LATITUD REAL (2,2),
  LONG REAL (3,2),
  MAGNITUD REAL (2,2),
  PROFUNDIDAD TEXT (10),
  REGION TEXT (50)
)""")

regiones = [
(1, '2022-11-15', 59.77, 26.13, 5.2,'65 km', 'Islas Sur' ),
(2, '2022-11-15', 42.81, 124.58, 5.0, '65 km', 'Australia')
]

c.executemany('INSERT INTO SISMOS VALUES(?,?,?,?,?,?,?)', regiones)

c.execute('SELECT * FROM SISMOS')
print(c.fetchall())

conn.commit
conn.close


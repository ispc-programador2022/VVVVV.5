#importamos libreria para conectar la bd en MySql
import mysql.connector

try:
#realizamos el enlace con los datos de conexion
 conexion= mysql.connector.connect(host='localhost',
                                  user='root',
                                  passwd='',
                                  database='proyecto-VVVVV5')
except Exception as err:
    print('Error de conexión a la base de datos.')
else:
    print('Conectado a la base de datos.')
    cur01 = conexion.cursor()
    #conectados a la bd mostramos las tablas de la base
    cur01.execute('show tables')
    for f in cur01:
        print(f)

try:
    #insertamos en la tabla de usuarios los datos de los usuarios de la bd 
    insertar="insert into usuarios values(1005, 'Alejandro Toloza', 'AT1005')"
    cur01.execute(insertar)
    conexion.commit()
except Exception as err:
    print('Error insertando datos en la tabla Usuarios', err)
else:
    print('Datos insertados correctamente en la tabla Usuarios')
#cerramos la conexion a la base
conexion.close()
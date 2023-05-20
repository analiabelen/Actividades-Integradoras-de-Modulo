import mysql.connector
conexion =  mysql.connector.connect(user= "root", password= "root", host= "localhost", db= "bd_ejemplo_innova", port= "3306")
print(conexion)

## PRUEBA DE CONEXION##
#cur = conexion.cursor()
#cur.execute("SELECT dni, NOMBRE FROM persona ")
#for dni, nombre in cur.fetchall():
#    print  (dni, nombre)
#conexion.close()

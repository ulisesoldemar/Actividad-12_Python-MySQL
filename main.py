import mysql.connector
from PIL import Image
from io import BytesIO

bd = mysql.connector.connect(
    user='ulises', password='passinseguraxd',
    database='mascotas')

cursor = bd.cursor()

while True:
    print("1) Agregar dueño")
    print("2) Mostrar dueños")
    print("0) Salir")
    op = input("Ingresa una opción: ")

    if op == '1':
        nombre = input("Nombre: ")
        apellido1 = input("Primer apellido: ")
        apellido2 = input("Segundo apellido: ")
        email = input("Correo: ")
        contra = input("Contraseña: ")
        telefono = input("Telefono: ")
        domicilio = input("Domicilio: ")
        ruta = input("Ruta a la foto de perfil: ")

        with open(ruta, 'rb') as file:
            foto = file.read()

        consulta = "INSERT INTO dueno (nombre, apellido1, apellido2, email, pass, telefono, domicilio, foto) " \
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 

        cursor.execute(consulta, (nombre, apellido1, apellido2, email, contra, telefono, domicilio, foto))
        bd.commit()
        if cursor.rowcount:
            print("Se agregó dueño")
        else:
            print("Error")

    elif op == '2':
        consulta = "SELECT * FROM dueno"

        cursor.execute(consulta)
        for row in cursor.fetchall():
            print("ID: ", row[0])
            print("Nombre: ", row[1])
            print("Apellidos: ", row[2], ' ', row[3])
            print("Correo: ", row[4])
            print("Contraseña: ", row[5])
            print("Teléfono: ", row[6])
            print("Domicilio: ", row[7])
            print("Foto: ")
            file_like = BytesIO(row[8])
            img = Image.open(file_like)
            img.show()
    elif op == '0':
        break
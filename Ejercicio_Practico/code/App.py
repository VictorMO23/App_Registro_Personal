import os

list_personal = [] #Lista de almacenamiento
list_ID = [] #Lista de almacenamiento de los id del personal

# Requerimiento: Registro de personal
def fnt_limpiar():
    os.system('cls')
    print('Creador/Autor: Victor Manuel Marin Oquendo\n'
+ 'Asignatura: Metodologías Ágiles\n'
+ 'Fecha: 16 de mayo del 2024\n\n')

def fnt_registrar():
    print('============ Modulo de Registro ============\n\n')
    id = input('ID: ')
    name = input('Nombre: ')
    contact = input('Contacto: ')
    email = input('Correo: ')
    if id == '' or name == '' or contact == '' or email == '':
        input('\nDebe diligenciar todos los datos solictados <ENTER>')
    else:
        datos = id + " | " + name + " |  " + contact + "  |   " + email
        list_personal.append(datos)
        list_ID.append(id)
        input(f'\nLa persona {name} ha sido registrada con éxito <ENTER>')

def fnt_ver():

        print('            ============ Modulo Ver Registros============\n\n')
        if len(list_personal) == 0:
            input('\nNo existen registros <ENTER>')
        else:
            print('   ID        |   Nombres    |     Contacto     |           Correo\n')
            for i in range(len(list_personal)):
                print (list_personal[i])
            input('\nFin de los registros <ENTER>')
            

def fnt_Consultar(c):

    sw_encontrado = False
    pos = 0
    for i in range(len(list_personal)):
        if list_ID[i] == c:
            sw_encontrado = True
            pos = i
            break
    if sw_encontrado == True:
        fnt_limpiar()
        print('            ============ Modulo Consulta Registros============\n\n')
        print('   ID     |   Nombres   |     Contacto     |           Correo\n')
        print(list_personal[pos])
        input('\nPersona encontrada con éxito <ENTER>')
    else:
        input('\nEsta persona no se encuentra registrada <ENTER>')

sw = True
while sw == True:
    fnt_limpiar()
    opciones = input('============ Menú Principal ============\n\n1. Agregar\n2. Ver\n3. Consultar\n4. Salir\n\n--> ')
    if opciones == '4':
        fnt_limpiar()
        input('Fin del programa. <ENTER>')
        sw = False
    if opciones == '1':
        fnt_limpiar()
        fnt_registrar()
    if opciones == '2':
        fnt_limpiar()
        fnt_ver()
    if opciones == '3':
        fnt_limpiar()
        print('============ Modulo de Consulta ============\n\n')
        if len(list_personal) == 0:
            input('\nNo existen registros aun <ENTER>')
        else:
            c = input('Ingrese el ID de la persona a consultar: ')
            fnt_Consultar(c)
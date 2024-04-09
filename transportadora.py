

'''una transportadora requiere el desarrollo de una aplicacion 
que permita llevar un registro de los despachos de sus vehiculos 
teniendo en cuenta lo siguiente:

placa de vehiculos 
descripcion del vehiculo
nombre del propietario 
contacto 
ruta 
descripcion de la carga 

El numero del despacho se registra de forma automatica
es decir una variable que se incrementa. dicha informacion debe quedar registrada en un direccion 

el sistema debe realizar : 
registro de salidas y mostrar salidas '''


mi_diccionario = {}

import os

sw = True
N_dspacho = 0

def fnt_agregar(diccionario,nombre, descripcion_vehiculo,placa_vehiculos , contacto, ruta, descripcion_carga):
    if placa_vehiculos == '' or descripcion_vehiculo == '' or nombre == '' or contacto == '' or ruta == '' or descripcion_carga == '':
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        diccionario[placa_vehiculos] = {'nombre': nombre, 'descripcion del vehiculo':descripcion_vehiculo, 'ruta': ruta, 'descripcion de la carga':descripcion_carga}
        enter = input(f'\nLa persona {nombre} ha sido registrada con éxito <ENTER>')
        
def fnt_selector(op):
    
    global N_dspacho
    if op == '1':
        os.system('cls')
        print('<<<<<< REGISTRAR PERSONA >>>>>>\n')
        nombre = input('Nombre: -> ')
        contacto = int(input(' su contacto : ->'))
        placa_vehiculo = input(' placa : -> ')
        descripcion_vehiculo = input('descripcion del vehiculo : -> ')
        ruta = input('ruta : -> ')
        descripcion_carga = input('descripcion de la carga : -> ')
       
        
        N_dspacho += 1
        print('numero de despacho es :',N_dspacho)
      
        fnt_agregar(mi_diccionario, nombre, contacto,placa_vehiculo, descripcion_vehiculo, ruta, descripcion_carga)
    elif op == '2':
        fnt_mostrar()
   
        
    
    elif op == '3':
        sw == False
    
        
        
def fnt_mostrar():
    os.system('cls')
    print('<<< REPORTE >>> \n\nCantidad de registros: ',len(mi_diccionario),'\n')
    for clave, valor in mi_diccionario.items():
        print(f"{clave}: {valor}")
    enter = input('\n\nPresione ENTER para continuar...')

    
        
        
        
        
while sw == True:
    
    os.system('cls')
    
    opcion = input('>>>>>OPCIONES<<<< \n1.registrar \n2. mostrar  \n3. salir \n ->')
    
    if opcion == '1':
        fnt_selector (opcion)
    if opcion == '2':
        fnt_selector (opcion)
    if opcion == '3':
        sw = False

    
    
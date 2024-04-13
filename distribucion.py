



'''Una Empresa dedicada a la distribución de mercancía requiere el desarrollo de un aplicativo que permita registrar los pedidos solicitados por los diferentes clientes dentro de los cuales se tiene la siguiente información: Nombre del cliente, dirección, contacto, sexo, descripción de la casa o lugar para guiar al personal de entrega. Adicional a ello se debe colocar el nombre del producto, referencia y cantidades a solicitar. Todo esto debe quedar registrado en un diccionario y debe tener la posibilidad de ver todos los pedidos realizados.

'''
mi_diccionario = {}

import os

sw = True
def fnt_agregar(diccionario,nombre,direccion,contacto,sexo,descripcion_casa):
    if   nombre == ''or direccion == ''or contacto == ''or sexo == '' or descripcion_casa == '':
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        diccionario[nombre] ={'direccion: {direccion}', 'contacto: {contacto} ', 'sexo {sexo}','descripcion de la casa {descripcion_casa}'}
        enter = input(f'\nLa persona {nombre} ha sido registrada con éxito <ENTER>')
        
def fnt_selector(op):
    
    
    if op == '1':
        os.system('cls')
        print('<<<<<< REGISTRAR PERSONA >>>>>>\n')
        nombre = input('Nombre: -> ')
        contacto = int(input(' su contacto : ->'))
        sexo = input(' sexo : -> ')
        direccion = input(' direccion : -> ')
        descripcion_casa = input('descripcion de la casa : -> ')
        
        
        
       
        
      
        fnt_agregar(mi_diccionario, nombre, contacto,direccion,sexo,descripcion_casa)
    elif op == '2':
    
        fnt_productos ()

    elif op == '3':
        fnt_mostrar()
    
   
        
    
    elif op == '4':
        sw == False
    
        
        
def fnt_mostrar():
    os.system('cls')
    print('<<< REPORTE >>> \n\nCantidad de registros: ',len(mi_diccionario),'\n')
    for clave, valor in mi_diccionario.items():
        print(f"{clave}: {valor}")
    enter = input('\n\nPresione ENTER para continuar...')
    
    

    
def fnt_productos ():
    os.system('cls')
    producto = input('Ingrese el producto: ')
    referencia  = input('Ingrese la referencia: ')
    cantidad = input('Ingrese la cantidad: ')
    

    print (f'el producto es : {producto}')
    print (f'la referencia es : {referencia}')
    print(f' la  cantidad es : {cantidad }')


    
        
        
        
        
while sw == True:
    
    os.system('cls')
    
    opcion = input('>>>>>OPCIONES<<<< \n1.registrar \n2.pedidos \n3. mostrar  \n4. salir \n ->')
    
    if opcion == '1':
        fnt_selector (opcion)
    if opcion == '2':
        fnt_selector (opcion)
    if opcion == '3':
        fnt_selector (opcion)
        producto = input('Ingrese el producto: ')
        referencia  = input('Ingrese la referencia: ')
        cantidad = input('Ingrese la cantidad: ')
        
    if opcion == '4':
        print (f'el producto es : {producto}')
        print (f'la referencia es : {referencia}')
        print(f' la  cantidad es : {cantidad }')
        sw = False

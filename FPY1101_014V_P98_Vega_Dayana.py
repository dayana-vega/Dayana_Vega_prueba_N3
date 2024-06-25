import os 
import random
# import time 
# import calendar

lista_tipo=[]
lista_patentes=[]
lista_marca=[]
lista_precio=[]
lista_multa=[]
lista_fecha_de_registro=[]
lista_run=[]
lista_nombre=[]

multa = 0
os.system("cls")

#Solicitar información
def registrar_datos_del_vehiculo() :
    tipo_de_vehiculo= input ("Tipo de vechiculo (Auto, Camión, Camioneta, Moto): ").strip().lower()
    if tipo_de_vehiculo == ""  :
        print("inválido")
    else:
        lista_tipo.append(tipo_de_vehiculo)
        patente = input ("Patente: ").strip()
        if patente == ""  :
            print("inválido")
        else:
            lista_patentes.append(patente)
            marca = input ("Marca: ").strip()
            if marca == "" or len(marca) < 2 or len(marca) > 15  :
                print("inválido")
            else:
                try:
                    precio = int ( input ("Valor del vehiculo: "))
                    lista_marca.append(marca)
                except:
                    precio = 0
                if precio < 5000000 :
                    print("Vehiculo no cumple con los requisitos")
                else:
                    try: 
                        multa = int (input ("Cantidad de multas: "))
                        lista_precio.append(precio)
                    except:
                        multa = -1
                    if multa == "" : 
                         print("inválido")
                    else:
                        lista_multa.append(multa)
                        fecha_de_registro = input ("Fecha de registro del vehiculo (dia-mes-año): ")
                        if fecha_de_registro == "" :
                            print("inválido")
                        else: 
                            try:
                                run = int (input ("Ingrese Run sin digito verificador, puntos o guión: "))
                                
                            except:
                                run = 0
                            if run < 1999999 or run > 39999999 :
                                print("inválido")
                            else:
                                lista_run.append(run)
                                nombre = input ("Ingrese Nombre").strip()
                                if nombre == "" :
                                    print("inválido") 
                                else:
                                    lista_nombre.append(nombre)
                                
                        
def menu_de_opciones() :
    print("""
1. Grabar información
2. Buscar información
3. Imprimir certificados
4. Salir
""")

def consultar_patente() :
    consulta = input ("Ingrese patente: ")
    if consulta in lista_patentes :
        print(lista_tipo, lista_patentes, lista_marca, lista_precio, lista_multa, lista_fecha_de_registro, lista_run, lista_nombre)
    else:
        print("Inválido")
               
def menu_imprimir_certificados() :
    print("""
1. Emisión de contaminantes
2. Anotaciones vigentes
3. Multas
""") 
    
#opcion_imprimir_certificados = int (input ("Seleccione una opción: "))


def imprimir_emision():
    for i in range (1) :
        print(random.randrange(1500, 3500))

def imprimir_anotaciones():
    for i in range (1) :
        print(random.randrange(1500, 3500))

def imprimir_multas():
    for i in range (1) :
        print(random.randrange(1500, 3500))
        

  
# menu_de_opciones()

while True :
    menu_de_opciones()
    try: 
        opcion = int (input ("Seleccione una opción: "))
    except :
        opcion = 0
    
    if opcion == 1 :
        registrar_datos_del_vehiculo()
    elif opcion == 2 :
        consultar_patente()        
    elif opcion == 3 :
        menu_imprimir_certificados ()
        try: 
            opcion_imprimir_certificados = int (input ("Seleccione opción: "))
        except:
            opcion_imprimir_certificados = 0
        
        if opcion_imprimir_certificados == 1 :
            print(f"Certificado de contaminantes \nPatente {lista_patentes} \nNombre {lista_nombre} \nRUN {lista_run} \nValor $:  ") 
            imprimir_emision()
            
        elif opcion_imprimir_certificados == 2 :
            print(f"Cetificado de anotaciones vigentes  \nPatente {lista_patentes} \nNombre {lista_nombre} \nRUN {lista_run} \nValor $: ")
            imprimir_anotaciones()
            
        elif opcion_imprimir_certificados == 3 :
            print(f"Certificado de Multas  \nPatente {lista_patentes} \nNombre {lista_nombre} \nRUN {lista_run} \nValor $: ")
            imprimir_multas()
        else:
            print("inválido")  
    elif opcion == 4 :
        print("Ha salido del sistema")
        break
    else:
      print("inválido")  
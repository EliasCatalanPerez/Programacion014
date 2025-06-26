#IMPORTS
import funciones
import time
from os import system

#CODIGO

while True:
    
    print("»"*100)
    print(" VENTA DE ENTRADAS SHOW CONEJO SIMPÁTICO ".center(100," "))
    print("«"*100)

    funciones.construir_menu(funciones.menu)
    ans = funciones.respuesta_usuario()
    
    if ans == "1": #COMPRAR
        system("cls")
        print("»» MENU DE COMPRA «« ")
        nom = funciones.pedir_nombre(funciones.nombres)
        comprar = funciones.tipo_de_funcion()
        codex =  funciones.verificar_codigo()
        reserva = {
            "Nombre": nom,
            "Funcion elegida": comprar,
            "Codigo": codex
        }
        funciones.entrada.append(reserva)
        system("cls")
    elif ans == "2": #Eliminar
        system("cls")
        funciones.eliminar_reserva(funciones.entrada)
    elif ans == "3": #ver reservas
        system("cls")
        funciones.ver_reservas(funciones.entrada)
    elif ans == "4": #SALIR
        print("Gracias por usar nuestro sistema de ventas!.")
        break
    else:
        print("Opcion invalida, intente nuevamente!.")
        time.sleep(0.4)
        system("cls")
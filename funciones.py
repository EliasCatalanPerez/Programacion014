
from os import system

codigo = "Elconej0"
nombres = []

entrada = []

menu = [
    "COMPRAR",
    "ELIMINAR RESERVA",
    "VER RESERVA",
    "SALIR"
    ""
]

def construir_menu(opciones:list):
    "Crea un menu con una lista entregada."
    for idx, opt in enumerate(opciones):
        print(f"{idx + 1}. {opt}")
        
def respuesta_usuario():
    "solicita una respuesta al usuario y la retorna"
    ans = input("Seleccione una opción:\n>")
    return ans 

def tipo_de_funcion():
    "solicita el tipo de funcion que el usuario quiere asistir y verifica si cumple los parametros" 
    while True:
        try:
            tip_funcion = input("Seleccione una entrada: (G)-General o (V)-VIP:\n").upper()
            if tip_funcion == "G" or tip_funcion == "V":
                return tip_funcion
        except:
            print("Error, solo puedes introducir una alguna opción de la lista!")

def pedir_nombre(nombre:list):
    "Solicita nombre de usuario lo retorna y almacena en una lista temporal."
    while True:
        try:
            nom = input("Nombre del comprador:\n").upper()
            if nom in nombres:
                print("Este nombre ya se encuentra inscrito!.")
                continue
            else:
                assert nom.replace(" ", "").isalpha()
                temp = [nom]
                nombre.append(nom)
                return nom
        except:
            print("Caracter invalido, solo puede utilizar letras!.")
    


def ver_reservas(listado):
    'Muestra reservas desde formato json'
    if not listado:
        print("No hay reservas registradas.\n")
        return

    print("\n--- RESERVAS ---")
    for i, reserva in enumerate(listado, 1):
        print(f"\nReserva #{i}")
        for clave, valor in reserva.items():
            print(f"{clave}: {valor}")
    print()
    
def eliminar_reserva(entrada):
    "Elimina la entrada verificando el index por defecto de la reserva."
    if not entrada:
        print("No hay reservas para eliminar.")
        return

    for i, o in enumerate(entrada, 1):
        print(f"{i}. Nombre: {o['Nombre']} | Tipo de entrada: {o['Funcion elegida']}")
    try:
        n = int(input("Número de reserva a eliminar (0 para salir): "))
        if n == 0:
            print("Operación cancelada.")
            return
        del entrada[n - 1]  
        print("Reserva eliminada.")
    except (ValueError, IndexError):
        print("Número inválido.")

def verificar_codigo():
    "Verifica que el codigo inroducido sea igual al almacenado"
    while True:
        try:
            codex = input("Introdusca el codigo de seguridad!.\n")
            assert codex.replace(" ", "")
            if codex == "Elconej0":
                return codex
        except:
            print("Error!, codigo no valido!.")
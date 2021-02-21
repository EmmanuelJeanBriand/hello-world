def ask_option(): return int(input("Seleccione opción"))

def ask_int(s): return int(input(s))

header = r"""********
Calculadora
********"""
menu = r"""Menu
    1) Suma
    2) Resta
    3) Multiplicación
    4) División
    5) Salir"""


pairs = {1: ('La suma es: {res}', lambda a, b: a + b),
         2: ('La resta es: {res}', lambda a, b: a - b),
         3: ('La multiplicación es: {res}', lambda a, b: a * b),
         4: ('La división es: {res}', lambda a, b: a / b)}
bye = 5

def calcula(a, b, op_number):
    r"""Realiza ``a`` @ ``b`` con @ la operación número ``op_number`` e imprime 
    el resultado.
    
    ``op_number`` es clave del diccionario global ``pairs``
    
    EJEMPLOS::
    
        >>> calcula(3, 2, 1)
        La suma es: 5
        >>> calcula(3, 2, 2)
        La resta es: 1
        >>> calcula(3, 2, 3)
        La multiplicación es: 6
        >>> calcula(3, 2, 4)
        La división es: 1.5
        >>> calcula(3, 0, 4)
        No se permite la división entre 0
        >>> calcula(3, 2, 0)
        Traceback (most recent call last):
            ...
        ValueError: Opción no prevista
    """
    if op_number in pairs.keys():
        (s, operation) = pairs[op_number]
        try:
            res = operation(a, b)
        except ZeroDivisionError:
            print("No se permite la división entre 0")  
        else:
            print(s.format(res=res))
    else:
        raise ValueError('Opción no prevista')

    
def calculadora():
    r"""Pide datos y operación, y realiza la operación
    
    Interactivo.
    """
    print(header)
    print(menu)
    option = ask_option()
        
    while option in pairs.keys():
        a = ask_int("Ingrese número:") # errors not considered here
        b = ask_int("Ingrese otro número:") # same
        calcula(a, b, option)
        option = ask_option()
    else:
        if option == bye:
            print("Bye")
        else:
            print("opción no prevista. Bye.")

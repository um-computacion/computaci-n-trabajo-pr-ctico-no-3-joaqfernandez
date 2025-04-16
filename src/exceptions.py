class NumeroDebeSerPositivo(Exception):
    ...

def ingrese_numero():
    palabra = input("Introduce un numero positivo: ")
    numero = int(palabra)
    if numero < 0:
        raise NumeroDebeSerPositivo() #Emite una excepcion "generica"
    return numero
    

class NumeroDebeSerPositivo(Exception):
    ...

def ingrese_numero():
    palabra = input("Introduce un numero positivo: ")
    numero = int(palabra)
    if numero < 0:
        raise NumeroDebeSerPositivo() #Emite una excepcion "generica"
    return numero
    
def main():
    while True: 
        try:
            numero = ingrese_numero()
            numero2 = ingrese_numero()
            print(numero / numero2)

        except ValueError as e:
            print("ingrese numero")
        except ZeroDivisionError as e:
            print("No se puede dividir por cero")
        except NumeroDebeSerPositivo as e:
            print("El numero tiene que ser positivo")

if __name__ == "__main__":
    main()
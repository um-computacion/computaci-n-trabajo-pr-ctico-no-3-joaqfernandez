from exceptions import ingrese_numero
from exceptions import NumeroDebeSerPositivo

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
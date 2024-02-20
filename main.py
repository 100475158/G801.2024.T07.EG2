#THIS MAIN PROGRAM IS ONLY VALID FOR THE FIRST THREE WEEKS OF CLASS
#IN GUIDED EXERCISE 2.2, TESTING MUST BE PERFORMED USING UNITTESTS.

from UC3MTravel import HotelManager


def main():
    mng = HotelManager()
    res = mng.ReaddatafromJSOn("test.json")
    strRes = res.__str__()
    print(strRes)
    print("CreditCard: " + res.CREDITCARD)
    print(res.LOCALIZER)

if __name__ == "__main__":
    main()

def tarjeta(numero_tarjeta):
    lista_tarjeta=[]
    #Cambio el numero de la tarjeta(que es un string) a una lista de enteros
    #cambio el numero de tarjeta a string
    for numero in str(numero_tarjeta):
        lista_tarjeta.append(int(numero))
    #Empiezo algoritmo de Luhn
    #Invierto la lista para empezar por el ultimo numero pq el algoritmo lo requiere
    lista_invertida = lista_tarjeta[::-1]
    #Multiplicar por 2 cada segundo digito empezando por la derecha
    #si el doble de un numero es mayor que 9 se suman las 2 cifras
    for i in range(len(lista_invertida)):
         if i % 2 !=0:
            doble = lista_invertida[i] * 2
             # si el doble de un numero es mayor que 9 se suman las 2 cifras
            if doble > 9:
                cadena_doble = str(doble)
                suma_doble = 0
                for j in cadena_doble:
                    suma_doble += int(j)
                    lista_invertida[i] = suma_doble
            else:
                lista_invertida[i] = doble
    suma_digito = 0
    for digito in lista_invertida:
        suma_digito+= digito
    if suma_digito % 10==0:
        print("El número de la tarjeta de credito", numero_tarjeta, "es válido.")
    else:
        print("El número de la tarjeta de credito", numero_tarjeta, "no es válido.")


#Numero de tarjeta valido
valido= "4532015112830366"
if tarjeta(valido):
    print("El número de la tarjeta de credito",valido,"es válido.")


#Numero de tarjeta no valido
no_valido= "1234567812345678"
if tarjeta(no_valido):
    print("El número de la tarjeta de credito",no_valido,"no es válido.")

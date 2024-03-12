import json
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation

class HotelManager:
    def __init__(self):
        pass

    def validatecreditcard( self, numero_tarjeta ):
        lista_tarjeta = []
        # Cambio el numero de la tarjeta(que es un string) a una lista de enteros
        # cambio el numero de tarjeta a string
        for numero in str(numero_tarjeta):
            lista_tarjeta.append(int(numero))
        # Empiezo algoritmo de Luhn
        # Invierto la lista para empezar por el ultimo numero pq el algoritmo lo requiere
        lista_invertida = lista_tarjeta[::-1]
        # Multiplicar por 2 cada segundo digito empezando por la derecha
        # si el doble de un numero es mayor que 9 se suman las 2 cifras
        for i in range(len(lista_invertida)):
            if i % 2 != 0:
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
            suma_digito += digito
        if suma_digito % 10 == 0:
            return True
        else:
            return False

    def ReaddatafromJSOn( self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise HotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            c = DATA["CreditCard"]
            p = DATA["phoneNumber"]
            req = HotelReservation(IDCARD="12345678Z",creditcardNumb=c,nAMeAndSURNAME="John Doe",phonenumber=p,room_type="single",numdays=3)
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req
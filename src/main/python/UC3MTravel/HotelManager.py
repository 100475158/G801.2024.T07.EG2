import json
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation
from stdnum import es

class HotelManager:
    def __init__(self):
        pass

    def room_reservation(self,
                         IDCARD,
                         creditcardNumb,
                         nAMeAndSURNAME,
                         phonenumber,
                         arrival,
                         room_type,
                         numdays):

        def validatecreditcard(numero_tarjeta):
            #Comprobamos que sea un entero y que sea de 16 digitos
            if not isinstance(numero_tarjeta, int) or len(str(numero_tarjeta)) != 16:
                raise HotelManagementException("El numero de la tarjeta de credito es MUY largo")

            lista_tarjeta = []
            # Cambio el numero de la tarjeta(que es un string) a una lista de enteros
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
                raise HotelManagementException("La tarjeta de crédito no cumple el algoritmo de Luhn")

        def validate_id_card(id_card):
            # Comprobamos que sea un string y de 9 caracteres
            if not isinstance(id_card, str) or len(id_card)!= 9:
                raise HotelManagementException("El DNI no es válido")
            # Comprobamos que sea un numero de 8 numeros seguidos de una letra
            if not id_card[0:8].isdigit():
                raise HotelManagementException("El DNI no es válido")
            if not id_card[8].isalpha():
                raise HotelManagementException("El DNI no es válido")
            return True

        def validate_name(nombre):
            # Comprobamos que sea un string y de entre 10 y 50 caracteres
            if not isinstance(nombre, str):
                raise HotelManagementException("El Nombre no es válido")
            if not 10<=len(nombre)<=50:
                raise HotelManagementException("El Nombre no es válido")
            # Comprobamos que sean 2 o 3 cadenas de caracteres
            cadenas_nombre= nombre.split()
            if len(cadenas_nombre) !=2 or len(cadenas_nombre) !=3:
                raise HotelManagementException("El Nombre no es válido")
            # Comprobamos que esten separadas por un espacio en blanco
            if "" not in nombre:
                raise HotelManagementException("El Nombre no es válido")
            return True

        def validate_phone(movil):
            # Comprobamos que sea un entero de 9 digitos
            if not isinstance(movil, int) or len(str(movil)) != 9:
                raise HotelManagementException("El Número de teléfono no es válido")
            return True

        def validate_room(habitacion):
            # Comprobamos que sea un string
            if not isinstance(habitacion, str):
                raise HotelManagementException("La Habitación no es válida")
            # Convertimos la palabra a minusculas por si el usuario introduce mayusculas
            habitacion = habitacion.lower()
            # Comprobamos que sea single, double o suite
            if habitacion != "single" and habitacion != "double" and habitacion != "suite":
                raise HotelManagementException("L Habitación no es válida")
            return True

        def validate_arrival(llegada):
            #Comprobamos que sea un string de 10 caracteres
            if not isinstance(llegada, str) or len(llegada) != 10:
                raise HotelManagementException("La llegada no es válida")
            #Comprobamos el formato(“DD/MM/YYYY” )
            dia, mes, año = llegada.split("/")
            dia = int(dia)
            mes = int(mes)
            año = int(año)
            if not(1 <= dia <= 31 and 1 <= mes <= 12 and año != 2024):
                raise HotelManagementException("La llegada no es válida, esa fecha no existe")
            return True
        def validate_num_days(dias):
            # Comprobamos que sea un entero y que este entre 1 y 10
            if not isinstance(dias, int):
                raise HotelManagementException("El número de días no es válido")
            if not 1 <= dias <= 10:
                raise HotelManagementException("El número de días no es válido")
            return True


            #Llamamos a las funciones despues de definirlas
        try:
            validatecreditcard(creditcardNumb)
            validate_id_card(IDCARD)
            validate_name(nAMeAndSURNAME)
            validate_phone(phonenumber)
            validate_room(room_type)
            validate_arrival(arrival)
            validate_num_days(numdays)

        except HotelManagementException as e:
            # Captura y propaga la excepción
            raise e

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


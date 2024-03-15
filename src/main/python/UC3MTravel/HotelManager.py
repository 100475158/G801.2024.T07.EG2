import json
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation
from stdnum import es

class HotelManager:
    def __init__(self):
        pass

    def room_reservation(self, IDCARD, creditcardNumb, nAMeAndSURNAME, phonenumber, arrival, room_type, numdays):

        def validatecreditcard( self, numero_tarjeta ):
            #Comprobamos que sea un entero y que sea de 16 digitos
            if not isinstance(numero_tarjeta, int) or len(str(numero_tarjeta))!= 16:
                return False

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
                return False

        def validate_id_card(self,id_card):
            # Comprobamos que sea un string y de 9 caracteres
            if not isinstance(id_card, str) or len(id_card)!= 9:
                return False
            #Comprobamos que sea un numero de 8 numeros seguidos de una letra
            if not id_card[0:8].isdigit():
                return False
            if not id_card[8].isalpha():
                return False

        def validate_name(self, nombre):
            # Comprobamos que sea un string y de entre 10 y 50 caracteres
            if not isinstance(nombre, str):
                return False
            if not 10<=len(nombre)<=50:
                return False
            #Comprobamos que sean 2 o 3 cadenas de caracteres
            cadenas_nombre= nombre.split()
            if len(cadenas_nombre) !=2 or len(cadenas_nombre) !=3:
                return False
            #Comprobamos que esten separadas por un espacio en blanco
            if "" not in nombre:
                return False

        def validate_phone(self,movil):
            #Comprobamos que sea un entero de 9 digitos
            if not isinstance(movil, int) or len(str(movil)) != 9:
                return False

        def validate_room(self,habitacion):
            #Comprobamos que sea un string
            if not isinstance(habitacion, str):
                return False
            #Convertimos la palabra a minusculas por si el usuario introduce mayusculas
            habitacion= habitacion.lower()
            # Comprobamos que sea single, double o suite
            if (habitacion != "single") or (habitacion != "double") or (habitacion != "suite"):
                return False

        def validate_arrival(self,llegada):
            #Comprobamos que sea un string de 10 caracteres
            if not isinstance(llegada, str) or len(llegada)!= 10:
                return False
            #Comprobamos el formato(“DD/MM/YYYY” )
            dia,mes,año =llegada.split("/")
            dia=int(dia)
            mes=int(mes)
            año=int(año)
            if not(1<=dia<=31 and 1<=mes<=12 and año!= 2024):
                return False
        def validate_num_days(self,dias):
            # Comprobamos que sea un entero y que este entre 1 y 10
            if not isinstance(dias, int):
                return False
            if not 1<=dias<=10:
                return False


            #Llamamos a las funciones despues de definirlas
            self.validatecreditcard(creditcardNumb)
            self.validate_id_card(IDCARD)
            self.validate_name(nAMeAndSURNAME)
            self.validate_phone(phonenumber)
            self.validate_room(room_type)
            self.validate_arrival(arrival)
            self.validate_num_days(dias)

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


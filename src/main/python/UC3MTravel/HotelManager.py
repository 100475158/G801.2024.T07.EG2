import json
from pathlib import Path
import os
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation
from .HotelStay import HotelStay
import re
import calendar
from datetime import datetime, timezone


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
            if len(str(numero_tarjeta)) < 16:
                raise HotelManagementException("El numero de la tarjeta de credito es demasiado corto")

            if len(str(numero_tarjeta)) > 16:
                raise HotelManagementException("El numero de la tarjeta de credito es demasiado largo")
            lista_tarjeta = []
            # Cambio el numero de la tarjeta(que es un string) a una lista de enteros
            for numero in str(numero_tarjeta):
                lista_tarjeta.append(int(numero))


                if not numero_tarjeta.isdigit():
                    raise HotelManagementException("La tarjeta de credito no es un entero")

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
                raise HotelManagementException("La tarjeta de credito no cumple el algoritmo de Luhn")

        def validate_id_card(id_card):
            tabla_letras = 'TRWAGMYFPDXBNJZSQVHLCKE'

            # Comprobar longitud del DNI
            if len(id_card) < 9:
                raise HotelManagementException("El DNI es demasiado corto")
            if len(id_card) > 9:
                raise HotelManagementException("El DNI es demasiado largo")

            # Extraer número y letra del DNI
            try:
                numero = int(id_card[:-1])
                letra = id_card[-1].upper()
            except ValueError:
                raise HotelManagementException("El formato DNI no es correcto")

            # Comprobar si la letra se corresponde con el número
            if letra == tabla_letras[numero % 23]:
                return True
            else:
                raise HotelManagementException("El formato DNI no es correcto")

        def validate_name(nombre):
            cadenas_nombre = nombre.split()
            for palabra in cadenas_nombre:
                if not palabra.isalpha():
                    raise HotelManagementException("Formato del Nombre incorrecto")
            # Comprobamos que sea un string y de entre 10 y 50 caracteres
            if len(nombre) < 10:
                raise HotelManagementException("El Nombre es demasiado corto")
            if len(nombre) > 50:
                raise HotelManagementException("El Nombre es demasiado largo")
            # Comprobamos que sean 2 o 3 cadenas de caracteres
            if len(cadenas_nombre) < 2:
                raise HotelManagementException("El nombre tiene menos de 2 cadenas de caracteres")
            if len(cadenas_nombre) > 3:
                raise HotelManagementException("El nombre tiene mas de 3 cadenas de caracteres")
            # Comprobamos que esten separadas por un espacio en blanco
            if "" not in nombre:
                raise HotelManagementException("Formato del Nombre incorrecto")
            return True

        def validate_phone(movil):
            # Comprobamos que sea un entero de 9 digitos
            if not movil.isdigit():
                raise HotelManagementException("El formato del Número de teléfono no es válido")
            if len(str(movil)) < 9:
                raise HotelManagementException("El telefono tiene menos de 9 digitos")
            if len(str(movil)) > 9:
                raise HotelManagementException("El telefono tiene mas de 9 digitos")
            return True

        def validate_room(habitacion):
            # Convertimos la palabra a minusculas por si el usuario introduce mayusculas
            habitacion = habitacion.lower()
            # Comprobamos que sea single, double o suite
            if habitacion != "single" and habitacion != "double" and habitacion != "suite":
                raise HotelManagementException("La Habitación no es válida")
            return True

        def validate_arrival(llegada):
            #Comprobamos que sea un string de 10 caracteres
            if len(llegada) < 10:
                raise HotelManagementException("La llegada es menor de 10 caracteres")
            if len(llegada) > 10:
                raise HotelManagementException("La llegada es mayor de 10 caracteres")

            # Comprobamos el formato(“DD/MM/YYYY” )
            # Definimos el patrón regex para el formato de fecha
            patron = r'\d{2}/\d{2}/\d{4}'
            # Comprobamos si la fecha coincide con el patrón
            if not re.fullmatch(patron, llegada):
                raise HotelManagementException("El formato de la llegada no es correcto")

            # Comprobamos que la fecha tenga sentido y exista
            dia, mes, año = llegada.split("/")
            dia = int(dia)
            mes = int(mes)
            año = int(año)
            # Verificar si el año es bisiesto
            bisiesto = calendar.isleap(año)

            # Verificar si la fecha es válida
            if mes < 1 or mes > 12 or dia < 1 or dia > 31:
                raise HotelManagementException("La llegada no es valida, esa fecha no existe")
            elif mes in [4, 6, 9, 11] and dia > 30:
                raise HotelManagementException("La llegada no es valida, esa fecha no existe")
            elif mes == 2:
                if bisiesto and dia > 29:
                    raise HotelManagementException("La llegada no es valida, esa fecha no existe")
                elif not bisiesto and dia > 28:
                    raise HotelManagementException("La llegada no es valida, esa fecha no existe")
            return True
        def validate_num_days(dias):
            # Comprobamos que sea un entero y que este entre 1 y 10
            if not dias.isdigit():
                raise HotelManagementException("El formato del numero de dias no es correcto")
            if int(dias) > 10:
                raise HotelManagementException("El numero de dias es mayor de 10")
            if int(dias) < 1:
                raise HotelManagementException("El numero de dias es menor de 1")
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

            # Si todos los datos son correctos, generas la reserva y obtienes el localizador
            # Obtener la representación en cadena de la reserva mediante __str__
            reserva = HotelReservation(IDCARD, creditcardNumb, nAMeAndSURNAME, phonenumber, arrival, room_type, numdays)
            localizer = reserva.LOCALIZER  # Aquí invocas el método LOCALIZER

            # Crear un diccionario con los datos de la reserva y el localizador
            reserva_dict = reserva.__dict__
            reserva_dict['LOCALIZER'] = localizer

            # Directorio donde se guardarán los archivos JSON
            json_files_path = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/json_files/"
            # Ruta completa del archivo de reserva
            file_store = json_files_path + "store_reservation.json"

            # Verificar si el directorio existe, y si no, crearlo
            if not os.path.exists(json_files_path):
                os.makedirs(json_files_path)

            # Escribir los datos de la reserva en un archivo
            try:
                # Intentar cargar los datos existentes del archivo si existe
                with open(file_store, "r", encoding="utf-8") as file:
                    data_list = json.load(file)
            except FileNotFoundError:
                # Si el archivo no existe, crear una lista vacía
                data_list = []
            except json.JSONDecodeError as ex:
                # Manejar errores de decodificación JSON
                raise HotelManagementException("Error de decodificación JSON - Formato JSON incorrecto") from ex

            # Comprobar si la reserva ya existe en la lista
            for item in data_list:
                if reserva.LOCALIZER == item.get("LOCALIZER"):
                    raise HotelManagementException("Reserva ya realizada")

            # Añadir los datos de la reserva a la lista
            data_list.append(reserva.__dict__)

            # Escribir la lista actualizada en el archivo
            try:
                with open(file_store, "w", encoding="utf-8") as file:
                    json.dump(data_list, file, indent=2)
            except FileNotFoundError:
                raise HotelManagementException("Archivo no encontrado")
            except Exception as e:
                raise HotelManagementException("Error al escribir en el archivo JSON") from e

            return localizer
        except HotelManagementException as e:
            # Captura y propaga la excepción
            raise e

    def guest_arrival(self, input_file):
        try:
            # Cargar los datos de entrada
            with open(input_file, 'r') as f:
                data = json.load(f)

            # Obtener los valores necesarios del archivo de entrada
            localizer = data.get("Localizer")
            idcard = data.get("IdCard")

            if localizer is None or idcard is None:
                raise HotelManagementException("El archivo JSON no tiene la estructura esperada")

            # Verificar si el localizador está en el archivo de reservas y obtener datos adicionales
            tc0 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/json_files/store_reservation.json"
            with open(tc0, 'r') as f:
                reservations = json.load(f)

            reservation_data = None
            for reservation in reservations:
                if reservation.get("LOCALIZER") == localizer:
                    reservation_data = reservation
                    break

            if reservation_data is None:
                raise HotelManagementException("El localizador no se corresponde con los datos almacenados")

            # Extraer datos relevantes de la reserva
            numdays = reservation_data.get("_HotelReservation__num_days")
            roomtype = reservation_data.get("_HotelReservation__roomtype")

            # Verificar si el localizador ya existe en el archivo de salida
            directorio = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/json_files/"
            output_file = os.path.join(directorio, "hotel_stays.json")

            if os.path.exists(output_file):
                with open(output_file, 'r') as f:
                    for line in f:
                        existing_stay = json.loads(line)
                        if existing_stay.get("localizer") == localizer:
                            raise HotelManagementException(
                                "La reserva con este localizador ya existe en el archivo de salida")
            # Crear instancia de HotelStay
            stay = HotelStay(idcard, localizer, numdays, roomtype)

            # Guardar información de la estancia en el archivo "hotel_stays.json"
            directorio = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/json_files/"
            output_file = os.path.join(directorio, "hotel_stays.json")
            with open(output_file, 'a') as f:
                stay_dict = {
                    "alg": stay._HotelStay__alg,
                    "typ": stay._HotelStay__type,
                    "idcard": stay.idCard,
                    "localizer": stay.localizer,
                    "arrival": str(stay.arrival),
                    "departure": str(stay.departure),
                    "room_key": stay.room_key
                }
                json.dump(stay_dict, f)
                f.write('\n')

            # Retornar la clave de la habitación
            return stay.room_key

        except FileNotFoundError:
            raise HotelManagementException("No se encuentra el archivo de datos")
        except json.JSONDecodeError:
            raise HotelManagementException("El archivo no tiene formato JSON")
        except ValueError:
            raise HotelManagementException("Los datos del JSON no tienen valores válidos")
        except Exception as e:
            raise HotelManagementException(f"Error de procesamiento interno: {str(e)}")

    def guest_checkout(self, room_key):
        try:
            # Verificar que room_key es una cadena hexadecimal válida de 64 caracteres
            if not isinstance(room_key, str) or len(room_key) != 64 or not all(
                    caracter in "0123456789abcdefABCDEF" for caracter in room_key):  # Nodo 1
                raise HotelManagementException(
                    "La cadena de entrada no contiene un código de habitación válido")  # Nodo 2

            # Verifico si esta registrado en el archivo de estancias
            tcc0 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/json_files/hotel_stays.json"
            with open(tcc0, "r") as estancias_file:  # Nodo 3
                reserva = json.load(estancias_file)  # Nodo 4
                if reserva.get("room_key") == room_key:  # Nodo 5
                    # Obtener la fecha y hora actual en formato UTC
                    fecha_actual = datetime.utcnow().replace(tzinfo=timezone.utc)

                    # Formatear la fecha y hora actual en el formato deseado
                    fecha_actual_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")

                    # Verificar si departure(salida programada calculada en f2) coincide con fecha_actual(fecha de salida)
                    fecha_salida = reserva.get("departure")
                    if fecha_salida == fecha_actual_formateada:  # Nodo 6
                        # Registra la entrega en un archivo con la marca de tiempo (hora UTC) en que el cliente ha dejado la habitación
                        # y el código de la habitación
                        # se registra la salida en un fichero
                        directorio = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/json_files/"
                        checkouts_file_path = directorio + "check-outs.json"
                        with open(checkouts_file_path, "a") as checkouts_file:  # Nodo 7
                            data = {"room_key": room_key, "departure": fecha_actual.strftime("%Y-%m-%d %H:%M:%S")}
                            json.dump(data, checkouts_file)
                        return True  # Nodo 8
                    else:
                        raise HotelManagementException("La fecha de salida no es válida")  # Nodo 14
                else:
                    raise HotelManagementException("El código de habitación no estaba registrado")  # Nodo 13

        except FileNotFoundError:
            raise HotelManagementException("No se encuentra el archivo de datos")  # Nodo 12
        except HotelManagementException as e:
            raise HotelManagementException(f"Error de procesamiento interno: {str(e)}")

                # Nodo F

def ReaddatafromJSOn(self, fi):

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
            req = HotelReservation(IDCARD="12345678Z", creditcardNumb=c, nAMeAndSURNAME="John Doe", phonenumber=p, room_type="single", numdays=3)
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req


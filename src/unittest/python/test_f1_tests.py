"""
Este módulo contiene pruebas para la F1.
"""
import os
import sys
import unittest
import json
from pathlib import Path
from unittest import TestCase
from UC3MTravel.HotelManagementException import HotelManagementException
from UC3MTravel.HotelManager import HotelManager

# Obtenemos el directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtenemos la ruta del directorio src
src_dir = os.path.join(current_dir, '..', '..', '..', 'main', 'python')
# Añadimos la ruta del directorio src al sys.path
sys.path.append(src_dir)


class test_room_reservation(TestCase):
    """
    Clase principal para pruebas relacionadas con la reserva de huéspedes.
    """
    file_store = None

    @classmethod
    def setUpClass(cls):
        json_files_path = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/json_files/"
        cls.file_store = json_files_path + "store_reservation.json"
        if os.path.isfile(cls.file_store):
            os.remove(cls.file_store)

    def test_valid_tc1(self):
        """
        CASI todas las clases válidas
        """
        my_reservation = HotelManager()
        valor = my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                                idcard="12345678Z",
                                                nameandsurname="JOSE LOPEZ",
                                                phonenumber="911234567",
                                                room_type="SINGLE",
                                                arrival="14/10/2024",
                                                numdays="2")
        print("OK")
        self.assertEqual(valor, "f9ab0de669b4fccf3ce0efd99cbded11")

        with open(self.file_store, "r", encoding="utf-8") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["LOCALIZER"] == "f9ab0de669b4fccf3ce0efd99cbded11":
                found = True
        self.assertTrue(found)

    def test_luhn_cd_tc2(self):
        """
        Tarjeta de credito invalida,no cumple algoritmo de Luhn
        """
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554442",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "La tarjeta de credito no cumple el algoritmo de Luhn")

    def test_tipo_dato_cd_tc3(self):
        """
        CASI todas las clases válidas
        """
        # Tarjeta de credito invalida, no es un entero
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="555555555555444a",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "La tarjeta de credito no es un entero")

    def test_mas_long_cd_tc4(self):
        """
        CASI todas las clases válidas
        """
        # Tarjeta de credito invalida, numero mas largo
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="95555555555554440",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "El numero de la tarjeta de credito es demasiado largo")

    def test_menos_long_cd_tc5(self):
        """
        CASI todas las clases válidas
        """
        # Tarjeta de credito invalida, numero mas corto
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="555555555554440",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "El numero de la tarjeta de credito es demasiado corto")

    def test_tipo_dato_id_tc6(self):
        """
        CASI todas las clases válidas
        """
        # Dni invalido, no cumple el formato
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="123456789",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "El formato DNI no es correcto")

    def test_mas_long_id_tc7(self):
        """
        CASI todas las clases válidas
        """
        # Dni invalido, longitud 10
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="123456789Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "El DNI es demasiado largo")

    def test_menos_long_id_tc8(self):
        """
        CASI todas las clases válidas
        """
        # Dni invalido, longitud 8
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="1234567Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "El DNI es demasiado corto")

    def test_tipo_dato_nombre_tc9(self):
        """
        CASI todas las clases válidas
        """
        # Nombre invalido, no es un string
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="1234",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "Formato del Nombre incorrecto")

    def test_valid_tc10(self):
        """
        CASI todas las clases válidas
        """
        # Nombre válido de 3 cadenas
        my_reservation = HotelManager()
        valor = my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                                idcard="12345678Z",
                                                nameandsurname="ANTONIO LOPEZ LOPEZ",
                                                phonenumber="911234567",
                                                room_type="SINGLE",
                                                arrival="14/10/2024",
                                                numdays="2")
        self.assertEqual(valor, "ddd1ae3b83051f1ff4dbdbae022ce195")

        with open(self.file_store, "r", encoding="utf-8") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["LOCALIZER"] == "ddd1ae3b83051f1ff4dbdbae022ce195":
                found = True
        self.assertTrue(found)

    def test_1_cadena_nombre_tc11(self):
        """
        CASI todas las clases válidas
        """
        # Nombre invalido, tiene una o menos cadenas de caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="JOSELUISLOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "El nombre tiene menos de 2 cadenas de caracteres")

    def test_4_cadenas_nombre_tc12(self):
        """
        CASI todas las clases válidas
        """
        # Nombre invalido, tiene cuatro cadenas de caracteres o más
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ LOPEZ LOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "El nombre tiene mas de 3 cadenas de caracteres")

    def test_menos_long_nombre_tc13(self):
        """
        CASI todas las clases válidas
        """
        # Nombre invalido, menos de 10 caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPE",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "El Nombre es demasiado corto")

    def test_mas_long_nombre_tc14(self):
        """
        CASI todas las clases válidas
        """
        # Nombre invalido, mas de 50 caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="JJJJJJJJJJJJJJJJJJJJJJJJ JJJJJJJJJJJJJJJJJJJJJJJJJJ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "El Nombre es demasiado largo")

    def test_tipo_dato_phone_tc15(self):
        """
        CASI todas las clases válidas
        """
        # Telefono invalido, no es un entero
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="91123456e",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "El formato del Número de teléfono no es válido")

    def test_mas_long_phone_tc16(self):
        """
        CASI todas las clases válidas
        """
        # Telefono invalido, longitud 10
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="9112345678",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "El telefono tiene mas de 9 digitos")

    def test_menos_long_phone_tc17(self):
        """
        CASI todas las clases válidas
        """
        # Telefono invalido, longitud 8
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="91123456",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "El telefono tiene menos de 9 digitos")

    def test_habitacion_incorrecta_tc18(self):
        """
        CASI todas las clases válidas
        """
        # Habitación incorrecta
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="911234567",
                                            room_type="5U1T3",
                                            arrival="14/10/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "La Habitación no es válida")

    def test_valid_tc19(self):
        """
        CASI todas las clases válidas
        """
        # Habitación correcta DOUBLE
        my_reservation = HotelManager()
        valor = my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                                idcard="12345678Z",
                                                nameandsurname="ANTONIO LOPEZ",
                                                phonenumber="911234567",
                                                room_type="DOUBLE",
                                                arrival="14/10/2024",
                                                numdays="2")
        self.assertEqual(valor, "46324af73dfb272314924e6a876dc2ac")

        with open(self.file_store, "r", encoding="utf-8") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["LOCALIZER"] == "46324af73dfb272314924e6a876dc2ac":
                found = True
        self.assertTrue(found)

    def test_valid_tc20(self):
        """
        CASI todas las clases válidas
        """
        # Habitación correcta SUITE
        my_reservation = HotelManager()
        valor = my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                                idcard="12345678Z",
                                                nameandsurname="ANTONIO LOPEZ",
                                                phonenumber="911234567",
                                                room_type="SUITE",
                                                arrival="14/10/2024",
                                                numdays="2")
        self.assertEqual(valor, "5d6cfb6170189551fa11ffd37b616140")

        with open(self.file_store, "r", encoding="utf-8") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["LOCALIZER"] == "5d6cfb6170189551fa11ffd37b616140":
                found = True
        self.assertTrue(found)

    def test_formato_llegada_tc21(self):
        """
        CASI todas las clases válidas
        """
        # Llegada invalida, fecha no existe
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="24/55/2678",
                                            numdays="2")
        self.assertEqual(str(cm.exception), "La llegada no es valida, esa fecha no existe")

    def test_formato_llegada_tc22(self):
        """
        CASI todas las clases válidas
        """
        # Llegada invalida, formato incorrecto
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="1401602024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "El formato de la llegada no es correcto")

    def test_mas_long_llegada_tc23(self):
        """
        CASI todas las clases válidas
        """
        # Llegada invalida, 11 caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/20245",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "La llegada es mayor de 10 caracteres")

    def test_menos_long_llegada_tc24(self):
        """
        CASI todas las clases válidas
        """
        # Llegada invalida, 9 caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/6/2024",
                                            numdays="2")
        self.assertEqual(cm.exception.message, "La llegada es menor de 10 caracteres")

    def test_tipo_dato_num_dias_tc25(self):
        """
        CASI todas las clases válidas
        """
        # Numero de dias invalido formato
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="X")
        self.assertEqual(cm.exception.message, "El formato del numero de dias no es correcto")

    def test_mas_num_dias_tc26(self):
        """
        CASI todas las clases válidas
        """
        # Numero de dias invalido, 11 dias
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="11")
        self.assertEqual(cm.exception.message, "El numero de dias es mayor de 10")

    def test_menos_num_dias_tc27(self):
        """
        CASI todas las clases válidas
        """
        # Número de dias inválido, 11 dias
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            my_reservation.room_reservation(creditcardnumb="5555555555554444",
                                            idcard="12345678Z",
                                            nameandsurname="JOSE LOPEZ",
                                            phonenumber="911234567",
                                            room_type="SINGLE",
                                            arrival="14/10/2024",
                                            numdays="0")
        self.assertEqual(cm.exception.message, "El numero de dias es menor de 1")


if __name__ == '__main__':
    unittest.main()

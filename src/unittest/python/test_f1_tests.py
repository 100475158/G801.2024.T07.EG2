import unittest
from unittest import TestCase
from src.main.python.UC3MTravel.HotelManagementException import HotelManagementException
from src.main.python.UC3MTravel.HotelManager import HotelManager
from src.main.python.UC3MTravel.HotelReservation import HotelReservation

class test_room_reservation(TestCase):
    def test_valid_tc1(self):
        # CASI todas las clases válidas
        my_reservation = HotelManager()
        valor = my_reservation.room_reservation(creditcardNumb = "5555555555554444",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/10/2024",
                                                numdays = "2")
        print("OK")
        self.assertEqual(valor,"f9ab0de669b4fccf3ce0efd99cbded11")
    def test_Luhn_CD_tc2(self):
        # Tarjeta de credito invalida,no cumple algoritmo de Luhn
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb = "5555555555554442",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/10/2024",
                                                numdays = "2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"La tarjeta de credito no cumple el algoritmo de Luhn")
    def test_tipo_dato_CD_tc3(self):
        # Tarjeta de credito invalida, no es un entero
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb = "555555555555444a",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/10/2024",
                                                numdays = "2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"La tarjeta de credito no es un entero")

    def test_mas_long_CD_tc4(self):
        # Tarjeta de credito invalida, numero mas largo
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb = "95555555555554440",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/10/2024",
                                                numdays = "2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El numero de la tarjeta de credito es demasiado largo")

    def test_menos_long_CD_tc5(self):
        # Tarjeta de credito invalida, numero mas corto
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb = "555555555554440",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/10/2024",
                                                numdays = "2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El numero de la tarjeta de credito es demasiado corto")

    def test_tipo_dato_ID_tc6(self):
        # Dni invalido, no cumple el formato
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/10/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El formato DNI no es correcto")

    def test_mas_long_ID_tc7(self):
        # Dni invalido, longitud 10
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="123456789Z",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/10/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El DNI es demasiado largo")

    def test_menos_long_ID_tc8(self):
        # Dni invalido, longitud 8
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="1234567Z",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/10/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El DNI es demasiado corto")

    def test_tipo_dato_nombre_tc9(self):
        # Nombre invalido, no es un string
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="1234",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/10/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "Formato del Nombre incorrecto")
    def test_valid_tc10(self):
        # Nombre válido de 3 cadenas
        my_reservation = HotelManager()
        valor = my_reservation.room_reservation(creditcardNumb = "5555555555554444",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "ANTONIO LOPEZ LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/10/2024",
                                                numdays = "2")
        print("OK")
        self.assertEqual(valor,"ddd1ae3b83051f1ff4dbdbae022ce195")
    def test_1_cadena_nombre_tc11(self):
        # Nombre invalido, tiene una o menos cadenas de caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="JOSELUISLOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/10/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El nombre tiene menos de 2 cadenas de caracteres")


    def test_4_cadenas_nombre_tc12(self):
        # Nombre invalido, tiene cuatro cadenas de caracteres o más
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="JOSE LOPEZ LOPEZ LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/10/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El nombre tiene mas de 3 cadenas de caracteres")

    def test_menos_long_nombre_tc13(self):
        # Nombre invalido, menos de 10 caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="JOSE LOPE",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/10/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El Nombre es demasiado corto")


    def test_mas_long_nombre_tc14(self):
        # Nombre invalido, mas de 50 caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ JJJJJJJJJJJJJJJJJ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/10/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El Nombre demasiado largo")


    def test_tipo_dato_phone_tc15(self):
        # Telefono invalido, no es un entero
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="91123456e",
                                                    room_type="SINGLE",
                                                    arrival="14/10/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El formato del Número de teléfono no es válido")
    def test_mas_long_phone_tc16(self):
        # Telefono invalido, longitud 10
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="9112345678",
                                                    room_type="SINGLE",
                                                    arrival="14/10/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El telefono tiene mas de 9 digitos")

    def test_menos_long_phone_tc17(self):
        # Telefono invalido, longitud 8
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="91123456",
                                                    room_type="SINGLE",
                                                    arrival="14/10/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El telefono tiene menos de 9 digitos")

    def test_habitacion_incorrecta_tc18(self):
        # Habitación incorrecta
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="5U1T3",
                                                    arrival="14/10/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "La Habitación no es válida")

    def test_valid_tc19(self):
        # Habitación correcta DOUBLE
        my_reservation = HotelManager()
        valor = my_reservation.room_reservation(creditcardNumb = "5555555555554444",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "ANTONIO LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "DOUBLE",
                                                arrival = "14/10/2024",
                                                numdays = "2")
        print("OK")
        self.assertEqual(valor,"46324af73dfb272314924e6a876dc2ac")

    def test_valid_tc20(self):
        # Habitación correcta SUITE
        my_reservation = HotelManager()
        valor = my_reservation.room_reservation(creditcardNumb = "5555555555554444",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "ANTONIO LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SUITE",
                                                arrival = "14/10/2024",
                                                numdays = "2")
        print("OK")
        self.assertEqual(valor,"5d6cfb6170189551fa11ffd37b616140")

    def test_formato_llegada_tc21(self):
        # Llegada invalida, fecha no existe
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="24/55/2678",
                                                    numdays="2")
        self.assertEqual(str(cm.exception), "La llegada no es valida, esa fecha no existe")

    def test_formato_llegada_tc22(self):
        # Llegada invalida, formato incorrecto
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="1401602024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El formato de la llegada no es correcto")

    def test_mas_long_llegada_tc23(self):
        # Llegada invalida, 11 caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/10/20245",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "La llegada es mayor de 10 caracteres")

    def test_menos_long_llegada_tc24(self):
        # Llegada invalida, 9 caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/6/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "La llegada es menor de 10 caracteres")

    def test_tipo_dato_num_dias_tc25(self):
        # Numero de dias invalido formato
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/10/2024",
                                                    numdays="X")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El formato del numero de dias no es correcto")

    def test_mas_num_dias_tc26(self):
        #Numero de dias invalido, 11 dias
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/10/2024",
                                                    numdays="11")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El numero de dias es mayor de 10")

    def test_menos_num_dias_tc27(self):
        #Numero de dias invalido, 11 dias
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="5555555555554444",
                                                    IDCARD="12345678Z",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/10/2024",
                                                    numdays="0")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El numero de dias es menor de 1")

if __name__ == '__main__':
    unittest.main()

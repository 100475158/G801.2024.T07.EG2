import unittest
from unittest import TestCase
from src.main.python.UC3MTravel.HotelManagementException import HotelManagementException
from src.main.python.UC3MTravel.HotelManager import HotelManager

class test_room_reservation(TestCase):
    def test_valid_tc1(self):
        #Tarjeta de credito valida
        my_reservation = HotelManager()
        valor = my_reservation.room_reservation(creditcardNumb = "5555555555554444",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/16/2024",
                                                numdays = "2")
        print("OK")

    def test_Luhn_CD_tc2(self):
        #Tarjeta de credito invalida,no cumple algoritmo de Luhn
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb = "5555555555554442",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/16/2024",
                                                numdays = "2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"La tarjeta de credito no cumple el algoritmo de Luhn")
    def test_tipo_dato_CD_tc3(self):
        #Tarjeta de credito invalida,no es un entero
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb = "555555555555444a",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/16/2024",
                                                numdays = "2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"La tarjeta de credito no es un entero")

    def test_mas_long_CD_tc4(self):
        #Tarjeta de credito invalida,numero mas largo
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb = "95555555555554440",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/16/2024",
                                                numdays = "2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El numero de la tarjeta de credito es demasiado largo")

    def test_menos_long_CD_tc5(self):
        #Tarjeta de credito invalida,numero mas corto
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb = "555555555554440",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/16/2024",
                                                numdays = "2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El numero de la tarjeta de credito es demasiado corto")

    def test_tipo_dato_ID_tc6(self):
        # Dni invalido,no es un string
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/16/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El dni no es un string")

    def test_mas_long_ID_tc7(self):
        # Dni invalido,longitud 10
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789Z",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/16/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El dni tiene mas de 9 caracteres")

    def test_menos_long_ID_tc8(self):
        # Dni invalido,longitud 8
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="12345678",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/16/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El dni tiene menos de 9 caracteres")

    def test_formato_ID_tc9(self):
        # Dni invalido,no tiene una letra al final
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/16/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El dni no tiene un formato valido")


    def test_tipo_dato_nombre_tc10(self):
        # Nombre invalido,no es un string
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="1234",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/16/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El nombre no es un string")

    def test_1_cadena_nombre_tc11(self):
        # Nombre invalido,tiene una cadena de caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/16/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El nombre tiene menos de 2 cadenas de caracteres")

    def test_4_cadenas_nombre_tc12(self):
        # Nombre invalido,tiene cuatro cadenas de caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPEZ LOPEZ LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/16/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El nombre tiene mas de 3 cadenas de caracteres")

    def test_no_espacio_nombre_tc13(self):
        # Nombre invalido,no hay separacion de cadenas
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSELOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/16/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El nombre no esta separado por un espacio en blanco")


    def test_menos_long_nombre_tc14(self):
        # Nombre invalido,menos de 10 caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPE",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/16/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El nombre tiene menos de 10 caracteres")


    def test_mas_long_nombre_tc15(self):
        # Nombre invalido,mas de 50 caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/16/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El nombre tiene mas de 50 caracteres")

    def test_tipo_dato_phone_tc16(self):
        # Telefono invalido,no es un entero
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="91123456e",
                                                    room_type="SINGLE",
                                                    arrival="14/16/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El telefono no es un entero")

    def test_mas_long_phone_tc17(self):
        # Telefono invalido,longitud 10
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="9112345678",
                                                    room_type="SINGLE",
                                                    arrival="14/16/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El telefono tiene mas de 9 digitos")

    def test_menos_long_phone_tc18(self):
        # Telefono invalido,longitud 8
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="91123456",
                                                    room_type="SINGLE",
                                                    arrival="14/16/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El telefono tiene menos de 9 digitos")

    def test_habitacion_incorrecta_tc19(self):
        # Telefono invalido,longitud 8
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="5U1T3",
                                                    arrival="14/16/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El telefono tiene menos de 9 digitos")

    def test_tipo_dato_llegada_tc20(self):
        #Llegada invalida,no es un string
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14162024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "La llegada no es un string")

    def test_formato_llegada_tc21(self):
        #Llegada invalida,formato incorrecto
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="35/54/2678",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El formato de la llegada es incorrecto")

    def test_mas_long_llegada_tc22(self):
        #Llegada invalida,11 caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/16/20245",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "La llegada tiene mas de 10 caracteres")

    def test_menos_long_llegada_tc23(self):
        #Llegada invalida,9 caracteres
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14/6/2024",
                                                    numdays="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "La llegada tiene menos de 10 caracteres")

    def test_tipo_dato_num_dias_tc24(self):
        #Numero de dias invalido,no es un entero
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14162024",
                                                    numdays="X")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El numero de dias no es un entero")

    def test_mas_num_dias_tc25(self):
        #Numero de dias invalido,11 dias
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14162024",
                                                    numdays="11")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El numero de dias es mayor de 10")

    def test_menos_num_dias_tc26(self):
        #Numero de dias invalido,11 dias
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb="555555555555444a",
                                                    IDCARD="123456789",
                                                    nAMeAndSURNAME="JOSE LOPEZ",
                                                    phonenumber="911234567",
                                                    room_type="SINGLE",
                                                    arrival="14162024",
                                                    numdays="0")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El numero de dias es menor de 1")







if __name__ == '__main__':
    unittest.main()

import unittest
from unittest import TestCase
from HotelManager import HotelManager

class test_room_reservation(TestCase):
    def test_validCreditCard_tc1(self):
        #Tarjeta de credito valida
        my_reservation = HotelManager()
        valor = my_reservation.room_reservation(creditcardNumb = "5555555555554444",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/16/2024",
                                                numdays = "2")
        print(valor)
        self.assertEqual(valor,)

    def test_Luhn_tc2(self):
        #Tarjeta de credito invalida,no cumple algoritmo de Luhn
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagerException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb = "5555555555554442",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/16/2024",
                                                numdays = "2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"La tarjeta de credito no cumple el algoritmo de Luhn")
    def test_tipo_dato_tc3(self):
        #Tarjeta de credito invalida,no es un entero
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagerException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb = "555555555555444a",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/16/2024",
                                                numdays = "2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"La tarjeta de credito no es un entero")

    def test_mas_long_tc4(self):
        #Tarjeta de credito invalida,numero mas largo
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagerException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb = "95555555555554440",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/16/2024",
                                                numdays = "2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El numero de la tarjeta de credito es mas largo")

    def test_menos_long_tc5(self):
        #Tarjeta de credito invalida,numero mas corto
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagerException) as cm:
            valor = my_reservation.room_reservation(creditcardNumb = "555555555554440",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/16/2024",
                                                numdays = "2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El numero de la tarjeta de credito es mas corto")

if __name__ == '__main__':
    unittest.main()

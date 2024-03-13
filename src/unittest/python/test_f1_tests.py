import unittest
from unittest import TestCase
from UC3MTravel import HotelManager


class test_room_reservation(TestCase):
    def test_validateCreditCard_tc1(self):
        my_reservation = HotelManager()
        valor = my_reservation.room_reservation(creditcardNumb = "5555555555554444",
                                                IDCARD = "12345678Z",
                                                nAMeAndSURNAME = "JOSE LOPEZ",
                                                phonenumber = "911234567",
                                                room_type = "SINGLE",
                                                arrival = "14/16/2024",
                                                numdays = "2")
        self.assertEqual(valor, "")


        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

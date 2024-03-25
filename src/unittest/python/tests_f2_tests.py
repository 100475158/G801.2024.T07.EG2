import unittest
from unittest import TestCase
from src.main.python.UC3MTravel.HotelManagementException import HotelManagementException
from src.main.python.UC3MTravel.HotelManager import HotelManager
from src.main.python.UC3MTravel.HotelReservation import HotelReservation
import json
import hashlib
import datetime
class TestGuestArrival(TestCase):
    def test_guest_arrival_test_ok(self):
        for index, input_data in enumerate(self.__test_data_f2):
            if index +1 in [1]:
                test_id = "TC" + str(index + 1)
                with self.subTest(test_id):
                    print("Executing: "+ test_id + ":" +input_data)
                    self.generate_tmp_test_data_file(input_data)
                    hm = HotelManager()
                    room_key= hm.guest_arrival(self.__path_tests + self.tmp_test_data_file)
                    match test_id:
                        case "TC1":
                            self.assertEqual(room_key, "ee25b7b863b77e9106d851875103a3076748a0d487e7a42340ea18855d36b89f")

    def get_store_hash(self):
        try:
            with open(self.__path_data + "all_stays.json", encoding='UTF-8' , mode="r") as f:
                file_hash = hashlib.md5(f.__str__().encode()).hexdigest()
        except FileNotFoundError:
            file_hash = " "
        return file_hash


    def test_guest_arrival_test_tc2(self):
        for index, input_data in enumerate(self.__test_data_f2):
            if index +1 in [2,3,4,5,6,7,8,9,11,12,13,15,16,18,19,20,22,23,24,25,26,27,28,29,30,32,33,34,36,37,39,41,44,45,46,47,49,50,51,53,54,56,57,58,60]:
                test_id = "TC" + str(index + 1)
                with self.subTest(test_id):
                    print("Executing: "+ test_id + ":" +input_data)
                    self.generate_tmp_test_data_file(input_data)
                    hm = HotelManager()
                    room_key= hm.guest_arrival(self.__path_tests + self.tmp_test_data_file)
                    match test_id:
                        case "TC1":
                            self.assertEqual(room_key, "El archivo JSON no tiene la estructura esperada")

import unittest
from unittest import TestCase
from src.main.python.UC3MTravel.HotelManagementException import HotelManagementException
from src.main.python.UC3MTravel.HotelManager import HotelManager
from src.main.python.UC3MTravel.HotelReservation import HotelReservation
import json
import hashlib
import datetime
from pathlib import Path
import os

class TestGuestArrival(TestCase):
    def test_guest_arrival_test_ok(self):
        for index, input_data in enumerate(self.__test_data_f2):
            if index + 1 in [1]:
                test_id = "TC" + str(index + 1)
                with self.subTest(test_id):
                    print("Executing: "+ test_id + ":" +input_data)
                    self.generate_tmp_test_data_file(input_data)
                    hm = HotelManager()
                    room_key= hm.guest_arrival(self.__path_tests + self.tmp_test_data_file)
                    match test_id:
                        case "TC1":
                            print(room_key)
                            self.assertEqual(room_key, "ee25b7b863b77e9106d851875103a3076748a0d487e7a42340ea18855d36b89f")

    def get_store_hash(self):
        try:
            with open(self.__path_data + "all_stays.json", encoding='UTF-8' , mode="r") as f:
                file_hash = hashlib.md5(f.__str__().encode()).hexdigest()
        except FileNotFoundError:
            file_hash = " "
        return file_hash

    def test_guest_arrival_test_invalid(self):
        for index, input_data in enumerate(self.__test_data_f2):
            if index +1 in range(2, 61):
                test_id = "TC" + str(index + 1)
                with self.subTest(test_id):
                    print("Executing: "+ test_id + ":" +input_data)
                    self.generate_tmp_test_data_file(input_data)
                    with self.assertRaises(HotelManagementException) as ar:
                        match test_id:
                            case "TC1", "TC2", "TC3", "TC4", "TC5", "TC6", "TC7", "TC8", "TC9", "TC11","TC12","TC13","TC15","TC16","TC18","TC19","TC20","TC22","TC23","TC24","TC25","TC26","TC27","TC28","TC29","TC30","TC32","TC33","TC34","TC36","TC37","TC39","TC41","TC44","TC45","TC46","TC47","TC49","TC50","TC51","TC53","TC54","TC56","TC57","TC58","TC60":
                                self.assertEqual(ar.exception.message, "El archivo JSON no tiene la estructura esperada")
                            case "TC10":
                                print(ar.exception.message)
                                self.assertEqual(ar.exception.message, "No se encuentra el archivo de datos")
                            case "TC14", "TC21", "TC35", "TC38", "TC42", "TC48", "TC55":
                                print(ar.exception.message)
                                self.assertEqual(ar.exception.message, "Los datos del JSON no tienen valores válidos")
                            case "TC31", "TC52", "TC59":
                                print(ar.exception.message)
                                self.assertEqual(ar.exception.message, "El localizador no se corresponde con los datos almacenados")







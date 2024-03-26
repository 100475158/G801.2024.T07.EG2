import unittest
import json
from pathlib import Path
import os
from unittest import TestCase
from src.main.python.UC3MTravel.HotelManagementException import HotelManagementException
from src.main.python.UC3MTravel.HotelManager import HotelManager


class TestGuestArrival(TestCase):
    """def test_guest_arrival_test_ok(self):
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
"""
#ENFOQUE 1
    def test_guest_arrival_test_tc30(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc30 = ""
            checkin.guest_arrival(tc30)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc31(self):
        #Eliminacion nodo 9 Etiqueta_dato1
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc31 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc31.json"
            checkin.guest_arrival(tc31)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"KEY ERROR")
    def test_guest_arrival_test_tc32(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc32 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc32.json"
            checkin.guest_arrival(tc32)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc33(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc33 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc33.json"
            checkin.guest_arrival(tc33)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc34(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc34 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc34.json"
            checkin.guest_arrival(tc34)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc35(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc35 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc35.json"
            checkin.guest_arrival(tc35)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc36(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc36 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc36.json"
            checkin.guest_arrival(tc36)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc37(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc37 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc37.json"
            checkin.guest_arrival(tc37)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc38(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc38 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc38.json"
            checkin.guest_arrival(tc38)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc39(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc39 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc39.json"
            checkin.guest_arrival(tc39)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc40(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc40 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc40.json"
            checkin.guest_arrival(tc40)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc41(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc41 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc41.json"
            checkin.guest_arrival(tc41)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc42(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc42 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc42.json"
            checkin.guest_arrival(tc42)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc43(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc43 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc43.json"
            checkin.guest_arrival(tc43)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc44(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc44 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc44.json"
            checkin.guest_arrival(tc44)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc45(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc45 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc45.json"
            checkin.guest_arrival(tc45)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc46(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc46 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc46.json"
            checkin.guest_arrival(tc46)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc47(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc47 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc47.json"
            checkin.guest_arrival(tc47)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc48(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc48 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc48.json"
            checkin.guest_arrival(tc48)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc49(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc49 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc49.json"
            checkin.guest_arrival(tc49)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc50(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc50 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc50.json"
            checkin.guest_arrival(tc50)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc51(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc51 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc51.json"
            checkin.guest_arrival(tc51)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc52(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc52 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc52.json"
            checkin.guest_arrival(tc52)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc53(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc53 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc53.json"
            checkin.guest_arrival(tc53)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc54(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc54 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc54.json"
            checkin.guest_arrival(tc54)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc55(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc55 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc55.json"
            checkin.guest_arrival(tc55)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc56(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc56 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc56.json"
            checkin.guest_arrival(tc56)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc57(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc57 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc57.json"
            checkin.guest_arrival(tc57)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc58(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc58 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc58.json"
            checkin.guest_arrival(tc58)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc59(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc59 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc59.json"
            checkin.guest_arrival(tc59)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc60(self):
        #Eliminacion nodo 8 comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc60 = "/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc60.json"
            checkin.guest_arrival(tc60)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON")

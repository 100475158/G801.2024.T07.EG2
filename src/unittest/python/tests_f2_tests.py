import hashlib
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

    def test_guest_arrival_test_tc1(self):
        #Test valido
        hm = HotelManager()
        tc2 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc1.json"
        room_key = hm.guest_arrival(tc2)
        self.assertEqual(room_key, "")


    def test_guest_arrival_test_tc2(self):
        #Duplicación del nodo JSON
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc2 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc2.json"
            checkin.guest_arrival(tc2)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc3(self):
        #Duplicación del nodo Inicio
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc3 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc3.json"
            checkin.guest_arrival(tc3)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc4(self):
        #Duplicación del nodo Datos
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc4 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc4.json"
            checkin.guest_arrival(tc4)
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El localizador no se corresponde con los datos almacenados")
    def test_guest_arrival_test_tc5(self):
        #Duplicación del nodo Fin
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc5 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc5.json"
            checkin.guest_arrival(tc5)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc6(self):
        #Duplicación del nodo Campo1
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc6 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc6.json"
            checkin.guest_arrival(tc6)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc7(self):
        # Duplicación del nodo Separador
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc7 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc7.json"
            checkin.guest_arrival(tc7)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc8(self):
        # Duplicación del nodo Campo2
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc8 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc8.json"
            checkin.guest_arrival(tc8)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc9(self):
        # Duplicación del nodo Comillas de antes de Etiqueta_dato1
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc9 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc9.json"
            checkin.guest_arrival(tc9)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    # Continuar con los siguientes casos de prueba hasta tc29

    def test_guest_arrival_test_tc10(self):
        # Duplicación del nodo Etiqueta_dato1
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc10 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc10.json"
            checkin.guest_arrival(tc10)
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El archivo JSON no tiene la estructura esperada")

    def test_guest_arrival_test_tc11(self):
        # Duplicación del nodo Comillas de después de Etiqueta_dato1
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc11 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc11.json"
            checkin.guest_arrival(tc11)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc12(self):
        # Duplicación del nodo Igualdad del Campo 1
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc12 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc12.json"
            checkin.guest_arrival(tc12)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc13(self):
        # Duplicación del nodo Comillas de después de igualdad del Campo 1
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc13 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc13.json"
            checkin.guest_arrival(tc13)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc14(self):
        # Duplicación del nodo Valor_dato1
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc14 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc14.json"
            checkin.guest_arrival(tc14)
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El localizador no se corresponde con los datos almacenados")

    def test_guest_arrival_test_tc15(self):
        # Duplicación del nodo Comillas del final del Campo 1
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc15 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc15.json"
            checkin.guest_arrival(tc15)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc16(self):
        # Duplicación del nodo Comillas del inicio de Campo 2
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc16 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc16.json"
            checkin.guest_arrival(tc16)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc17(self):
        # Duplicación del nodo Etiqueta_dato2
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc17 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc17.json"
            checkin.guest_arrival(tc17)
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El archivo JSON no tiene la estructura esperada")

    def test_guest_arrival_test_tc18(self):
        # Duplicación del nodo Comillas de después de Etiqueta_dato2
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc18 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc18.json"
            checkin.guest_arrival(tc18)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc19(self):
        # Duplicación del nodo Igualdad del Campo 2
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc19 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc19.json"
            checkin.guest_arrival(tc19)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc20(self):
        # Duplicación del nodo Comillas de después de igualdad del Campo 2
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc20 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc20.json"
            checkin.guest_arrival(tc20)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc21(self):
        # Duplicación del nodo Valor_dato2
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc21 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc21.json"
            checkin.guest_arrival(tc21)
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El localizador no se corresponde con los datos almacenados")

    def test_guest_arrival_test_tc22(self):
        # Duplicación del nodo Comillas del Campo 2
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc22 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc22.json"
            checkin.guest_arrival(tc22)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc23(self):
        # Eliminación del nodo JSON
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc23 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc23.json"
            checkin.guest_arrival(tc23)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc24(self):
        # Eliminación del nodo Inicio
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc24 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc24.json"
            checkin.guest_arrival(tc24)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc25(self):
        # Eliminación del nodo Datos
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc25 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc25.json"
            checkin.guest_arrival(tc25)
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El archivo JSON no tiene la estructura esperada")

    def test_guest_arrival_test_tc26(self):
        # Eliminación del nodo Fin
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc26 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc26.json"
            checkin.guest_arrival(tc26)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc27(self):
        # Eliminación del nodo Campo1
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc27 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc27.json"
            checkin.guest_arrival(tc27)
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El archivo JSON no tiene la estructura esperada")

    def test_guest_arrival_test_tc28(self):
        # Eliminación del nodo Separador
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc28 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc28.json"
            checkin.guest_arrival(tc28)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc29(self):
        # Eliminación del nodo Campo2
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc29 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc29.json"
            checkin.guest_arrival(tc29)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")


    def test_guest_arrival_test_tc30(self):
        #Eliminación del nodo Comillas
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc30 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc30.json"
            checkin.guest_arrival(tc30)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")
    def test_guest_arrival_test_tc31(self):
        #Eliminacion nodo 9 Etiqueta_dato1
        checkin=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc31 = "C:/PycharmProjects/G801.2024.T07.EG2/src/json_files/entradas_f2/tc31.json"
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


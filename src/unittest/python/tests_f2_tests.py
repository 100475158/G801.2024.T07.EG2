from pathlib import Path
import os
from unittest import TestCase
from src.main.python.UC3MTravel.HotelManagementException import HotelManagementException
from src.main.python.UC3MTravel.HotelManager import HotelManager
from freezegun import freeze_time

class TestGuestArrival(TestCase):
    @classmethod
    def setUpClass(cls):
        json_files_path = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/json_files/"
        cls.file_store = json_files_path + "hotel_stays.json"
        if os.path.isfile(cls.file_store):
            os.remove(cls.file_store)

    @freeze_time("2024-10-14")
    def test_guest_arrival_test_tc1(self):
        #Test valido
        checkin = HotelManager()
        tc1 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tcc1.json"
        key = checkin.guest_arrival(tc1)
        print(key)

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
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El localizador no se corresponde con los datos almacenados")

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
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El localizador no se corresponde con los datos almacenados")

    def test_guest_arrival_test_tc29(self):
        # Eliminación del nodo Campo2
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc29 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc29.json"
            checkin.guest_arrival(tc29)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")


    def test_guest_arrival_test_tc30(self):
        # Eliminacion nodo 8 comillas
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc30 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc30.json"
            checkin.guest_arrival(tc30)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc31(self):
        # Eliminacion nodo 9 Etiqueta_dato1
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc31 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc31.json"
            checkin.guest_arrival(tc31)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El archivo JSON no tiene la estructura esperada")
    def test_guest_arrival_test_tc32(self):
        # Eliminacion nodo 10 comillas
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc32 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc32.json"
            checkin.guest_arrival(tc32)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc33(self):
        # Eliminacion nodo 11 Igualdad
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc33 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc33.json"
            checkin.guest_arrival(tc33)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc34(self):
        # Eliminacion nodo 12 comillas
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc34 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc34.json"
            checkin.guest_arrival(tc34)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc35(self):
        # Eliminacion nodo 14 Valor_dato1
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc35 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc35.json"
            checkin.guest_arrival(tc35)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El localizador no se corresponde con los datos almacenados")

    def test_guest_arrival_test_tc36(self):
        # Eliminacion nodo 16 comillas
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc36 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc36.json"
            checkin.guest_arrival(tc36)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc37(self):
        # Eliminacion nodo 17 comillas
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc37 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc37.json"
            checkin.guest_arrival(tc37)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc38(self):
        # Eliminacion nodo 18 Etiqueta_dato2 comillas
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc38 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc38.json"
            checkin.guest_arrival(tc38)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El archivo JSON no tiene la estructura esperada")

    def test_guest_arrival_test_tc39(self):
        # Eliminacion nodo 19 comillas
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc39 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc39.json"
            checkin.guest_arrival(tc39)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc40(self):
        # Eliminacion nodo 20 Igualdad
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc40 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc40.json"
            checkin.guest_arrival(tc40)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc41(self):
        # Eliminacion nodo 21 comillas
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc41 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc41.json"
            checkin.guest_arrival(tc41)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc42(self):
        # Eliminacion nodo 23 Valor_dato2
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc42 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc42.json"
            checkin.guest_arrival(tc42)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El localizador no se corresponde con los datos almacenados")

    def test_guest_arrival_test_tc43(self):
        # Eliminacion nodo 25 comillas
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc43 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc43.json"
            checkin.guest_arrival(tc43)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc44(self):
        # Modificacion nodo 5 { por }
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc44 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc44.json"
            checkin.guest_arrival(tc44)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc45(self):
        # Modificacion nodo 9 } por {
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc45 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc45.json"
            checkin.guest_arrival(tc45)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc46(self):
        # Modificacion nodo 19 , por .
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc46 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc46.json"
            checkin.guest_arrival(tc46)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc47(self):
        # Modificacion nodo 29 "" por !
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc47 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc47.json"
            checkin.guest_arrival(tc47)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc48(self):
        # Modificacion nodo 30 Localizer por Arrival
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc48 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc48.json"
            checkin.guest_arrival(tc48)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El archivo JSON no tiene la estructura esperada")

    def test_guest_arrival_test_tc49(self):
        # Modificacion nodo 31 "" por ¿
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc49 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc49.json"
            checkin.guest_arrival(tc49)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc50(self):
        # Modificacion nodo 32 : por ,
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc50 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc50.json"
            checkin.guest_arrival(tc50)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc51(self):
        # Modificacion nodo 33 " por :
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc51 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc51.json"
            checkin.guest_arrival(tc51)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc52(self):
        # Modificacion nodo 35 String de 32 caracteres en hexadecimal por otro invalido de 31 caracteres
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc52 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc52.json"
            checkin.guest_arrival(tc52)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El localizador no se corresponde con los datos almacenados")

    def test_guest_arrival_test_tc53(self):
        # Modificacion nodo 37 " por /
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc53 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc53.json"
            checkin.guest_arrival(tc53)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc54(self):
        # Modificacion nodo 38 " por ;
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc54 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc54.json"
            checkin.guest_arrival(tc54)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc55(self):
        # Modificacion nodo 39 IdCard
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc55 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc55.json"
            checkin.guest_arrival(tc55)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El archivo JSON no tiene la estructura esperada")

    def test_guest_arrival_test_tc56(self):
        # Modificacion nodo 40 " por .
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc56 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc56.json"
            checkin.guest_arrival(tc56)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc57(self):
        # Modificacion nodo : por _
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc57 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc57.json"
            checkin.guest_arrival(tc57)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc58(self):
        # Modificacion nodo 42 " por @
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc58 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc58.json"
            checkin.guest_arrival(tc58)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_guest_arrival_test_tc59(self):
        # Modificacion nodo 44 valid IdCard por invalid IdCard(sin letra al final)
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc59 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc59.json"
            checkin.guest_arrival(tc59)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: El localizador no se corresponde con los datos almacenados")

    def test_guest_arrival_test_tc60(self):
        # Modificacion nodo 46 " por ,
        checkin = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            tc60 = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/entradas_f2/tc60.json"
            checkin.guest_arrival(tc60)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")



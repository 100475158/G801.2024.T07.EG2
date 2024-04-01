from pathlib import Path
from unittest import TestCase
from src.main.python.UC3MTravel.HotelManagementException import HotelManagementException
from src.main.python.UC3MTravel.HotelManager import HotelManager
from freezegun import freeze_time
import os


class TestGuestArrival(TestCase):
    @classmethod
    def setUpClass(cls):
        json_files_path = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/json_files/"
        cls.file_store2 = json_files_path + "registro_entregas.json"
        if os.path.isfile(cls.file_store2):
            os.remove(cls.file_store2)

    @freeze_time("2024-10-16")
    def test_guest_checkout_test_tc1(self):
        # Test valido
        checkout = HotelManager()
        key = "2f22c203b2765e4aa7c2308d3e41cdd64470bf9c701129ede7ddd34c3011063e"
        checkout.guest_checkout(key)

    @freeze_time("2024-10-16")
    def test_guest_checkout_test_tc2(self):
        #Room key no es valido
        checkout=HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            checkout.guest_checkout("770c547dc8adacd3860f47b8c9e8f6815269f967478a141e458aa4104dfab2")
        self.assertEqual(cm.exception.message, "Error de procesamiento interno: La cadena de entrada no contiene un código de habitación válido")

    @freeze_time("2024-10-16")
    def test_guest_checkout_test_tc3(self):
        json_files_path = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/json_files/"
        file_store = json_files_path + "hotel_stays.json"

        # Guarda el contenido original del archivo
        original_content = None
        if os.path.isfile(file_store):
            with open(file_store, "r") as f:
                original_content = f.read()

        # Elimina el archivo antes de ejecutar el caso de prueba
        if os.path.isfile(file_store):
            os.remove(file_store)

        # No se encuentra el archivo hotel_stays.json
        checkout = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            checkout.guest_checkout("770c547dc8adacd3860f47b8c9e8f6815269f967478a141e458aa4104dfab24f")
        self.assertEqual(cm.exception.message, "No se encuentra el archivo de datos")

        # Restaura el contenido original del archivo después de completar el caso de prueba
        if original_content is not None:
            with open(file_store, "w") as f:
                f.write(original_content)

    @freeze_time("2024-10-16")
    def test_guest_checkout_test_tc4(self):
        # El room key no coincide con el del archivo de estancias
        checkout = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            checkout.guest_checkout("770c547dc8adacd3860f47b8c9e8f6815269f967478a141e458aa4104dfab24f")
        self.assertEqual(cm.exception.message,
                         "Error de procesamiento interno: El código de habitación no estaba registrado")

    @freeze_time("2024-10-18")
    def test_guest_checkout_test_tc5(self):
        # La fecha de salida no coincide con la esperada
        checkout = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            checkout.guest_checkout("770c547dc8adacd3860f47b8c9e8f6815269f967478a141e458aa4104dfab24f")
        self.assertEqual(cm.exception.message,
                         "Error de procesamiento interno: La fecha de salida no es válida")


    @freeze_time("2024-10-16")
    def test_guest_checkout_test_tc6(self):
        # No se encuentra el archivo registro_entregas.json
        checkout = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            checkout.guest_checkout("770c547dc8adacd3860f47b8c9e8f6815269f967478a141e458aa4104dfab24f")
        self.assertEqual(cm.exception.message,"No se encuentra el archivo de datos")

    @freeze_time("2024-10-16")
    def test_guest_checkout_test_tc7(self):
        # El room_key no se encuentra en el archivos de estancias (el archivo sí existe)
        checkout = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            checkout.guest_checkout("770c547dc8adacd3860f47b8c9e8f6815269f967478a141e458aa4104dfab24f")
        self.assertEqual(cm.exception.message,"Error de procesamiento interno: El código de habitación no estaba registrado")
"""
Este módulo contiene pruebas para la F3.
"""

import os
import sys
from pathlib import Path
from unittest import TestCase
from freezegun import freeze_time
from UC3MTravel.HotelManagementException import HotelManagementException
from UC3MTravel.HotelManager import HotelManager

# Obtenemos el directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtenemos la ruta del directorio src
src_dir = os.path.join(current_dir, '..', '..', '..', 'main', 'python')
# Añadimos la ruta del directorio src al sys.path
sys.path.append(src_dir)


class TestGuestArrival(TestCase):
    """
    Clase principal para pruebas relacionadas con la salida de huéspedes..
    """
    file_store = None

    @classmethod
    def setUpClass(cls):
        json_files_path = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/json_files/"
        cls.file_store = json_files_path + "registro_entregas.json"
        if os.path.isfile(cls.file_store):
            os.remove(cls.file_store)

    @freeze_time("2024-10-16")
    def test_guest_checkout_test_tc1(self):
        """
        Caso válido.
        """
        checkout = HotelManager()
        key = "2f22c203b2765e4aa7c2308d3e41cdd64470bf9c701129ede7ddd34c3011063e"
        checkout.guest_checkout(key)

    @freeze_time("2024-10-16")
    def test_guest_checkout_test_tc2(self):
        """
        Room key no es valido.
        """
        checkout = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            checkout.guest_checkout("770c547dc8adacd3860f47b8c9e8f6815269f967478a141e458aa4104dfab2")
        self.assertEqual(cm.exception.message, "Error de procesamiento interno:"
                                               " La cadena de entrada no contiene un código de habitación válido")

    @freeze_time("2024-10-16")
    def test_guest_checkout_test_tc3(self):
        """
        No encuentra el archivo hotel_stays.
        """
        json_files_path = str(Path.home()) + "/PycharmProjects/G801.2024.T07.EG2/src/json_files/"
        file_store = json_files_path + "hotel_stays.json"

        # Guarda el contenido original del archivo
        original_content = None
        if os.path.isfile(file_store):
            with open(file_store, "r", encoding='utf-8') as f:
                original_content = f.read()

        # Elimina el archivo antes de ejecutar el caso de prueba
        if os.path.isfile(file_store):
            os.remove(file_store)

        # No se encuentra el archivo hotel_stays.json
        checkout = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            checkout.guest_checkout("2f22c203b2765e4aa7c2308d3e41cdd64470bf9c701129ede7ddd34c3011063e")
        self.assertEqual(cm.exception.message, "No se encuentra el archivo de datos")

        # Restaura el contenido original del archivo después de completar el caso de prueba
        if original_content is not None:
            with open(file_store, "w", encoding='utf-8') as f:
                f.write(original_content)

    @freeze_time("2024-10-16")
    def test_guest_checkout_test_tc4(self):
        """
        El room key no coincide con el del archivo de estancias.
        """
        checkout = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            checkout.guest_checkout("770c547dc8adacd3860f47b8c9e8f6815269f967478a141e458aa4104dfab24f")
        self.assertEqual(cm.exception.message,
                         "Error de procesamiento interno: El código de habitación no estaba registrado")

    @freeze_time("2024-10-18")
    def test_guest_checkout_test_tc5(self):
        """
        La fecha de salida no coincide con la esperada.
        """
        checkout = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            checkout.guest_checkout("2f22c203b2765e4aa7c2308d3e41cdd64470bf9c701129ede7ddd34c3011063e")
        self.assertEqual(cm.exception.message,
                         "Error de procesamiento interno: La fecha de salida no es válida")

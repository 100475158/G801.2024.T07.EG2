import unittest
from src.main.python.UC3MTravel.HotelManagementException import HotelManagementException
from src.main.python.UC3MTravel.HotelManager import HotelManager

class TestRoomReservation(unittest.TestCase):

    def test_room_reservation_valid1(self):
        mi_reserva=HotelManager()
        valor=mi_reserva.room_reservation()
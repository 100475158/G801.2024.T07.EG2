import unittest
from UC3MTravel import HotelManagerException
from UC3MTravel import HotelManager

class TestRoomReservation(unittest.TestCase):

    def test_room_reservation_valid1(self):
        mi_reserva=HotelManager()
        valor=mi_reserva.room_reservation()

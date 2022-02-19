import unittest
from networkspeed import Device, NetworkStation

class TestSpeed(unittest.TestCase):
    def test_positive(self):
        """
        Test for the case where distance<reach
        """
        device = Device((0,0))
        station = [NetworkStation((0,0), 9)]
        best_speed, station = device.get_best_speed(station)
        self.assertEqual(best_speed, 81.0)
        self.assertEqual(station.location[0],0)
        self.assertEqual(station.location[1],0)

    def test_negative(self):
        """
        Test for the case where distance>reach
        """
        device = Device((100,100))
        station = [NetworkStation((0,0), 9)]
        best_speed, station = device.get_best_speed(station)
        self.assertEqual(best_speed, -1)
        self.assertEqual(station, None)
        
    def test_boundary(self):
        """
        Test for the case where distance=reach
        """
        device = Device((0,0))
        station = [NetworkStation((9,0), 9)]
        best_speed, station = device.get_best_speed(station)
        self.assertEqual(best_speed, 0.0)
        self.assertEqual(station.location[0],9)
        self.assertEqual(station.location[1],0)

    




if __name__ == '__main__':
    unittest.main()

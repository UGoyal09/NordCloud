from typing import List, Tuple

class NetworkStation():
    """
    Defines the NetworkStation object
    """
    def __init__(self, location: Tuple[int, int], reach: int):
        self.location = location
        self.reach = reach


class Device():
    """
    Defines the Device object
    """
    def __init__(self, location: Tuple[int, int]):
        self.location = location

    def get_speed(self, station: NetworkStation) -> float:
        """
        Get the speed from this device to a given station only if distance is less than reach
        """
        distance_from_station = get_distance(self.location, station.location)
        if distance_from_station > station.reach:
            return -1
        return round((station.reach - distance_from_station) ** 2,2)

    def get_best_speed(self, stations: List[NetworkStation]) -> Tuple[int, Tuple[int, int]]:
        """
        Get the best speed of this device among all the stations
        """
        speeds = []
        for station in stations:
            speed = self.get_speed(station)
            if speed == -1:
                speeds.append((-1, None))
            else:
                speeds.append((speed, station))
        speeds.sort(key=lambda x: x[0], reverse=True)
        return speeds[0]
    

def get_distance(devicePoint: Tuple[int, int], stationPoint: Tuple[int, int]):
    """
    Cartesian distance between two points
    """
    return ((devicePoint[0]-stationPoint[0])**2 \
            + (devicePoint[1]-stationPoint[1])**2)**0.5


def get_results():
    devices = [Device((0, 0)), 
                Device((100, 100)), 
                Device((15, 10)), 
                Device((18, 18)), 
                Device((13, 13)), 
                Device((25, 99))]

    stations = [NetworkStation((0,0), 9), 
                NetworkStation((20,20), 6), 
                NetworkStation((10,0), 12), 
                NetworkStation((5,5), 13), 
                NetworkStation((99,25), 22)]

    results = []
    for device in devices:
        best_speed, station = device.get_best_speed(stations)
        if best_speed == -1:
            results.append(f"No network station within reach for point ({device.location[0]},{device.location[1]})")
        else:
            results.append(f"Best network station for point ({device.location[0]},{device.location[1]}) is ({station.location[0]},{station.location[1]}) with speed <strong>{best_speed}</strong>")
    return "<br>".join(results)

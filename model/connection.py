from dataclasses import dataclass


@dataclass
class Connection:

    def __init__(self, origin_airport_id: int, destination_airport_id: int, distance: float, count: int):
        self.origin_airport_id = origin_airport_id
        self.destination_airport_id = destination_airport_id
        self.distance = distance
        self.count = count

    def __str__(self):
        return f"{self.origin_airport_id} - {self.destination_airport_id}, average distance={self.distance}, count={self.count}"

    def updateConnection(self, dis, c):
        previous_distance = self.distance
        previous_count = self.count
        new_distance = round((previous_distance * previous_count + dis * c) / (previous_count + c), 3)
        self.distance = new_distance
        self.count = previous_count + c

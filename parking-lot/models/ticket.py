from typing import Literal


class Ticket:
    def __init__(self, vehicle_type: Literal["CAR", "TRUCK", "BIKE"]):
        self.id = ""
        self.type = vehicle_type
        pass

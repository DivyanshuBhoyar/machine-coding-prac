from typing import List
from .floor import Floor


class ParkingLotApp:
    def __init__(self, id: str, no_floors: int, no_slots: int):
        self.id = id
        self.tickets = set()

        self.floors = ["test" for i in range(no_floors)]

    def get_floors(self) -> List[Floor]:
        return self.floors

    def save_tickets(self, t_id):
        self.tickets.add(t_id)

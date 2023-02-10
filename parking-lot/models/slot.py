from typing import Literal

from .ticket import Ticket


class Slot:
    def __init__(self, type: Literal["CAR", "TRUCK", "BIKE"], floor: int,  pos: int):
        self.type = type
        self.ticket = None
        self.id = f"s_{floor}_{pos}__{type}"

    def use_slot(self, ticket: Ticket):
        try:
            if self.type == ticket.type and not self.ticket:
                self.ticket = ticket
                self.ticket.id = self.id
            return self.ticket
        except Exception as e:
            return None

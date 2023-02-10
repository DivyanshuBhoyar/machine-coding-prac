from typing import List
from .slot import Slot


class Floor:
    def __init__(self, n: int, capacity: int):
        self.floor_no = n
        self.slots = self.create_slots(capacity)
        self.min_vacant_pos = 0
        self.slots_avail = capacity

    def create_slots(self, no):
        slots = [] * self.slots_avail
        slots[0] = Slot(type="TRUCK", floor=self.floor_no, pos=1)
        try:
            for i in range(1, no):
                print(i)
                if i < 3:
                    slots[i] = Slot(type="BIKE", floor=self.floor_no, pos=i+1)
                    break
                slots[i] = Slot(type="CAR", floor=self.floor_no, pos=i+1)
        except Exception as e:
            print('error', e)

    def get_slots(self) -> List[Slot]:
        return self.slots

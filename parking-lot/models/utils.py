from .app import ParkingLotApp
from .ticket import Ticket


class Utils:
    use_debug = False

    @staticmethod
    def greet(): print("welcome")

    @staticmethod
    def handle_park_cmd(app: ParkingLotApp, args):
        type, reg_no, color = args[0], args[1], args[2]
        for f in app.get_floors():
            if f.slots_avail > 0:
                min_pos = f.get_slots()[f.min_vacant_pos]
                min_pos.use_slot(ticket=Ticket(type))
                app.save_ticket(min_pos.id)   # pos.id is same as ticket id
                print(min_pos.id)
                return
        print("no slots found")

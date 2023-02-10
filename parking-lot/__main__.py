from models.app import ParkingLotApp


def main():
    app = None

    while True:
        cmd = input("Enter command\n").split()
        ctype, cargs = cmd[0], cmd[1:]

        if ctype == 'CREATE_PARKING_LOT' and len(cargs) == 3:
            try:
                id = cargs[0]
                floors, cap = int(cargs[1]), int(cargs[2])
                app = ParkingLotApp(
                    id=id, no_floors=floors, no_slots=cap)
                print(vars(app))
            except Exception as e:
                print("error", e)
            return

        if ctype == "PARK_VEHICLE" and len(cargs) == 3 and app:
            Utils.handle_park_cmd(app, cargs)


if __name__ == "__main__":
    main()

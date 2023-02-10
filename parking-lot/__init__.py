__name__ = "Parking Lot design"
__author__ = "Divyanshu"
__version__ = '0.1.0'

''' 
INPUT FORMAT

    create_parking_lot <parking_lot_id> <no_of_floors> <no_of_slots_per_floor>

    park_vehicle <vehicle_type> <reg_no> <color>

    unpark_vehicle <ticket_id>

    display <display_type> <vehicle_type>

    Possible values of display_type: free_count, free_slots, occupied_slots
'''
'''
OUTPUT FORMAT

    create_parking_lot
        Created parking lot with <no_of_floors> floors and <no_of_slots_per_floor> slots per floor

    park_vehicle
        Parked vehicle. Ticket ID: <ticket_id>
        Print "Parking Lot Full" if slot is not available for that vehicle type.

    unpark_vehicle
        Unparked vehicle with Registration Number: <reg_no> and Color: <color>
        Print "Invalid Ticket" if ticket is invalid or parking slot is not occupied.

    display free_count <vehicle_type>
        No. of free slots for <vehicle_type> on Floor <floor_no>: <no_of_free_slots>
        The above will be printed for each floor.

    display free_slots <vehicle_type>
        Free slots for <vehicle_type> on Floor <floor_no>: <comma_separated_values_of_slot_nos>
        The above will be printed for each floor.

    display occupied_slots <vehicle_type>
        Occupied slots for <vehicle_type> on Floor <floor_no>: <comma_separated_values_of_slot_nos>
        The above will be printed for each floor.

'''

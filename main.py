from datetime import datetime, timedelta
from Legitarsasag import Airline
from jegyfoglalas import TicketReservation

def main():
    airline = Airline("Sky Horizon")

    first_plane_seed = airline.create_domestic_flight("Budapest", "Debrecen", 50, 30_000,
                                                      datetime.now() + timedelta(days=5))
    first_plane_seed.booking("Petrovics Péter")
    first_plane_seed.booking("Álmos Ádám")

    second_plane_seed = airline.create_domestic_flight("Győr", "Pécs", 50, 52_000, datetime.now() + timedelta(days=3))
    second_plane_seed.booking("Kiss Kinga")
    second_plane_seed.booking("Nagy Nóra")

    third_plane_seed = airline.create_international_flights("Budapest", "Isztambul", 80, 140_700,
                                                            datetime.now() + timedelta(days=2))
    third_plane_seed.booking("Elek Endre")
    third_plane_seed.booking("Kovács Kristóf")

    # fixture flight numbers
    first_plane_seed_number = first_plane_seed._Flight__flight_number
    first_plane_seed._Flight__flight_number = 'AB-10'
    airline._Airline__domestic_flights['AB-10'] = airline._Airline__domestic_flights.pop(first_plane_seed_number)

    second_plane_seed_number = second_plane_seed._Flight__flight_number
    second_plane_seed._Flight__flight_number = 'AB-11'
    airline._Airline__domestic_flights['AB-11'] = airline._Airline__domestic_flights.pop(second_plane_seed_number)

    third_plane_seed_number = third_plane_seed._Flight__flight_number
    third_plane_seed._Flight__flight_number = 'AB-12'
    airline._Airline__international_flights['AB-12'] = airline._Airline__international_flights.pop(
        third_plane_seed_number)
    third_plane_seed._Flight__date = datetime(2024, 1, 1)

    booking_system = TicketReservation(airline)
    booking_system.start()


if __name__ == "__main__":
    main()

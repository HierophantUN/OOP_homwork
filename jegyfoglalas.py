# Jegyfoglalás
from Legitarsasag import Airline


class TicketReservation:

    def __init__(self, airline: Airline):
        self.airline = airline

    def start(self):
        while True:
            self.__display_menu(self.airline.get_name(), self.airline.get_monogram())
            try:
                menu_option = self.__get_user_input_as_int("Enter menu number: ")
            except ValueError as e:
                print(f"{e}")
                continue

            if menu_option == 1:
                self.__ticket_booking()

            if menu_option == 2:
                self.__cancel_booking()

            if menu_option == 3:
                self.__list_bookings()

            if menu_option == 4:
                print("Exit")
                exit()

    def __list_bookings(self):
        try:
            self.__space_terminal()
            print("Domestic Flights: ")
            self.__print_flights(self.airline.get_domestic_flights())
            print("\nInternational Flights: ")
            self.__print_flights(self.airline.get_international_flights())
            self.__space_terminal()
            flight_number = self.__get_user_input_as_string("Enter Flight number: ")
            flight = self.airline.get_flight_by_number(flight_number)
            self.__print_flight(flight)
        except ValueError as e:
            print(f"An error occurred: {e}\n")

    def __ticket_booking(self):
        try:
            flight_number = self.__get_user_input_as_string("Enter Flight number: ")
            flight = self.airline.get_flight_by_number(flight_number)
            name = self.__get_user_input_as_string("Enter Person name: ")
            seat_number, seat_price = flight.booking(name)
            print(
                f"The booking was completed for flight: {flight_number}, seat number: {seat_number}, price: {seat_price}")
        except ValueError as e:
            print(f"An error occurred: {e}\n")

    def __cancel_booking(self):
        try:
            flight_number = self.__get_user_input_as_string("Enter Flight number: ")
            flight = self.airline.get_flight_by_number(flight_number)
            name = self.__get_user_input_as_int("Enter seat number: ")
            flight.cancel_booking(name)
            print(f"The booking was cancelled for flight: {flight_number} seat number: {name}")
        except ValueError as e:
            print(f"An error occurred: {e}\n")

    @staticmethod
    def __print_flights(flights):
        for key, value in flights.items():
            print(
                f"Flight number: {key}, date: {value.get_date()}, Destination: [ {value.get_departure()} -> {value.get_destination()} ]")

    @staticmethod
    def __get_user_input_as_int(msg):
        try:
            return int(input(msg))
        except ValueError:
            raise ValueError("Invalid input format, it must be a number")

    @staticmethod
    def __get_user_input_as_string(msg):
        return str(input(msg)).strip()

    @staticmethod
    def __print_flight(flight, items_per_line=10):
        print("\n")
        print(f"Flight number: {flight.get_flight_number()}")
        print(f"Date: {flight.get_date()}")
        print(f"Destination: [ {flight.get_departure()} -> {flight.get_destination()} ]")
        print(f"Seat price: {flight.get_seat_price()}, income: {flight.get_income()}")
        print("Seats: ")
        for i, (key, value) in enumerate(flight.get_seats().items(), 1):
            display_value = value if value != "" else "-"
            print(f"{key}: {display_value}", end=" | " if i % items_per_line != 0 else "\n")
        if len(flight.get_seats()) % items_per_line != 0:
            print()
        print("\n")

    @staticmethod
    def __display_menu(name, monogram):
        print("-----------------------------------------------")
        print("✈️ --- Flight Ticket Booking System menu --- ✈️")
        print("-----------------------------------------------")
        print(f"Welcome: {name} ({monogram})")
        print("1. Booking a ticket")
        print("2. Cancel ticket booking")
        print("3. List bookings")
        print("4. Exit")

    @staticmethod
    def __space_terminal():
        print("\n")

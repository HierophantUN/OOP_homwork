import copy

from belfoldijarat import DomesticFlight
from kulfoldijarat import InternationalFlight


class Airline:

    def __init__(self, name):
        self.__domestic_destinations = ["Budapest", "Debrecen", "Pécs", "Győr", "Szeged"]
        self.__domestic_flights = {}
        self.__international_destinations = ["Budapest", "Bécs", "London", "Párizs", "Kijev", "Isztambul"]
        self.__international_flights = {}
        self.__name = name
        self.__monogram = self.__generate_monogram(name)

    def create_domestic_flight(self, departure, destination, seats_number, seats_price, date):
        self.__validate_destinations_or_die(departure, destination, self.__domestic_destinations)
        domestic_flight = DomesticFlight(self.__monogram, departure, destination, seats_number, seats_price, date)
        flight_number = domestic_flight.get_flight_number()
        self.__domestic_flights[flight_number] = domestic_flight
        return domestic_flight

    def create_international_flights(self, departure, destination, seats_number, seats_price, date):
        self.__validate_destinations_or_die(departure, destination, self.__international_destinations)
        international_flight = InternationalFlight(self.__monogram, departure, destination, seats_number, seats_price,
                                                   date)
        flight_number = international_flight.get_flight_number()
        self.__international_flights[flight_number] = international_flight
        return international_flight

    def get_domestic_destinations(self):
        return copy.deepcopy(self.__domestic_destinations)

    def get_domestic_flights(self):
        return copy.deepcopy(self.__domestic_flights)

    def get_flight_by_number(self, flight_number):
        if flight_number in self.__domestic_flights:
            return self.__domestic_flights[flight_number]
        if flight_number in self.__international_flights:
            return self.__international_flights[flight_number]
        raise ValueError(F"Flight number was not found: {flight_number}")

    def get_international_destinations(self):
        return copy.deepcopy(self.__international_destinations)

    def get_international_flights(self):
        return copy.deepcopy(self.__international_flights)

    def get_name(self):
        return self.__name

    def get_monogram(self):
        return self.__monogram

    @staticmethod
    def __validate_destinations_or_die(departure, destination, destinations):
        if departure == destinations:
            raise ValueError(f"Departure: {departure} cant be same as destination: {destination}")
        if departure not in destinations:
            raise ValueError(f"Departure: {departure} not in destinations list: {destination}")
        if destination not in destinations:
            raise ValueError(f"Destination: {destination} not in destinations list: {destination}")

    @staticmethod
    def __generate_monogram(name):
        name_parts = name.upper().split()
        if len(name_parts) >= 2:
            return f"{name_parts[0][0]}{name_parts[-1][0]}"
        return name_parts[0][0] * 2

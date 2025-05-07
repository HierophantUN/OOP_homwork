import copy
from abc import ABC, abstractmethod
import random
from datetime import datetime

# Járat
class Flight(ABC):

    def __init__(self, airline_monogram, departure, destination, seats_number, seat_price, date):
        self.__flight_number = self.__generate_flight_number(airline_monogram)
        self.__departure = departure
        self.__destination = destination
        self.__seats_number = seats_number
        self.__date = date
        self.__seats = {i: "" for i in range(1, seats_number + 1)}
        self.__seat_price = seat_price
        self.__income = 0

    @abstractmethod
    def get_max_seat_price(self):
        pass

    @abstractmethod
    def get_minimum_seat_price(self):
        pass

    @abstractmethod
    def get_max_seats_number(self):
        pass

    def booking(self, name):
        self.__validate_date()

        if name is None or name == "":
            raise ValueError("Name can't be empty or blank")

        seat_number = self.__get_first_free_seat()
        self.__seats[seat_number] = name
        self.__income += self.__seat_price
        return seat_number, self.__seat_price

    def cancel_booking(self, seat_number):
        self.__validate_date()
        if seat_number < 1 or seat_number > self.__seats_number:
            raise ValueError(
                f"Seat number not belong to any reservation it must be between: {1} - {self.__seats_number}")
        if self.__seats[seat_number] == "":
            raise ValueError("There is no booking for this chair")
        self.__seats[seat_number] = ""
        self.__income -= self.__seat_price

    def get_flight_number(self):
        return self.__flight_number

    def get_departure(self):
        return self.__departure

    def get_destination(self):
        return self.__destination

    def get_seats_number(self):
        return self.__seats_number

    def get_seats(self):
        return copy.deepcopy(self.__seats)

    def get_seat_price(self):
        return self.__seat_price

    def get_income(self):
        return self.__income

    def get_date(self):
        return self.__date

    def __get_first_free_seat(self):
        for seat_number, person_name in self.__seats.items():
            if person_name == "":
                return seat_number
        raise ValueError("No more empty seats lef")

    def __validate_date(self):
        if self.__date < datetime.now():
            raise ValueError("The booking time is invalid. Please select a future date.")

    @staticmethod
    def __generate_flight_number(monogram):
        return f"{monogram}-{random.randint(10000, 99999)}"

# Belföldi járat
from Flight import Flight

class DomesticFlight(Flight):

    MINIMUM_SEAT_PRICE = 10_000
    MAX_SEAT_PRICE = 100_000
    MAX_SEATS = 50

    def __init__(self, airline_monogram, departure, destination, seats_number, seat_price, date):
        if seat_price > self.MAX_SEAT_PRICE:
            raise ValueError(f"Price cant be bigger then max price: {self.MAX_SEAT_PRICE}")
        if seat_price < self.MINIMUM_SEAT_PRICE:
            raise ValueError(f"Price cant be smaller then min price: {self.MINIMUM_SEAT_PRICE}")
        if seats_number > self.MAX_SEATS:
            raise ValueError(f"Max seats size is: {self.MAX_SEATS}")
        super().__init__(airline_monogram, departure, destination, seats_number, seat_price, date)

    def get_minimum_seat_price(self):
        return self.MAX_SEAT_PRICE

    def get_max_seats_number(self):
        return self.MAX_SEAT_PRICE

    def get_max_seat_price(self):
        return self.MAX_SEATS

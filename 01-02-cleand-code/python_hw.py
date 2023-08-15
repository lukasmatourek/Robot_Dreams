import random
from datetime import datetime


class FlyingTicket:
    """Flying ticket class

    Attributes:
        departure_airport (str): Airport from which is flight
        arrival_airport (str): Airport the fly arrives
        departure_time (datetime): Time of departure
        arrival_time (datetime): Time of arrival into target destination
        price (float): Price of ticket
    """

    def __init__(
            self,
            departure_airport: str,
            arrival_airport: str,
            departure_time: datetime,
            arrival_time: datetime,
            price: float,
    ):
        self.ticket_id: int = random.randint(1, 1000000)
        self.departure_airport: str = departure_airport
        self.arrival_airport: str = arrival_airport
        self.arrival_time: datetime = arrival_time
        self.departure_time: datetime = departure_time
        self.price: float = price

    def get_details(self) -> None:
        """Print ticket information"""

        print(f"Ticket ID: {self.ticket_id}")
        print(f"Ticket from: {self.departure_airport}")
        print(f"Ticket to: {self.arrival_airport}")
        print(f"Departure time: {self.departure_time}")
        print(f"Arrival time: {self.arrival_time}")
        print(f"Price: {self.price}$")


class Order:
    """Order class"""

    def __init__(self):
        self.order_id: int = random.randint(1, 1000000)
        self.ticket_list: list[FlyingTicket] = []

    def get_order_details(self):
        """Get order details"""

        print(f"Order ID: {self.order_id}")
        for ticket in self.ticket_list:
            ticket.get_details()

    def add_ticket(self, ticket: FlyingTicket) -> None:
        """
        Add ticket to order

        Args:
            ticket (FlyingTicket): Ticket class which should be added to order
        """

        self.ticket_list.append(ticket)

    def remove_tickets(self):
        """
        Remove all tickets from order
        """

        self.ticket_list = []


class Payment:
    """
    Payment class

    Attributes:
        order (Order): Order for which is created the payment
    """

    def __init__(self, order: Order):
        self.payment_id: int = random.randint(1, 1000000)
        self.order: Order = order

    def pay_order(self) -> None:
        """Pay order"""

        print("Paying order...")
        if not self.order.ticket_list:
            print("No tickets in the order")

        total_price: int = sum(ticket.price for ticket in self.order.ticket_list)
        print(f"Total price for the order: {total_price}$")

        if total_price > 0:
            print("Order paid")

    def generate_invoice(self) -> None:
        """Generate invoice for payment"""

        print("Generating invoice...")
        print("---Invoice:")
        print(f"Payment ID: {self.payment_id}")
        self.order.get_order_details()
        print("Invoice generated")


def run() -> None:
    """Run whole process"""

    tickets: list[FlyingTicket] = [
        FlyingTicket(
            departure_airport="Prague",
            arrival_airport="Washington",
            departure_time=datetime(
                year=2023,
                month=8,
                day=10,
                hour=10,
            ),
            arrival_time=datetime(
                year=2023,
                month=8,
                day=10,
                hour=22,
            ),
            price=500.30,
        ),
        FlyingTicket(
            departure_airport="Berlin",
            arrival_airport="Paris",
            departure_time=datetime(
                year=2023,
                month=8,
                day=10,
                hour=10,
            ),
            arrival_time=datetime(
                year=2023,
                month=8,
                day=10,
                hour=22,
            ),
            price=400.25,
        ),
        FlyingTicket(
            departure_airport="London",
            arrival_airport="Budapest",
            departure_time=datetime(
                year=2023,
                month=8,
                day=10,
                hour=10,
            ),
            arrival_time=datetime(
                year=2023,
                month=8,
                day=10,
                hour=22,
            ),
            price=350.45,
        ),
    ]

    # Create order
    order: Order = Order()
    # Add tickets into the order
    for ticket in tickets:
        order.add_ticket(ticket)

    # Create payment for order
    payment: Payment = Payment(order)
    payment.pay_order()
    payment.generate_invoice()


if __name__ == "__main__":
    run()

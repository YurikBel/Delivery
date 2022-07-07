from CourierOrder import *
import random
from datetime import datetime


class Repositories:
    def __init__(self, couriers, strategy):
        self.couriers = couriers
        self.orders = []
        self.strategy = strategy

    def AddOrder(self, weight, source, destination):
        while True:
            number = random.randint(1000, 9999)
            numbers = [k.number for k in self.orders]
            if number not in numbers:
                order = Order(number, weight, source, destination)
                self.orders.append(order)
                break

    def AssignCourier(self, order):
        courier = self.strategy.select(self.couriers, order)
        now = datetime.now()
        courier.is_avail = False
        courier.orders.append(order)
        order.start_d_t = now
        order.courier = courier

    def CompleteOrder(self, order):
        now = datetime.now()
        order.end_d_t = now
        order.courier.is_avail = True
        order.courier.coord = order.destination

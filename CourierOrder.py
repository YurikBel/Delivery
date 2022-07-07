

class Courier:
    def __init__(self, name, ph_number, maximal_w):
        self.name = name
        self.ph_number = ph_number
        self.maximal_w = maximal_w
        self.is_avail = True
        self.coord = [56.3287, 44.002]
        self.orders = []

    def __repr__(self):
        return f'{self.name} {self.orders} {self.is_avail} '


class Order:
    def __init__(self, number, weight, source, destination):
        self.number = number
        self.weight = weight
        self.source = source
        self.destination = destination
        self.start_d_t = None
        self.end_d_t = None
        self.courier = None

    def __repr__(self):
        return f'{self.number} {self.weight}'

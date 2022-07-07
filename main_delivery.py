from repository import *
from minimal import *


def fill_orders(repos):
    with open('orders.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        weight, source, destination = line.split()
        source = [float(k) for k in source.split(',')]
        destination = [float(k) for k in destination.split(',')]
        repos.AddOrder(int(weight), source, destination)


def start_order(repos):
    for k in repos.orders:
        if k.courier == None:
            print(k)
    try:
        num = int(input('Введите номер заказа: '))
        order = next((f for f in repos.orders if f.number == num), None)
        repos.AssignCourier(order)
    except ValueError as e:
        print(e)



def outfile(repos):
    with open('complete_orders.txt', 'w') as out:
        out.write('Свободные заказы:\n')
        for k in repos.orders:
            if k.courier == None:
                out.write(f'{str(k.number)}\n')
        out.write('Незавершенные заказы:\n')
        for k in repos.orders:
            if k.courier != None and k.end_d_t == None:
                out.write(f'{str(k.number)}, {k.start_d_t}\n')
        out.write('Завершенные заказы\n')
        for k in repos.orders:
            if k.courier != None and k.end_d_t != None:
                out.write(f'{str(k.number)}, {k.end_d_t}\n')


def main():
    try:
        cour1 = Courier('Иван', 14675, 15)
        cour2 = Courier('Егор', 1465785, 12)
        arr_cour = [cour1, cour2]
        strategy = MinimalDistanceStrategy()
        repos = Repositories(arr_cour, strategy)
        fill_orders(repos)
        start_order(repos)
        start_order(repos)
        print(repos.orders)
        print(repos.couriers)
        repos.CompleteOrder(repos.orders[0])
        print(repos.couriers)
        outfile(repos)
        start_order(repos)
        outfile(repos)
    except ValueError as e:
        print(e)



main()

from abc import ABC, abstractmethod
from geopy.distance import geodesic as GD


class Strategy(ABC):

    @abstractmethod
    def select(self, couriers, order):
        pass


class MinimalDistanceStrategy(Strategy):

    def select(self, couriers, order):
        ind_cour = None
        min_distance = 10**10
        for i in range(len(couriers)):
            local_distance = GD(couriers[0].coord, order.source).km
            if couriers[i].is_avail and couriers[i].maximal_w >= order.weight and local_distance < min_distance:
                    min_distance = local_distance
                    ind_cour = i
        if ind_cour != None:
            return couriers[ind_cour]
        else:
            raise ValueError('Нет подходящего курьера')

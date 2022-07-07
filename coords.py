from geopy.distance import geodesic as GD



# class Coord:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
#
#     def Distanse_to(self, other):

coord = [56.3287, 44.002]
coord2 = [55.45, 37.37]

print(GD(coord, coord2).km)
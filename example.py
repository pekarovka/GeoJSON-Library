"""
Program zahodí body moc vzdálené od středu

(poslední 3 body)
"""
import json
from geojson_lib.GeoJSON import GeoJSON
from geojson_lib.MultiPoint import MultiPoint

MAX_DISTANCE = 1.0  # max vzdálenost od středu
FILE_NAME = "example.geojson"

collection = GeoJSON.loadFromFile(FILE_NAME)
center_point = collection.items[0]
point_cloud = collection.items[1]

filtered_points = []
for i in range(len(point_cloud)):
    if ((center_point.lat - point_cloud.lat(i))**2 \
            + (center_point.lon - point_cloud.lon(i))**2) ** 0.5 <= MAX_DISTANCE:
        filtered_points.append([point_cloud.lat(i), point_cloud.lon(i)])

filtered_point_cloud = MultiPoint(*filtered_points)
collection.items[1] = filtered_point_cloud

print(json.dumps(collection.saveToJsonEntity(), indent=2))

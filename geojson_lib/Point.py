from geojson_lib.Geometry import Geometry


class Point(Geometry):
    def __init__(self, json_entity):
        super(Point, self).__init__(json_entity)

        self.lat = json_entity["coordinates"][0]
        """Point latitude"""

        self.lon = json_entity["coordinates"][1]
        """Point longitude"""

    def getType(self):
        return "Point"

    def saveToJsonEntity(self):
        json_entity = super(Point, self).saveToJsonEntity()
        json_entity["coordinates"] = [self.lat, self.lon]
        return json_entity


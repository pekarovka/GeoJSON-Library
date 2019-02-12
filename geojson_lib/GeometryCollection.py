from geojson_lib.Geometry import Geometry
from geojson_lib.GeoJSON import GeoJSON


class GeometryCollection(Geometry):
    def __init__(self, *items):
        super(GeometryCollection, self).__init__()

        self.items = list(items)

    def getType(self):
        return "GeometryCollection"

    @classmethod
    def loadFromJsonEntity(cls, json_entity):
        return GeometryCollection(*map(lambda x: GeoJSON.loadFromJsonEntity(x), json_entity["geometries"]))

    def saveToJsonEntity(self):
        json_entity = super(GeometryCollection, self).saveToJsonEntity()
        json_entity["geometries"] = list(map(lambda x: x.saveToJsonEntity(), self.items))
        return json_entity


from geojson_lib.Geometry import Geometry
from geojson_lib.GeoJSON import GeoJSON
from geojson_lib.Feature import Feature


class FeatureCollection(GeoJSON):
    def __init__(self, *items):
        super(FeatureCollection, self).__init__()

        self.items = items

    def getType(self):
        return "FeatureCollection"

    @classmethod
    def loadFromJsonEntity(cls, json_entity):
        return FeatureCollection(*map(lambda x: Feature.loadFromJsonEntity(x), json_entity["features"]))

    def saveToJsonEntity(self):
        json_entity = super(FeatureCollection, self).saveToJsonEntity()
        json_entity["features"] = list(map(lambda x: x.saveToJsonEntity(), self.items))
        return json_entity


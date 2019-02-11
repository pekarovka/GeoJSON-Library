from geojson_lib.Geometry import Geometry
from geojson_lib.GeoJSON import GeoJSON


class Feature(Geometry):
    def __init__(self, geometry, properties):
        super(Feature, self).__init__()

        self.geometry = geometry
        self.properties = properties

    def getType(self):
        return "Feature"

    @classmethod
    def loadFromJsonEntity(cls, json_entity):
        return Feature(GeoJSON.loadFromJsonEntity(json_entity["geometry"]), json_entity["properties"])

    def saveToJsonEntity(self):
        json_entity = super(Feature, self).saveToJsonEntity()
        json_entity["geometry"] = self.geometry.saveToJsonEntity()
        json_entity["properties"] = self.properties
        return json_entity


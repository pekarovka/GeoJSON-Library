from geojson_lib.Geometry import Geometry
from geojson_lib.GeoJSON import GeoJSON


class Feature(Geometry):
    def __init__(self, geometry, properties, id=None):
        super(Feature, self).__init__()

        self.geometry = geometry
        self.properties = properties
        self.id = id


    def getType(self):
        return "Feature"

    @classmethod
    def loadFromJsonEntity(cls, json_entity):
        return Feature(GeoJSON.loadFromJsonEntity(json_entity["geometry"]),json_entity["properties"],
            json_entity["id"] if "id" in json_entity else None)

    def saveToJsonEntity(self):
        json_entity = super(Feature, self).saveToJsonEntity()
        json_entity["geometry"] = self.geometry.saveToJsonEntity() if self.geometry is not None else None
        json_entity["properties"] = self.properties

        if self.id is not None:
            json_entity["id"] = self.id

        return json_entity


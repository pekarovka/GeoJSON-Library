import json


class GeoJSON:

    def getType(self):
        """Returns geo json type of the instance."""
        raise Exception("Method must be overridden.")
    
    @classmethod
    def loadFromFile(cls, filename):
        """Loads geo json object from a file."""
        with open(filename, "r", encoding ="utf-8") as f:
            return GeoJSON.loadFromString(f.read())

    @classmethod
    def loadFromString(cls, text):
        """Loads geo json object from a string."""
        json_entity = json.loads(text)
        return GeoJSON.loadFromJsonEntity(json_entity)

    @classmethod
    def loadFromJsonEntity(self, json_entity):
        if json_entity is None:
            return None

        if json_entity["type"] == "Point":
            from geojson_lib.Point import Point
            return Point.loadFromJsonEntity(json_entity)

        elif json_entity["type"] == "MultiPoint":
            from geojson_lib.MultiPoint import MultiPoint
            return MultiPoint.loadFromJsonEntity(json_entity)

        elif json_entity["type"] == "LineString":
            from geojson_lib.LineString import LineString
            return LineString.loadFromJsonEntity(json_entity)

        elif json_entity["type"] == "MultiLineString":
            from geojson_lib.MultiLineString import MultiLineString
            return MultiLineString.loadFromJsonEntity(json_entity)

        elif json_entity["type"] == "Polygon":
            from geojson_lib.Polygon import Polygon
            return Polygon.loadFromJsonEntity(json_entity)

        elif json_entity["type"] == "MultiPolygon":
            from geojson_lib.MultiPolygon import MultiPolygon
            return MultiPolygon.loadFromJsonEntity(json_entity)

        elif json_entity["type"] == "GeometryCollection":
            from geojson_lib.GeometryCollection import GeometryCollection
            return GeometryCollection.loadFromJsonEntity(json_entity)

        elif json_entity["type"] == "Feature":
            from geojson_lib.Feature import Feature
            return Feature.loadFromJsonEntity(json_entity)

        elif json_entity["type"] == "FeatureCollection":
            from geojson_lib.FeatureCollection import FeatureCollection
            return FeatureCollection.loadFromJsonEntity(json_entity)

        raise Exception("Unknown type.")

    def saveToFile(self, filename):
        """Save geo json object to a file."""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.saveToString())

    def saveToString(self):
        return json.dumps(self.saveToJsonEntity())

    def saveToJsonEntity(self):
        return {
            "type": self.getType()
        }

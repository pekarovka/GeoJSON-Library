import json


class GeoJSON:
    def __init__(self, json_entity):
        pass

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

        if json_entity["type"] == "Point":
            from geojson_lib.Point import Point
            return Point(json_entity)

        return GeoJSON(json_entity)

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

import json

class GeoJSON:
    def __init__(self, json_entity):
        self.json_entity = json_entity
    
    @classmethod
    def loadFromFile(cls, filename):
        """Loads geo json object from a file."""
        with open(filename, "r", encoding ="utf-8") as f:
            return GeoJSON.loadFromString(f.read())

    @classmethod
    def loadFromString(cls, text):
        """Loads geo json object from a string."""
        json_entity = json.loads(text)
        return GeoJSON(json_entity)

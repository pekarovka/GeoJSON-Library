import unittest
from geojson_lib.GeoJSON import GeoJSON


class TestFeatureCollection(unittest.TestCase):

    def test_it_saves_to_string(self):
        text = """{"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "Point", "coordinates": [102.0, 0.5]}, "properties": {"foo": 42}}]}"""
        featurecollection = GeoJSON.loadFromString(text)
        savedtext = featurecollection.saveToString()
        self.assertEqual(text, savedtext)


if __name__ == '__main__':
    unittest.main()
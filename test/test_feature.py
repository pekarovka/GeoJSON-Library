import unittest
from geojson_lib.GeoJSON import GeoJSON


class TestFeature(unittest.TestCase):

    def test_it_saves_to_string(self):
        text = """{"type": "Feature", "geometry": {"type": "Point", "coordinates": [102.0, 0.5]}, "properties": {"foo": 42}}"""
        feature = GeoJSON.loadFromString(text)
        savedtext = feature.saveToString()
        self.assertEqual(text, savedtext)


if __name__ == '__main__':
    unittest.main()
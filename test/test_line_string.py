import unittest
from geojson_lib.GeoJSON import GeoJSON


class TestLineString(unittest.TestCase):

    def test_it_saves_to_string(self):
        text = """{"type": "LineString", "coordinates": [[101, 0.6], [102.0, 0.5]]}"""
        linestring = GeoJSON.loadFromString(text)
        savedtext = linestring.saveToString()
        self.assertEqual(text, savedtext)


if __name__ == '__main__':
    unittest.main()

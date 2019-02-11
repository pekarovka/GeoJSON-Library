import unittest
from geojson_lib.GeoJSON import GeoJSON


class TestMultiLineString(unittest.TestCase):

    def test_it_saves_to_string(self):
        text = """{"type": "MultiLineString", "coordinates": [[[101, 0.6], [102.0, 0.5]], [[101, 0.6], [102.0, 0.5]]]}"""
        multilinestring = GeoJSON.loadFromString(text)
        savedtext = multilinestring.saveToString()
        self.assertEqual(text, savedtext)


if __name__ == '__main__':
    unittest.main()
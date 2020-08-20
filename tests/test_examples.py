"""
Общиие тест-кейсы из:
Методические рекомендации по работе со СМЭВ версия 3.5.0.1
"""
# pylint: disable=C0116,C0115,C0114
import json
import unittest

from gost_xml_transform import GOSTXMLTransform


class XMLTest(unittest.TestCase):
    def setUp(self) -> None:
        with open('tests/data.json', 'r') as fp:
            self.data = json.load(fp)

    def test_all(self):
        for (in_, output) in self.data:
            transformer = GOSTXMLTransform.from_string(in_)
            self.assertEqual(
                transformer.to_bytes().decode('utf-8'),
                output
            )


if __name__ == '__main__':
    unittest.main()

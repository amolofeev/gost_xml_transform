"""
Общиие тест-кейсы из:
Методические рекомендации по работе со СМЭВ версия 3.5.0.1
"""
import json
import unittest
from unittest import TestCase
from gost_xml_transform import GOSTXMLTransform


class XMLTest(TestCase):
    def setUp(self) -> None:
        with open('tests/data.json', 'r') as fp:
            self.data = json.load(fp)

    def test_all(self):
        for (input, output) in self.data:
            transformer = GOSTXMLTransform.from_string(input)
            self.assertEqual(
                transformer.to_bytes().decode('utf-8'),
                output
            )


if __name__ == '__main__':
    unittest.main()

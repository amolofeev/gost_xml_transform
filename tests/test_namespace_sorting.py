"""
Тест-кейсы для проверки правил:
25. Атрибуты должны быть отсортированы в алфавитном порядке:
    сначала по namespace URI (если атрибут - в qualified form), затем – по local name.
    Атрибуты в unqualified form после сортировки идут после атрибутов в qualified form.
26. Объявления namespace prefix должны находиться перед атрибутами.
    Объявления префиксов должны быть отсортированы в порядке объявления, а именно:
    a. Первым объявляется префикс пространства имён элемента,
       если он не был объявлен выше по дереву.
    b. Дальше объявляются префиксы пространств имён атрибутов, если они требуются.
       Порядок этих объявлений соответствует порядку атрибутов,
       отсортированных в алфавитном порядке (см. п.25 текущего перечня).
"""
# pylint: disable=C0116,C0115,C0114
import unittest

from gost_xml_transform import GOSTXMLTransform


class XMLTest(unittest.TestCase):
    def test_unqualified_attribute_sorting(self):
        self.assertEqual(
            '<tag a="1" b="1" c="1"></tag>',
            GOSTXMLTransform.from_string(
                '<tag c="1" b="1" a="1"/>'
            ).to_bytes().decode('utf-8')
        )

    def test_qualified_attribute_sorting_with_the_same_namespace(self):
        self.assertEqual(
            '<ns1:tag xmlns:ns1="urn://x" ns1:a="1" ns1:b="1" ns1:c="1"></ns1:tag>',
            GOSTXMLTransform.from_string(
                '<m:tag xmlns:m="urn://x" m:c="1" m:b="1" m:a="1"/>'
            ).to_bytes().decode('utf-8')
        )

    def test_namespace_sorting_26_ab(self):
        self.assertEqual(
            '<ns1:tag xmlns:ns1="urn://x" xmlns:ns2="urn://x1" ns2:a="1" ns2:b="1" ns2:c="1">'
            '</ns1:tag>',
            GOSTXMLTransform.from_string(
                '<m:tag xmlns:m="urn://x" xmlns:m1="urn://x1" m1:c="1" m1:b="1" m1:a="1"/>'
            ).to_bytes().decode('utf-8')
        )

    def test_qualified_attribute_sorting_with_different_namespace(self):
        self.assertEqual(
            '<ns1:tag '
            'xmlns:ns1="urn://1" xmlns:ns2="urn://2" xmlns:ns3="urn://3" xmlns:ns4="urn://4" '
            'ns2:b="1" ns3:c="1" ns4:a="1"></ns1:tag>',
            GOSTXMLTransform.from_string(
                '<m1:tag xmlns:m4="urn://4" xmlns:m3="urn://3" xmlns:m2="urn://2" '
                'xmlns:m1="urn://1" m3:c="1" m2:b="1" m4:a="1"/>'
            ).to_bytes().decode('utf-8')
        )

    def test_qualified_attribute_sorting_with_different_namespace_and_names(self):
        self.assertEqual(
            '<ns1:tag xmlns:ns1="urn://1" xmlns:ns2="urn://2" xmlns:ns3="urn://3" '
            'xmlns:ns4="urn://4" ns2:a="1" ns2:b="1" '
            'ns2:c="1" ns3:a="1" ns3:b="1" ns3:c="1" ns4:a="1" ns4:b="1" ns4:c="1"></ns1:tag>',
            GOSTXMLTransform.from_string(
                '<m1:tag xmlns:m4="urn://4" xmlns:m3="urn://3" xmlns:m2="urn://2" '
                'xmlns:m1="urn://1" m3:c="1" m3:b="1" m3:a="1" m2:c="1" '
                'm2:b="1" m2:a="1" m4:c="1" m4:b="1" m4:a="1" />'
            ).to_bytes().decode('utf-8')
        )


if __name__ == '__main__':
    unittest.main()

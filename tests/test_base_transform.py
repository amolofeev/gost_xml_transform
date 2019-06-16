"""
тест-кейсы для поверики следующих правил:
- После применения правил из пунктов 1 и 20, если даже у элемента нет дочерних узлов,
  элемент не может быть представлен в виде empty element tag
  (http://www.w3.org/TR/2008/REC-xml-20081126/#sec-starttags, правило [44]),
  а должен быть преобразован в пару start-tag + end-tag.
- Если текстовый узел содержит только пробельные символы
  (код символа меньше или равен '\u0020'), этот текстовый узел вырезается.
- Удалить namespace prefix, которые на текущем уровне объявляются, но не используются.
- Проверить, что namespace текущего элемента объявлен либо выше по дереву, либо в текущем элементе.
  Если не объявлен, объявить в текущем элементе.
- Namespace prefix элементов и атрибутов должны быть заменены на автоматически сгенерированные.
  Сгенерированный префикс состоит из литерала «ns», и порядкового номера сгенерированного префикса
  в рамках обрабатываемого XML-фрагмента, начиная с единицы.
  При генерации префиксов должно устраняться их дублирование.
"""
import unittest
from unittest import TestCase
from gost_xml_transform import GOSTXMLTransform


class TestBase(TestCase):
    def test_self_close_tag(self):
        self.assertEqual(
            '<tag></tag>',
            GOSTXMLTransform.from_string("<tag/>").to_bytes().decode('utf-8')
        )

    def test_rm_empty_text(self):
        self.assertEqual(
            '<tag></tag>',
            GOSTXMLTransform.from_string("<tag>        </tag>").to_bytes().decode('utf-8')
        )

    def test_pass_text(self):
        self.assertEqual(
            '<tag>  text  </tag>',
            GOSTXMLTransform.from_string("<tag>  text  </tag>").to_bytes().decode('utf-8')
        )

    def test_rm_unused_namespace(self):
        self.assertEqual(
            '<tag></tag>',
            GOSTXMLTransform.from_string('<tag  xmlns:myns="urn://x" />').to_bytes().decode('utf-8')
        )

    def test_rename_namespace(self):
        self.assertEqual(
            '<ns1:tag xmlns:ns1="urn://x"></ns1:tag>',
            GOSTXMLTransform.from_string('<myns:tag xmlns:myns="urn://x" />').to_bytes().decode('utf-8')
        )

    def test_children_namespace(self):
        self.assertEqual(
            '<ns1:tag xmlns:ns1="urn://x"><ns2:tag2 xmlns:ns2="urn://x1"></ns2:tag2></ns1:tag>',
            GOSTXMLTransform.from_string(
                '<myns:tag xmlns:myns="urn://x"  xmlns:myns2="urn://x1">'
                '<myns2:tag2/>'
                '</myns:tag>'
            ).to_bytes().decode('utf-8')
        )

    def test_children_namespace_2(self):
        self.assertEqual(
            '<ns1:tag xmlns:ns1="urn://x">'
            '<ns2:tag2 xmlns:ns2="urn://x1"></ns2:tag2>'
            '<ns3:tag2 xmlns:ns3="urn://x1">'
            '</ns3:tag2></ns1:tag>',

            GOSTXMLTransform.from_string(
                '<myns:tag xmlns:myns="urn://x"  xmlns:myns2="urn://x1">'
                '<myns2:tag2/>'
                '<myns2:tag2/>'
                '</myns:tag>'
            ).to_bytes().decode('utf-8')
        )


if __name__ == '__main__':
    unittest.main()

**GOST XML transformation for SMEV 3**

Python impelemtation of `urn://smev-gov-ru/xmldsig/transform` in according to documentation [v3.5.0.1](https://smev3.gosuslugi.ru/portal/)


```python
from gost_xml_transform import GOSTXMLTransform

transformer = GOSTXMLTransform.from_string('<tag />', encoding='utf-8')
# transformer = GOSTXMLTransform.from_bytes(b'<tag />')
# transformer = GOSTXMLTransform(etree.Element) # not recommended
result = transformer.to_bytes()
do_smth(result)
```

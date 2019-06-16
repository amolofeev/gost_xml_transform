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


**Warning!**

Sorting algorithm of ns prefix could be wrong. 

To be sure that's right we must contact to SMEV 3 support team and ask them to provide correct output for input like that

```xml
<m1:tag 
    xmlns:m4="urn://4"  xmlns:m3="urn://3" 
    xmlns:m2="urn://2" xmlns:m1="urn://1" 
    m3:c="1" m3:b="1" m3:a="1" 
    m2:c="1" m2:b="1" m2:a="1" 
    m4:c="1" m4:b="1" m4:a="1" 
/>
```

Currently sorting algorithm has implemented in according to p.25 of documentation.
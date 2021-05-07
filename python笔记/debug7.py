import re

text = 'asdklnasfjn:Sdf,sl;,;aa={a:123,b:123},sdmiunnws'
print(re.findall(r'aa=({.*?}),sd', text))
print(re.findall(r'aa=(.*?),sd', text))
text2 = '03-15<br>04:05a<22'
print(re.findall(r'(.*)<br>(.*)<22', text2))

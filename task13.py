1)
import re
str="aeeb and4 afgh3 ammb 45 6"
res=re.findall(r'\w\w*\w',str)
print(res)

2)
import re
str="aeeb and afgh amb"
res=re.match(r'a\w*b',str)
print(res.group( ))

3)
import re
str="excercises number456 and345 important"
res=re.findall(r'\w*[0-9]',str)
print(res)

4)
import re
str='excercises number 1 12 134 456 678 and 34 important'
res=re.findall(r'[0-9]{1,3}',str)
print(res)


5)
import re
str="APP and ball CAT and dog"
res=re.match(r'\w[A-Z]\w',str)
print(res.group( ))
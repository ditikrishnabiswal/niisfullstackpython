import re  

result = re.match(r'\D+','xyzab56c')
print(result.group())
#split
import re  

result = re.split(r'\d+','abc123def456')
print(result)        


import re  

result = re.sub(r'\D+','x','abc123def456')
print(result)
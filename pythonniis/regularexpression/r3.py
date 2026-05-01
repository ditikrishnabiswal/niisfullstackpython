#search
import re  

result = re.search(r'\D+','abc123de56f')
print(result.group())
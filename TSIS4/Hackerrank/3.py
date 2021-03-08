import re
m = re.findall(r"(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]", input(), flags = re.I)
print('\n'.join(m or ['-1']))
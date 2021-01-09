import re
PATTERN =  r'([+-][\d]{0,}[\.?[\d]{0,}]{0,}[*]?[a-zA-Z]?)'
# PATTERN = r'([+-][\d]{0,}[*]?[a-zA-Z]?)'
x = '+12312.0'
y = '+3.212312x+2.123123x+12x+151+y+7'
print(bool(re.fullmatch(r'([-+]?\d+.\d+)',x)))
print(re.findall(PATTERN, y))
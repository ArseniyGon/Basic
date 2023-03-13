import re

s = 'geeks.forgeeks'

# without using \
match = re.search(r'venv', s)
print(match)

# using \
match = re.search(r'venv', s)
print(match)
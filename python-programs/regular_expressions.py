import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
'''

pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)

for match in matches :
    print(match)

print(text_to_search[1:4])
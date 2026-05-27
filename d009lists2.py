languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']

if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)  # ['Python', 'SQL', 'C++', 'JavaScript']

languages.pop()
temp = languages.pop(1)
print(temp)       # SQL
print(languages)

languages.append(temp)
print(languages)  # ['Python', 'C++', 'SQL']

languages.clear()
print(languages)  # []
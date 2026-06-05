languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']

if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)  # ['Python', 'SQL', 'C++', 'JavaScript']

languages.pop()
print(languages)  # ['Python', 'SQL', 'C++']
#languages.pop('C++') TypeError: 'str' object cannot be interpreted as an integer
temp = languages.pop(1)
print(temp)       # SQL
print(languages)

languages.append(temp)
print(languages)  # ['Python', 'C++', 'SQL']

languages.clear()
print(languages)  # []

languages2 = ['Python', 'SQL', 'Python','Java', 'C++', 'JavaScript']
languages2.remove('Python')
print(languages2)  # ['SQL', 'Python', 'Java', 'C++', 'JavaScript']
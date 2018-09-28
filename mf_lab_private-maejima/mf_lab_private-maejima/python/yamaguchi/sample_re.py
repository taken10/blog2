import re

# match
fruits = 'apple banana apple cherry'
result_match_1 = re.match('apple', fruits)
print(result_match_1)  # <_sre.SRE_Match object; span=(0, 5), match='apple'>
result_match_2 = re.match('a[a-z]+e', fruits)
print(result_match_2)  # <_sre.SRE_Match object; span=(0, 5), match='apple'>
# matchオブジェクト
print(result_match_1.group())  # apple
print(result_match_1.start())  # 0
print(result_match_1.end())  # 5
print(result_match_1.span())  # (0, 5)
# matchしない
result_match_3 = re.match('banana', fruits)
print(result_match_3)  # None

# search
result_search_1 = re.search('apple', fruits)
print(result_search_1)  # <_sre.SRE_Match object; span=(0, 5), match='apple'>
result_search_2 = re.search('ba[a-z]+na', fruits)
print(result_search_2)  # <_sre.SRE_Match object; span=(6, 12), match='banana'>

# findall
result_findall_1 = re.findall('apple', fruits)
print(result_findall_1)  # ['apple', 'apple']
result_findall_2 = re.findall(r'a[a-z]+e\s*[a-z]+rry', fruits)
print(result_findall_2)  # ['apple cherry']

# finditer
result_finditer_1 = re.finditer('apple', fruits)
print(result_finditer_1)  # <callable_iterator object at 0x028F3650>
for matchObj in result_finditer_1:
    print(matchObj)
# <_sre.SRE_Match object; span=(0, 5), match='apple'>
# <_sre.SRE_Match object; span=(13, 18), match='apple'>

# sub
result_sub = re.sub('^a[a-z]+e', 'APPLE', fruits)
print(result_sub) # APPLE banana apple cherry
# ()で囲う
result_sub_2 = re.sub('(apple) (banana)', '\\1AND\\2', fruits)
print(result_sub_2)  # appleANDbanana apple cherry

# split
result_split = re.split(' ', fruits)
print(result_split)  # ['apple', 'banana', 'apple', 'cherry']

# compile
pattern = re.compile('apple')
result_compile_1 = pattern.match(fruits)
print(result_compile_1)  # <_sre.SRE_Match object; span=(0, 5), match='apple'>
result_compile_2 = pattern.findall(fruits)
print(result_compile_2)  # ['apple', 'apple']
result_compile_3 = pattern.sub('APPLE', fruits)
print(result_compile_3)  # APPLE banana APPLE cherry

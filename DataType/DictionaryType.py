# key - value 자료형. Java의 Map과 흡사하구만

dic = {'name': 'Yoon', 'age': 20, 'phone': '010-1234-1234'}

# 사용하기
print(dic['name'])
print(dic.get('name'))
# print(dic['school']) #에러 KeyError: 'school'
print(dic.get('school')) #None
print(dic.get('school', '학교정보 없음')) #학교정보 없음

# 추가하기
dic['address'] = '대한민국'
print(dic)

# 수정하기
dic['name'] = 'Kim'
print(dic['name'])
print(dic)

# 삭제하기
del dic['address']
print(dic)

# 키 리스트
keys = dic.keys()
print(keys) #dict_keys(['name', 'age', 'phone'])
print(list(keys)) #['name', 'age', 'phone']

# 키 순회
for key in dic.keys():
    print(key)

# 값 리스트
values = dic.values()
print(values) #dict_values(['Kim', 20, '010-1234-1234'])
print(list(values)) #['Kim', 20, '010-1234-1234']

# 키 체크
print('name' in dic) #True
print('school' in dic) #False

# 리스트는 key로 쓸 수 없지만, 튜플은 키로 쓸 수 있다!
dic2 = {(1, 2): '일 콤마 이', 1: '일'}
print(dic2[(1, 2)])

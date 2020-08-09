# 使用get()的简单数据库
people={
    'lgh':{
        'phone':13387212527,
        'address':"将军山村一组"
    },
    'wme':{
        'phone':13387212528,
        'address':"将军山村一组01"
    },
    'xxx':{
        'phone':13387212529,
        'address':"将军山村一组02"
    }
}

labels={
    'phone':'phone number',
    'address':'address'
}
name=input('name: ')
# 查找电话号码还是地址
request=input('phone number (p) or address (a) ?')
# 使用正确的键
key=request
if request=='p':
    key='phone'
if request=='a':
    key='address'

# 使用get()提供默认值
person=people.get(name,{})
label=labels.get(key,key)
result=person.get(key,"not available")

print("{0}'s {1} is {2}".format(name,label,result))
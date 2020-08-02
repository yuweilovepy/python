# a="hello python13"
# print(len(a))
# # type 判断字符串类型
# # print(type(a))
# # 列表和元组
# #索引
# #分片
# numbers=[1,2,3,4,5]
# print(numbers[:])
# print(numbers[:-1])
# #步长 序列相加  序列相乘
# #  成员资格  in  条件为真或者假
# database=[
#     ['albert','1234'],
#     ['dilbert','4242'],
#     ['smith','9843'],
#     ['jones','7524']
# ]
# username=input("User name:")
# pin=input("PIN code:")
# if [username,pin] in database:
#     print("Access granted")
# else:
#     print("Error")
# print(type([username,pin])) # 肯定是列表了 列表是可变的 有许多方法
# 长度 最小值 最大值 len() max() min()
# # list函数
# print(list("hello")) # 根据字符串创建列表
# # 基本的列表操作
# #改变列表 元素赋值
# # 使用索引进行改变
# x=[1,2,3]
# x[1]=100
# print(x)
# #  删除列表  del 语句实现
# names=["lgh",'wme','xxx']
# del names[1]
# print(names)
#
# # 分片赋值
# yu_yan='java'
# yu_yan_list=list(yu_yan)
# print(yu_yan_list)

#  列表方法
# append count extend index insert pop remove reverse sort
# lst=[1,2,3,4]
# lst.append("lgh_xxx")  #  不是返回一个修改过得新列表 而是直接修改原来的列表
# print(lst)
# # count 统计某个元素在列表中出现的次数
# # extend  末尾一次性追加
# a=[1,2,3,4,5]
# b=[5,6,7,8,9]
# a.extend(b)
# print(a) # a 的值已近该改变了
# print(a+b)
# # index 方法 用于从列表中找出某一个值第一个匹配项的索引位置
# print(a.index(9))
# print(a.index(6))
# print(a.index(5))
# #  ok
# # insert 用于将对象插入到列表中  #  我就说么
# a.insert(1,"lgh_love_wme")
# print(a)
#
# #pop 方法会移除列表中侧一个元素 并且会返回该元素的值
# a.pop()
# print(a)
# # remove 会移除列表中第一个匹配项
# a.remove(5)
# a.remove(5)
# print(a)
# #   reverse 将列表中的元素反向存放
# a.reverse()
# print(a)
# #sort 用于原位置在列表排序
# a.remove("lgh_love_wme")
# print(a)
# a.sort()
# print(a)
# num=[4,5,6,7,8,955,4,22]
#
# num.sort()
#   字符串
#  字符串格式化 一般使用元组
# 字符串方法
# find  可以在较长的字符串中查找子串 最左端索引
# str="ip-01 ip-02 ip-03"
# print(str.find("ip-02"))
#
# # join 方法 非常虫重要的字符串方法
# seq=['1','2','3']
# print("---".join(seq))
# str2="1,2,3,4,5,6"
# print(str2.split(','))  #  根据什么分割

# lower 返回字符串的小写字母
#
# # replace
from pprint import pprint
# pprint("ke ke is a fuck".replace('ke','fuck'))
#
# # split 将字符串分割为 序列
# # strip 方法  返回    去除两侧空格的字符串  return
# a='  ppp ppp  ppp  '
# b=a.strip()
# pprint(b)

# 字典 {} 空字典
# 创建和使用字典
# phone_book={'lgh':123,'wme':456,'lr':789}
# # dict 函数
items=[('name','lgh'),('age',28)]
d=dict(items)  # 用dict 创建字典
pprint(d)
#
# # dict 函数可以通过关键字来创建字典
# pprint(dict(name='lgh',age=28))

# 基本字典操作
print(len(d)) # 键值对的数量
pprint(d['name']) # 通过键查找值
d["sex"]='男' # 赋值
pprint(d)
# del d[k]  删除键为k的项
del d['sex']
print(d)
# k in d  检查d中是否含有k的项






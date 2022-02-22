#1 变量交换
a, b = b, a

#2 字符串格式化
"my name is {}, my age is {}".format(name, age)
f"my name is {name}, my age is {age}"

#3 yield语法，使用yield的优势在于：不用等整个函数计算完成之后才输出，而是在计算过程中就可以输出。
def func():
    res = []
    for i in range(10):
        res.append(i)
    return res

res = func()
for i in res:
    print(i)
    
#等价于

def func():
    for i in range(10):
        yield i

for i in func():
    print(i)
    
#4 列表解析式
fruit = ['apple', 'banana', 'orange', 'pear']
fruit = [x.upper() for x in fruit]

#5 解包,也叫unpacking
a = {'ross':'123', 'bob':'456'}
b = {'lile':'111', 'zab':'789'}
c = {**a, **b} #相当于通过**分别将a字典和b字典中的内容写到新的字典，完成字典的合并

#6 三元运算符
s = 'pass' if score > 60 else 'fail'

#7 with语句
f = open('train.txt', 'r')
s = f.read()
f.close()

#等价于

with open('train.txt', 'r'):
    s = f.read() #执行完之后会自动的关闭
    
#8 重复元素判定
len(lst) == len(set(lst))

#9 字符元素组成判定
from collections import Counter
Counter(str1) == Counter(str2)

#10 内存占用
import sys
sys.getsizeof(var)

#11 字节占用
len(str1.encode('utf-8'))

#12 打印n次字符
print('-'*n)

#13 大写第一个字母
str1.title()

#14 首字母小写
str1[:1].lower() + str1[1:]

#15 解包
#将打包好的成对列表解开为两组不同的元组
array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
zip(*array) # 返回 [('a', 'c', 'e'), ('b', 'd', 'f')]

#16 链式对比
2 < a < 5

#17 zip打包可迭代对象
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for i, j in zip(nums1, nums2):
    print(i, j)
    
#18 divmod同时进行除法和取余
m, n = divmod(233, 2) #n为余数

#19 拒绝手动拼接路径
from pathlib import Path
root = Path('Dir')
path = root/'train.csv'

#20 海象运算符：保留if条件判断中的结果。
c = a-b
if c < 0:
    print(c)

#等价于

if (c := a-b) < 0: 
    print(c)
    
#21 默认字典
d = defaultdict(int)
d[1] += 1 #即d[1] = 1

#22 product 
from itertools import product 
for x, y, z in product(lst1, lst2, lst3):
    print(x, y, z)

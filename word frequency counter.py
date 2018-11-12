import operator

str = '1!2@q#s$%7hfgu483abce75921hfwur99'

def creat_word_list(str):
 word_list = []      #定义一个空列表
 for word in str:    #将str中的每个字符添加到word_list中
  word_list.append(word)
 print(word_list)
 creat_clean_word_list(word_list)
 
def creat_clean_word_list(word_list):
#清除列表中的!@#$%
 clean_word_list = []  
 symbols = '!@#$%'      #需要清除的元素
 for word in word_list:   #对于列表中的每一个元素word
  for i in range(len(symbols)):   #依次与symbols中的每个字符相比较
   word = word.replace(symbols[i],'') #如果与symbols中的某一项相同，则用''替换该word
  if len(word)>0:                       #如果该word的长度大于0
   clean_word_list.append(word)           #则将该word，添加到clean_word_list中
 print (clean_word_list)
 creat_dictionary(clean_word_list)

'''
  字典是一种可变容器模型，且可存储任意类型对象
  字典中的每一个键值key=>value对用冒号':'分割，每个键值对之间用逗号','分割
整个字典包括在{}中，格式如下：     d = {key1 : value1, key2 : value2}
  键一般是唯一的，如果重复最后一个的键值会替换前面的，值不需要唯一
  dict = {'a':1, 'b':2, 'b':'c'} >>> {'a':1,'b':'c'}  
  值可以取任何数据类型，但键必须是不变的
''' 

def creat_dictionary(clean_word_list):
 word_count = {}
 for word in clean_word_list:
  if word in word_count:
   word_count[word] += 1
   '''
   访问字典里的值：把相应的键放入[]
   如：dict = {'Name':'Herry','Age':21,'Class':3}
       print(dict['Name'] >>>'Herry'
	   for key,value in dict.items():
	    pritn(key,value)
	>>>Name Herry
	   Class 3
	   Age 21
	  修改键值：
	   dict['Age']=88  >>>dict = {'Name':'Herry','Age':88,'Class':3}
   '''
  else:
   word_count[word] = 1
 for key,value in sorted(word_count.items(),key=operator.itemgetter(1)):
 #sorted()函数对所有可迭代的对象进行排序操作
 #operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号（即需要获取的数据在对象中的序号）
 #word_count{}中包含了key（如'1','a')、value(每个字母出现的次数）两类
 #当key=operator.itemgetter(0)时，按key排序，当为1时按照value的值从小到大排序，即按照出现次数升序输出
 #输入其他数字会报错：IndexError: tuple index out of range
  print(key,value)
 
 
creat_word_list(str)

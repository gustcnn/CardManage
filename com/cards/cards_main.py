#--*--coding:utf-8
#Author:cnn
import sys
from com.cards.cards_tools import *
#欢迎
print("名片管理系统".center(46,"*"))
str_1="1、新建名片"
str_2="2、操作名片"
str_3="3、查询名片"
print(str_1)
print(str_2)
print(str_3)
print("*"*50)


#1,2,3针对名片的操作
#0退出系统
#输入其它,提示输入错误
    # 输入操作
action_str = input("请选择您希望执行的操作:")
print("您选择的操作是【%s】" % action_str)
action = int(action_str)
if action==0:
    print("退出系统")
    sys.exit(1)
elif action==1:
    #print(str_1)
    create_card()
    write_file()
elif action==2:
    print(str_2)
elif action==3:
    print(str_3)
else:
    print("输入错误")



# --*--coding:utf-8
# Author:cnn
import json
import os
card_dict = {}
card_list = []


# 新建名片
def create_card():
    card_name = input("请输入姓名:")
    card_qq = input("请输入qq:")
    card_phone = input("请输入电话:")
    card_email = input("请输入邮箱:")
    card_dict["name"] = card_name
    card_dict["qq"] = card_qq
    card_dict["phone"] = card_phone
    card_dict["email"] = card_email
    #card_list.append(card_dict)
    #write_file()


# 写名片到test.json文件
def write_file():
    # with open("D:/python/script/CardManage/files/file.txt","a") as f:
    #     f.write(str(card_dict)+"\n")
    # "a"追加到test.json文件
    # with open("test.json", "a", encoding="utf8") as f:
    #     # 格式化输出到test.json文件
    #     f.write(json.dumps(card_dict)+"\n")
    with open("D:/python/script/CardManage/files/file.txt", "a", encoding="utf8") as f:
        # 格式化输出到test.json文件
        f.write(json.dumps(card_dict)+"\n")
# 查询名片
def search_card():
    search_name = input("请输入姓名:")
    dict_read=read_file()
    for key in dict_read:
        if dict_read[key]==search_name:
            print("找到了%s"%search_name)
            print(dict_read)
            break
    else:
        print("您要查找的人不存在")

def read_file():
    with open(os.path.abspath(os.path.join(os.getcwd(), "../.."))+"\\files\\file.txt","r",encoding="utf8") as f:
        dict_loads=json.loads(f.read())
    #print(dict_loads)
    return dict_loads

if __name__ == "__main__":
    #create_card()
    # print(card_dict)
    # print(card_list)
    #write_file()
    read_file()
    #获得当前文件所在目录
    print(os.path.abspath(os.path.dirname(__file__)))
    #获得当前文件所在上级目录
    print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    #获得当前文件所在目录上上级目录
    #print(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    print(os.path.abspath(os.path.join(os.getcwd(), "../..")))

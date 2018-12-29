#--*--coding:utf-8
#Author:cnn
card_dict={}
card_list=[]
def create_card():
    card_name=input("请输入姓名:")
    card_qq=input("请输入qq:")
    card_phone=input("请输入电话:")
    card_email=input("请输入邮箱:")
    card_dict["name"]=card_name
    card_dict["qq"]=card_qq
    card_dict["phone"]=card_phone
    card_dict["email"]=card_email
    card_list.append(card_dict)
def write_file():
    with open("D:/python/script/CardManage/files/file.txt","a") as f:
        f.write(str(card_dict)+"\n")
# if __name__=="__main__":
#     create_card()
#     print(card_dict)
#     print(card_list)
#     write_file()
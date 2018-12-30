# --*--coding:utf-8
# Author:cnn
import json

"""名片类"""


class Card:
    card_list = []  # 名片列表用来记录所有名片的
    def create_card(self):
        """新增名片"""
        print("-" * 50)
        print("新增名片")
        card_dict = {}  # 名片字典,用来记录每张名片信息
        name_str = input("请输入姓名:")
        qq_str = input("请输入qq:")
        phone_str = input("请输入电话:")
        email_str = input("请输入邮箱:")
        card_dict["name"] = name_str
        card_dict["qq"] = qq_str
        card_dict["phone"] = phone_str
        card_dict["email"] = email_str
        self.card_list.append(card_dict)
        print("添加%s的名片成功！"%name_str)

    """将card_list写入本地文件"""

    def write_file(self):
        with open("card.json", "w+", encoding="utf8") as f:
            f.write(json.dumps(self.card_list))

    def read_file(self):
        list_read = []
        #必须是.json文件
        with open("card.json", "r", encoding="utf8") as f:
            line_read=json.loads(f.readline())
        #print(type(line_read))
        #print(line_read)
        return line_read

    def show_all_cards(self):
        """显示所有名片"""
        print("-" * 50)
        print("显示所有名片")
        card_json_read=self.read_file()
        if len(card_json_read) == 0:
            print("没有数据")
        else:
            #print(card_json_read)
            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t" * 4)
            print()
            for card_dic in card_json_read:
                for key in card_dic:
                    print(card_dic[key],end="\t"*4)
                print()
            print()

    def search_card(self):
        """搜索名片"""
        print("-" * 50)
        print("搜索名片")
        search_list=self.read_file()
        #print(search_list)
        #print(type(search_list))
        if len(search_list)==0:
            print("没有数据")
        else:
            name_str = input("请输入名字:")
            for dic_str in search_list:
                for key in dic_str:
                    if dic_str[key]==name_str:
                        # print("找到了%s" % name_str)
                        for title_name in ["姓名", "电话", "QQ", "邮箱"]:
                            print(title_name, end="\t" * 4)
                        print()
                        for k in dic_str:
                            print(dic_str[k], end="\t" * 4)
                        print()
                        print("找到了%s" % name_str)
                    break




# if __name__ == "__main__":
#     card = Card()
#     count = 0
#     while True:
#         card.create_card()
#         count += 1
#         if count == 2:
#             break
#     print(card.card_list)
#     card.write_file()
#     card.show_all_cards()
    # print(card.card_list)
    #card.search_card()


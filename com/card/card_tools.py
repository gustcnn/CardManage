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
        with open("card.json", "a", encoding="utf8") as f:
            f.write(json.dumps(self.card_list))

    def read_file(self):
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
        #card_json_read=self.read_file()
        if len(self.card_list) == 0:
            print("没有数据")
        else:
            #print(card_json_read)
            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t" * 4)
            print()
            for card_dic in self.card_list:
                for key in card_dic:
                    print(card_dic[key],end="\t"*4)
                print()
            print()

    def search_card(self):
        """搜索名片"""
        print("-" * 50)
        print("搜索名片")
        #search_list=self.read_file()
        search_list=self.card_list
        if len(self.card_list)==0:
            print("没有数据")
        else:
            name = input("请输入名字:")
            for dic in search_list:
                for key in dic:
                    if dic[key]==name:
                        print("找到了%s"%name)
                        for title_name in ["姓名","电话","QQ","邮箱"]:
                            print(title_name,end="\t"*4)
                        print()
                        for k in dic:
                            print(dic[k],end="\t"*4)
                        print()
                        break
                else:
                    print("没有找到%s"%name)
                    break
                    #break
        # for key in self.card_dict:
        #     if self.card_dict[key] == name:
        #         print("找到了%s" % name)
        #         break
        # else:
        #     print("没有找到%s" % name)


if __name__ == "__main__":
    card = Card()
    # count = 0
    # while True:
    #     card.create_card()
    #     count += 1
    #     if count == 2:
    #         break
    # #print(card.card_list)
    # card.write_file()
    card.show_all_cards()
    # print(card.card_list)


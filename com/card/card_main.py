# --*--coding:utf-8
# Author:cnn
import sys
from com.card.card_tools import Card
#from com.card.card_tool import Card


class CardMain:
    _str_1 = "1.新建名片"  # 定义私有变量
    _str_2 = "2.显示全部"
    _str_3 = "3.查询名片"

    # TODO(cnn) 显示欢迎信息和功能菜单
    def show_menu(self):
        print("名片管理系统".center(46, "*"))
        print("欢迎使用【名片管理系统】V1.0")
        print(self._str_1)
        print(self._str_2)
        print(self._str_3)
        print()
        print("0.退出系统")
        print("*" * 50)

    # TODO(cnn) 选择功能菜单
    def select_menu(self):
        """
        选择菜单
        :return:
        """
        card=Card()#创建名片对象
        while True:
            action_str = input("请选择您希望执行的操作:")
            print("您选择的操作是【%s】" % action_str)
            if action_str in ["1", "2", "3"]:
                if action_str == "1":
                    print(self._str_1)
                    card.create_card()
                    card.write_file()
                elif action_str == "2":
                    print(self._str_2)
                    # pass
                    card.show_all_cards()
                elif action_str == "3":
                    print(self._str_3)
                    card.search_card()
            elif action_str == "0":
                print("退出系统")
                sys.exit(1)
            else:
                print("输入错误,请重新输入")


if __name__ == "__main__":
    card = CardMain()
    card.show_menu()
    card.select_menu()

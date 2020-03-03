# Created by LiuMinXuan 2020/3/3 12:42 
# --coding:utf-8--

product_list = [
    ["Iphone", 5800],
    ["Mac Pro", 9800],
    ["bike", 800],
    ["watch", 10600],
    ["coffee", 31],
    ["Alex Python", 20]
]
# for i in product_list:
#   print(i)

# 创建购物列表
shopping_list = []
# 要求用户输入数据
salary = input("Input your salary:")
# 首先要对用户的输入做判断
if salary.isdigit():
    salary = int(salary)  # 转换为整形
    while True:  # 循环输出列表
        for index, item in enumerate(product_list):
            print(index, item)
        user_choice = input("请选择要买什么......")
        if user_choice.isdigit():  # 转换为整形
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:  # 钱够
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" % (p_item, salary))
                else:  # 钱不够
                    print("\033[41;1m您的余额只剩【%s】，余额不足\033[0m" % salary)
            else:
                print("\033[32;1mProduct code [%s]is not exist\033[0m " % user_choice)
        elif user_choice == "q":

            print("----------shoppig list--------")
            for p in shopping_list:
                print(p)
            print("------------------------------")
            print("\033[33;1mYour current balance is :\033[0m", salary)
            exit()
        else:
            print("Invalid Option")
else:  # 输入q退出
    print("\033[13;1m【错误】请输入正确的数字!\033[0m")
    exit()
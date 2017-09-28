#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

user = [{"username":"admin","password":"123456"}]

books = [{"bookname":"《三体世界》","price":20.00,"num":5,"user":"admin"},
         {"bookname": "《黑暗森林》", "price": 30.00, "num": 8,"user":"admin"},
         {"bookname": "《死神永生》", "price": 50.00, "num": 20,"user":"admin"}]
userAmount = [{"username":"admin","amount":100.00}]
userBooks = []

def index():
    print("********************************")
    print("**************主页**************")
    print("1、登录")
    print("2、注册")
    print("0、退出")
    print("********************************")
    choose = input("请选择：")
    if(choose=='1'):
        login()
    elif(choose=='2'):
        regis()
    elif(choose=='0'):
        logout()
    else:
        print("无效选择，请重新选择")
        index()

# 登录页面
def login():
    print("********************************")
    print("**************登录**************")
    print("********************************")
    username = input("请输入用户名:")
    password = input("请输入密码:")
    login_user = {"username":username,"password":password}
    if(login_user in user):
        login_success(username)
    else:
        print("账号密码错误")
        print("1、重新登录")
        print("2、去注册")
        print("0、退出")
        choose = input("请选择：")
        if (choose == '1'):
            login()
        elif (choose == '2'):
            regis()
        elif (choose == '0'):
            logout()
        else:
            print("无效选择，返回到首页")
            index()


# 注册页面
def regis():
    print("********************************")
    print("**************注册**************")
    print("********************************")
    username = input("请输入用户名:")
    password = checkPwd()
    reg_user = {"username":username,"password":password}
    user.append(reg_user)
    reg_amount = {"username":username,"amount":100.00}
    userAmount.append(reg_amount)
    print("注册成功！返回首页")
    index()


def checkPwd():
    password = input("请输入密码:")
    rePassword = input("请再次输入密码:")
    if (password != rePassword):
        print("两次密码不一致,请重新输入")
        checkPwd()
    else:
        return password

# 退出页面
def logout():
    print("系统即将关闭。。。。")


def login_success(username):
    print("登录成功，欢迎进入本系统")
    main_index(username)

def main_index(username):
    print("********************************")
    print("*********XXX图书管理系统*********")
    print("1、选购书籍")
    print("2、我的书籍")
    print("3、上传书籍")
    print("4、查看余额")
    print("0、退出")
    print("********************************")
    choose = input("请选择：")
    if (choose == '1'):
        book_list(username)
    elif (choose=='2'):
        book_manage(username)
    elif (choose == '3'):
        add_book(username)
    elif (choose == '4'):
        amount_manage(username)
    elif (choose == '0'):
        index()
    else:
        print("无效选择，请重新选择")
        main_index()


def book_list(username):
    print("*********书籍列表*********")
    print("\v\v编号\v\v书籍名称\v\v书籍价格\v\v剩余数量\v\v卖家")
    for i,book in enumerate(books):
        print("\v\v%s"%str(i+1),"\v\v%s"%book["bookname"],"\v\v%s"%str(book["price"]),"\v\v%s"%str(book["num"]),"\v\v\v%s"%str(book["user"]))
    print("请输入书籍编号选购书籍，按0返回上一级")
    choose = input("请选择：")
    if (choose == '0'):
        main_index(username)
    else:
        if(re.match("[0-9]",choose) and int(choose)<=len(books)):
            book_order(choose,username)
        else:
            print("输入编号有误，请重新选择")
            book_list(username)

def book_order(bookId,username):
    book = books[(int(bookId) - 1)]
    print("*********书籍订单*********")
    print("书籍名称:%s"%book["bookname"])
    print("书籍单价:%s"%str(book["price"]))
    print("1、确认购买")
    print("0、返回上一级")
    choose = input("请选择：")
    if (choose == '1'):
        num = checkBuyNum(book)
        submit_order(username,bookId,num)
    elif (choose == '0'):
        book_list(username)
    else:
        print("无效选择，请重新选择")
        book_list(username)

def checkBuyNum(book):
    num = input("请输入购买数量:")
    if (re.match("[^0-9]", num) and int(num) > int(book["num"])):
        print("购买数量有误，请重新输入")
        checkBuyNum(book)
    else:
        return num


def submit_order(username,bookId,num):
    book = books[(int(bookId) - 1)]
    print("*********提交订单*********")
    print("书籍名称:%s"%book["bookname"])
    print("书籍单价:%s"%str(book["price"]))
    print("购买数量:%s"%num)
    priceAll = int(int(num) * int(book["price"]))
    print("订单总价:%s"%priceAll)
    print("1、购买并支付")
    print("0、返回上一级")
    choose = input("请选择：")
    if (choose == '1'):
        amountId = getAmountByUser(username)
        amount = userAmount[amountId]
        if(int(amount["amount"])<priceAll):
            print("账户余额不足")
        else:
            doOrder(username,bookId,num)
            print("支付成功，购买成功，返回到书籍列表")
            book_list(username)
    elif (choose == '0'):
        book_order(book_order,username)
    else:
        print("无效选择，请重新选择")
        submit_order(username,bookId,num)

def doOrder(username,bookId,num):
    book = books[(int(bookId) - 1)]
    priceAll = int(int(num) * int(book["price"]))
    book["num"] = int(int(book["num"])-int(num))
    books[int(bookId)] = book
    amountId = getAmountByUser(username)
    amount = userAmount[amountId]
    amount["amount"] = int(int(amount["amount"])-priceAll)
    userAmount[amountId] = amount
    saleId = getAmountByUser(str(book["user"]))
    saleAmount = userAmount[saleId]
    saleAmount["amount"] = int(int(saleAmount["amount"]) + priceAll)
    userAmount[saleId] = saleAmount


def amount_manage(username):
    print("*********余额*********")
    print("0、退出")
    amountId = getAmountByUser(username)
    amount = userAmount[amountId]
    print("余额:%s"%amount["amount"])
    choose = input("请选择：")
    if (choose == '0'):
        main_index(username)
    else:
        print("无效选择，请重新选择")
        amount_manage(username)

def getAmountByUser(username):
    for i,amount in enumerate(userAmount):
        if(username==amount["username"]):
            return i
            break


def book_manage(username):
    print("************我的书籍*************")
    print("\v\v编号\v\v书籍名称\v\v书籍价格\v\v剩余数量")
    user_book_num = 0
    clearUserBooks()
    for i, book in enumerate(books):
        if(book["user"]==username):
            print("\v\v%s" % str(user_book_num + 1), "\v\v%s" % book["bookname"], "\v\v%s" % str(book["price"]),"\v\v%s" % str(book["num"]))
            userBooks.append(book)
            user_book_num+=1
    print("请输入书籍编号进行操作，输入0返回上一级")
    choose = input("请选择：")
    if (choose == '0'):
        main_index(username)
    else:
        if (re.match("[0-9]", choose) and int(choose) <= user_book_num):
            book_detail(choose, username)
        else:
            print("输入编号有误，请重新选择")
            book_manage(username)

def clearUserBooks():
    for i,book in enumerate(userBooks):
        del userBooks[i]


def book_detail(bookId,username):
    book = userBooks[int(int(bookId)-1)]
    print("************书籍详情******************")
    print("书籍名称:%s" % book["bookname"])
    print("书籍价格:%s" % str(book["price"]))
    print("书籍数量:%s" % str(book["num"]))
    print("1、编辑书籍")
    print("2、删除书籍")
    print("3、返回上一级")
    print("0、退出")
    choose = input("请选择：")
    if (choose == '1'):
        edit_book(username,bookId)
    elif (choose == '2'):
        del_book(bookId,username)
    elif(choose=='3'):
        book_manage(username)
    elif(choose=='0'):
        index()
    else:
        print("无效选择，请重新选择")
        book_detail(bookId,username)

def edit_book(username,bookId):
    book = userBooks[int(int(bookId) - 1)]
    print("************编辑书籍******************")
    print("当前编辑书籍名称:%s"%book["bookname"])
    bookname = input("请输入书籍名称:")
    price = checkPrice()
    num = checkBookNum()
    new_book = {"bookname":bookname,"price":price,"num":num,"user":username}
    books_id = getBookIdByBook(book)
    books[books_id] = new_book
    print("更改成功，返回到我的书籍")
    book_manage(username)

def checkPrice():
    price = input("请输入书籍价格:")
    if (re.match("[0-9]", price) ):
        return price
    else:
        print("价格格式不正确，请重新输入")
        checkPrice()

def checkBookNum():
    num = input("请输入书籍数量:")
    if (re.match("[0-9]", num) ):
        return num
    else:
        print("数量格式不正确，请重新输入")
        checkBookNum()

def add_book(username):
    print("************新增书籍*************")
    bookname = input("请输入书籍名称:")
    price = checkPrice()
    num = checkBookNum()
    new_book = {"bookname": bookname, "price": price, "num": num, "user": username}
    books.append(new_book)
    print("新增成功，返回到我的书籍")
    book_manage(username)

def del_book(bookId,username):
    book = userBooks[int(int(bookId) - 1)]
    print("*************删除书籍**************")
    print("当前编辑书籍名称:%s" % book["bookname"])
    print("1、确认删除")
    print("2、不删除，返回上一级")
    print("3、退出")
    choose = input("请选择:")
    if(choose=='1'):
        books_id = getBookIdByBook(book)
        del books[books_id]
        book_manage(username)
    elif(choose=='2'):
        book_manage(username)
    elif(choose=='3'):
        index()
    else:
        print("无效选择，请重新选择")
        del_book(bookId, username)


def getBookIdByBook(book):
    for i,b in enumerate(books):
        if(b==book):
            return i
            break




index()

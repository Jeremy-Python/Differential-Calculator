# 微分計算機v5.3 作者:沈啟安 更新日期:20210103
from __future__ import division  # 必須放在程式第一行
# 金鑰設定
print("金鑰驗證中......")
f = open("key.txt", mode="r")
k=False
while k==False:
    if f.read() != "Jeremy_Calculator":
        print("產品金鑰錯誤")
        key = input("請輸入產品金鑰")
        if key == "Jeremy_Calculator":
            print("金鑰正確")
            k=True
        else:
            print("金鑰錯誤")
    else:
        k=True
f.close()
f = open("key.txt", mode="w")
f.write("Jeremy_Calculator")
f.close()
# 啟動主程式
print("啟動中，請耐心等候(初次使用須等較久)......")
# 模組導入
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *
from tkinter.filedialog import askdirectory
from scipy import interpolate
from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np
import json
import time
import sys
import os
import datetime
import smtplib
# 前置作業
Result = ""
i = 5
NumbersListDisplay = []  # 儲存使用者輸入的數字並顯示
NumbersList = []  # 儲存已微分的數字
ResultOutputList = []  # 最後輸出
HistoryList = []  # 歷史紀錄
DrawHistoryList = []
DrawNumbersList = []
DrawHistoryNumbersList = []
# 導入歷史紀錄
f = open("history.txt", mode="r")
HistoryList = f.read().splitlines()
f.close()
# 說明
print("★歡迎使用微分計算機v5.3★")
print("使用方法如下:")
print("1.微分格式ax^b+cx^d+ex^f+gx+h(最高次方數可由使用者自行決定)")
print("  範例3x^4+4x^3+6x+7")
print("2.開始時，可直接輸入最高次數開始計算或選擇功能，功能簡介如下:")
print("3.輸入最高次數後，程式會依序詢問每一項的係數，如有缺項則輸入0")
print("  例:依照上方範例方程式，則先輸入最高次方數4，接著再依序輸入3 4 0 6 7即可")
print("4.輸入delete可以刪除指定歷史紀錄")
print("5.輸入deleteA可以刪除所有歷史紀錄")
print("6.輸入history可以查看歷史紀錄")
print("7.輸入out可以匯出歷史紀錄")
print("  (部分電腦需用系統管理員身分開啟此程式才能匯出)")
print("8.輸入feedback可以發給作者反饋與建議(需要連接網路)")
print("9.輸入draw可繪製指定歷史紀錄中計算結果的圖形")
print("10.輸入version可以顯示版本紀錄")
print("11.輸入key可以檢視產品啟用資訊")
print("12.輸入information可以查詢本程式最低系統需求")
print("13.輸入exit可離開程式")
print("---------------------------------------------------------------------------")
# 開始
while i > 0:
    # 導入繪圖歷史數字json
    filename = "number.json"
    with open(filename) as file:
        DrawHistoryNumbersList = json.load(file)
    # 清空串列與設定
    NumbersListDisplay = []
    NumbersList = []
    ResultOutputList = []
    DrawNumbersList = []
    Result = ""
    # 判斷輸入為功能或數字
    try:
        num1 = input("請問你的最高次方數是多少?(或要什麼功能?)")
        if int(num1) < 0:
            print("請輸入正確數字或功能")
        num2 = int(num1)
    except ValueError:
        num2 = 0

    if num1 == "delete":  # 部分刪除
        delete1 = input("請問要刪除第幾項?")
        try:
            try:
                PoppedResult = HistoryList.pop(int(delete1)-1)
                print("已刪除", PoppedResult)
                print("``````````````````````````")
                print("歷史紀錄:")
                if len(HistoryList) > 0:
                    i = 1
                    for out in HistoryList:
                        print(str(i)+". "+HistoryList[i-1])
                        i += 1
                if len(HistoryList) == 0:
                    print("空白......")
                print("--------------------------")
                data = open("history.txt", mode="w")
                for save in HistoryList:
                    print(save, file=data)
                data.close()
                poppedresult = DrawHistoryNumbersList.pop(int(delete1)-1)
                filename = "number.json"
                with open(filename, "w") as file:
                    json.dump(DrawHistoryNumbersList, file)
            except ValueError:
                print("請確認輸入之項數正確")
                print("--------------------------")
        except IndexError:
            print("請確認輸入之項數正確")
            print("------------------------------")
    elif num1 == "key":  # 輸入金鑰
        print("--------------------------------")
        print("產品已啟動 授權到期日:2099/12/31")
        print("--------------------------------")
        ask = input("是否要輸入新的金鑰?")
        if ask == "y":
            a = 1
            while(a == 1):
                newkey = input("請輸入金鑰")
                if newkey != "YC7DK-G2NP3-2QQC3-J6H88-GVGXT":
                    print("金鑰輸入錯誤")
                    print("------------")
                    a = 1
                if newkey == "YC7DK-G2NP3-2QQC3-J6H88-GVGXT":
                    a = 0
                    print("啟動產品中......")
                    print("產品已啟動")
                    print("----------")
        else:
            print("不輸入")
    elif num1 == "deleteA":  # 全部刪除
        HistoryList = []
        DrawHistoryList = []
        print("已刪除所有歷史紀錄")
        print("-----------------")
        print("歷史紀錄:")
        if len(HistoryList) > 0:
            i = 1
            for out in HistoryList:
                print(str(i)+". "+HistoryList[i-1])
                i += 1
        if len(HistoryList) == 0:
            print("空白......")
        print("--------------------------")
        data = open("history.txt", mode="w")
        for save in HistoryList:
            print(save, file=data)
        data.close()
        DrawHistoryNumbersList = []
        filename = "number.json"
        with open(filename, "w") as file:
            json.dump(DrawHistoryNumbersList, file)
    elif num1 == "version":
        print("-------------")
        data = open("version.txt", mode="r",encoding="utf-8")
        words = data.read()
        print(words)
        print("-------------")
    elif num1 == "information":
        print("-----------------")
        print("1.本程式可在Windows10和Windows11任何版本上執行")
        print("2.32位元或64位元電腦皆可使用")
        print("3.CPU i5 以上")
        print("4.記憶體 4GB 以上")
        print("5.磁碟空間約300MB")
        print("-----------------")
    elif num1 == "history":  # 顯示歷史紀錄
        print("歷史紀錄:")
        if len(HistoryList) > 0:
            i = 1
            for out in HistoryList:
                print(str(i)+". "+"\n"+HistoryList[i-1]+"\n")
                i += 1
            draw_turn = i
        if len(HistoryList) == 0:
            print("空白......")
        print("--------------------------")
    elif num1 == "feedback":  # 回饋與建議
        v = 5.1
        print("檢查網路連線中......")
        exit_code = os.system('ping www.google.com')
        if exit_code:
            print("網路無法連接")
            print("------------")
        else:
            print("網路連線正常")
            print("------------")
            try:
                ask = int(input("請輸入寄件人信箱種類:(1=gmail , 2=yahoo, 3=自行輸入)"))
                if ask == 1:
                    try:
                        emailaccount = input("請輸入寄件人gmail信箱帳號:")
                        password = input("請輸入寄件人gmail信箱密碼:")
                        contenthing = input("請輸入內容:")
                        content = MIMEMultipart()  # 建立MIMEMultipart物件
                        content["subject"] = "微分計算機v"+str(v)+"問題回報"  # 郵件標題
                        content["from"] = emailaccount  # 寄件者
                        content["to"] = "jeremy.studyhard666@gmail.com"  # 收件者
                        content.attach(MIMEText(contenthing))  # 郵件內容
                        with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
                            smtp.ehlo()  # 驗證SMTP伺服器
                            smtp.starttls()  # 建立加密傳輸
                            smtp.login(emailaccount, password)  # 登入寄件者gmail
                            smtp.send_message(content)  # 寄送郵件
                            print("已成功發送")
                            print("----------")
                    except:
                        print("--------------------------------------------------")
                        print(
                            "錯誤，可能原因有以下兩點:\n1.帳號密碼輸入錯誤，請再試一次\n2.寄件帳號未開啟低安全性應用程式存取權\n  請至https://myaccount.google.com/lesssecureapps更改設定")
                        print("--------------------------------------------------")
                if ask == 2:
                    try:
                        emailaccount = input("請輸入寄件人yahoo信箱帳號:")
                        password = input("請輸入寄件人yahoo信箱「第三方應用程式密碼」:")
                        contentthing = input("請輸入內容:")
                        content = MIMEMultipart()  # 建立MIMEMultipart物件
                        content["subject"] = "微分計算機v"+str(v)+"問題回報"  # 郵件標題
                        content["from"] = emailaccount  # 寄件者
                        content["to"] = "10931047@stu.tshs.tp.edu.tw"  # 收件者
                        content.attach(MIMEText(contentthing))  # 郵件內容
                        # 設定SMTP伺服器
                        with smtplib.SMTP(host="smtp.mail.yahoo.com", port="587") as smtp:
                            smtp.ehlo()  # 驗證SMTP伺服器
                            smtp.starttls()  # 建立加密傳輸
                            smtp.login(emailaccount, password)  # 登入寄件者
                            smtp.send_message(content)  # 寄送郵件
                            print("已成功發送")
                            print("----------")
                    except:
                        print(
                            "錯誤，可能原因有以下兩點:\n1.帳號密碼輸入錯誤，請再試一次\n2.密碼未輸入第三方應用程式密碼\n  請至https://login.yahoo.com/account/security更改設定")
                        print(
                            "-------------------------------------------------------")
                if ask == 3:
                    try:
                        smtp = input("請輸入該郵箱之smtp伺服器:")
                        port = input("請輸入該smtp伺服器的port:")
                        emailaccount = input("請輸入寄件人信箱帳號:")
                        password = input("請輸入寄件人密碼:")
                        contentthing = input("請輸入內容:")
                        content = MIMEMultipart()  # 建立MIMEMultipart物件
                        content["subject"] = "微分計算機v"+str(v)+"問題回報"  # 郵件標題
                        content["from"] = emailaccount  # 寄件者
                        content["to"] = "10931047@stu.tshs.tp.edu.tw"  # 收件者
                        content.attach(MIMEText(contentthing))  # 郵件內容
                        with smtplib.SMTP(host=smtp, port=port) as smtp:  # 設定SMTP伺服器
                            smtp.ehlo()  # 驗證SMTP伺服器
                            smtp.starttls()  # 建立加密傳輸
                            smtp.login(emailaccount, password)  # 登入寄件者
                            smtp.send_message(content)  # 寄送郵件
                            print("已成功發送")
                            print("----------")
                    except:
                        print(
                            "錯誤，可能原因有以下四點:\n1.帳號密碼輸入錯誤，請再試一次\n2.smtp或port輸入錯誤\n3.請確定帳戶已開啟低安全性應用程式存取權")
                        print(
                            "-------------------------------------------------------")
            except ValueError:
                print("請輸入正確功能")
                print("--------------")
    elif num1 == "out":
        root = Tk()
        root.withdraw()
        path = askdirectory()
        FileName = input("請輸入檔案名稱:")
        OpenData = path+"\\"+FileName+".txt"
        try:
            data = open(OpenData, mode="x")
            print(HistoryList, "      ""保存時間:", datetime.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S'), file=data)
            data.close()
            print("已成功將歷史紀錄保存成功")
            print("-------------------------------------------------")
        except PermissionError:
            print("請以系統管理員身分開啟此程式(請注意，關閉程式後，歷史紀錄將會清除)")
            print("------------------------------------------------------------------")
        except OSError:
            print("程式執行錯誤，可能原因有\n 1.未輸入正確位置\n 2.未以系統管理員身分開啟此程式")
            print(
                "------------------------------------------------------------------------")
        except FileNotFoundError:
            print("請輸入正確位置")
            print("------------------------------------------------------------------")
        except FileExistsError:
            try:
                data = open(OpenData, mode="a")
                print(HistoryList, "      ""保存時間:", datetime.datetime.now().strftime(
                    '%Y-%m-%d %H:%M:%S'), file=data)
                data.close()
                print("已成功將歷史紀錄保存成功" % (path, FileName))
                print("-------------------------------------------------")
            except PermissionError:
                print("請以系統管理員身分重新開啟此程式")
                print(
                    "----------------------------------------------------------------------------------")
    elif num1 == "draw":
        try:
            DrawYN = int(input("請問要將歷史紀錄第幾項繪圖?"))
            if str(DrawHistoryNumbersList[DrawYN-1]) == "0":
                print("繪圖中......")
                print("------------")
                x = np.linspace(-10, 10, 100)
                y1 = 0*x
                plt.style.use('bmh')
                fig = plt.figure()
                ax = plt.axes()
                plt.xlim(-10, 10)
                plt.ylim(-100, 100)
                xnew = np.arange(-10, 10, 0.01)
                func = interpolate.interp1d(x, y1, kind='cubic')
                ynew = func(xnew)
                plt.plot(xnew, ynew)
                plt.show()
                print("繪圖完成")
                print("--------------")
            else:
                try:
                    if str(DrawHistoryNumbersList[DrawYN-1]) != "0":
                        print("繪圖中......")
                        print("------------")
                        DrawNumber = DrawHistoryNumbersList[DrawYN-1]
                        x = 1
                        y1 = float(DrawNumber)*1
                        plt.style.use('bmh')
                        fig = plt.figure()
                        ax = plt.axes()
                        x = np.linspace(-10, 10, 100)
                        plt.ylim(-50, 50)
                        plt.axhline(y=int(DrawNumber))
                        plt.show()
                        print("繪圖完成")
                        print("--------------")
                except TypeError:
                    x = np.linspace(-10, 10, 100)
                    try:
                        z = 0
                        y1 = (DrawHistoryNumbersList[DrawYN-1][z]) * \
                            x**(len(DrawHistoryNumbersList[DrawYN-1])-1)
                        z = 1
                        while z >= 0:
                            y1 = y1 + \
                                DrawHistoryNumbersList[DrawYN-1][z]*x**(
                                    len(DrawHistoryNumbersList[DrawYN-1])-(z+1))
                            z += 1
                    except IndexError:
                        plt.style.use('bmh')
                        fig = plt.figure()
                        ax = plt.axes()
                        plt.xlim(-10, 10)
                        plt.ylim(-100, 100)
                        xnew = np.arange(-10, 10, 0.01)
                        func = interpolate.interp1d(x, y1, kind='cubic')
                        ynew = func(xnew)
                        plt.plot(xnew, ynew)
                        plt.show()
                        print("繪圖完成")
                        print("--------------")
        except IndexError:
            print("請輸入正確項數")
            print("--------------")

    elif num1 == "exit":
        sys.exit(0)
    # 開始計算
    else:
        power = []
        try:
            testnumber = int(num1)
            time1 = Decimal(num1)
            time2 = num1
            if time2 == "0":
                power.append(int("0"))
                print("計算結果:")
                print("0")
                HistoryList.insert(0, "0")
                print("\n歷史紀錄:")
                i = 1
                for out in HistoryList:
                    print(str(i)+". \n"+HistoryList[i-1]+"\n")
                    i = i+1
                print("--------------------------")
                # 保存歷史紀錄
                data = open("history.txt", mode="w")
                for save in HistoryList:
                    print(save, file=data)
                data.close()
                # 保存DrawHistoryNumbersList
                DrawHistoryNumbersList.insert(0,"0")
                filename = "number.json"
                with open(filename, "w") as file:
                    json.dump(DrawHistoryNumbersList, file)
                DrawYN = input("是否要繪圖?(y:繪圖，n:不繪圖)")
                if DrawYN == "y":
                    print("繪圖中......")
                    print("------------")
                    x = np.linspace(-10, 10, 100)
                    y1 = 0*x
                    plt.style.use('bmh')
                    fig = plt.figure()
                    ax = plt.axes()
                    plt.xlim(-10, 10)
                    plt.ylim(-100, 100)
                    xnew = np.arange(-10, 10, 0.01)
                    func = interpolate.interp1d(x, y1, kind='cubic')
                    ynew = func(xnew)
                    plt.plot(xnew, ynew)
                    plt.show()
                    print("繪圖完成")
                    print("--------------")
                else:
                    print("不要繪圖")
                    print("----------")
                    x = np.linspace(-10, 10, 100)
                    y1 = 0*x
            elif time2 == "1":
                NumberInput = input("請依序輸入各項係數:")
                power.append(int("1"))
                print("計算結果:")
                print(NumberInput)
                HistoryList.insert(0, NumberInput)
                print("\n歷史紀錄:")
                i = 1
                for out in HistoryList:
                    print(str(i)+". \n"+HistoryList[i-1]+"\n")
                    i = i+1
                # 保存歷史紀錄
                data = open("history.txt", mode="w")
                for save in HistoryList:
                    print(save, file=data)
                data.close()
                print("--------------------------")
                # 保存DrawHistoryNumbersList
                DrawHistoryNumbersList.insert(0,NumberInput)
                filename = "number.json"
                with open(filename, "w") as file:
                    json.dump(DrawHistoryNumbersList, file)
                drawYN = input("是否要繪圖?(y:繪圖，n:不繪圖)")
                if drawYN == "y":
                    print("繪圖中......")
                    print("------------")
                    x = 1
                    y1 = float(NumberInput)*1
                    plt.style.use('bmh')
                    fig = plt.figure()
                    ax = plt.axes()
                    x = np.linspace(-10, 10, 100)
                    plt.ylim(-50, 50)
                    plt.axhline(y=int(NumberInput))
                    plt.show()
                    print("繪圖完成")
                    print("--------------")
                else:
                    print("不要繪圖")
                    print("----------")
                    y1 = NumberInput*1
            else:
                while time1 >= 0:
                    if time1 == 0:
                        NumberInput = input("請依序輸入各項係數:")
                        testnumber = float(NumberInput)
                        NumbersListDisplay.append(NumberInput)
                        print(NumbersListDisplay)
                        NumberInput = Decimal(NumberInput)
                        time1 = time1-1
                    else:
                        NumberInput = input("請依序輸入各項係數:")
                        testnumber = float(NumberInput)
                        NumbersListDisplay.append(NumberInput)
                        print(NumbersListDisplay)
                        NumberInput = Decimal(NumberInput)
                        a = str(Decimal(NumberInput*time1))
                        NumbersList.append(a)####
                        time1 = time1-1
                Ctime = len(NumbersList)
                time2 = int(time2)-1
                # 計算最高次
                if len(NumbersList) >= 3:
                    ResultOutput = str(NumbersList[0])+"x^"+str(time2)
                    DrawNumbers = float(NumbersList[0])
                    ResultOutputList.append(ResultOutput)
                    DrawNumbersList.append(DrawNumbers)
                    popped = NumbersList.pop(0)
                    power.append(int(time2))
                    time2 = time2-1
                    Ctime = Ctime-1
                # 計算(最高次、一次、常數除外)
                while Ctime >= 3:
                    if float(NumbersList[0]) > 0:
                        ResultOutput = "+"+str(NumbersList[0])+"x^"+str(time2)
                        DrawNumbers = float(NumbersList[0])
                        ResultOutputList.append(ResultOutput)
                        DrawNumbersList.append(DrawNumbers)
                        popped = NumbersList.pop(0)
                        power.append(int(time2))
                        time2 = time2-1
                        Ctime = Ctime-1
                    elif float(NumbersList[0]) < 0:
                        ResultOutput = str(NumbersList[0])+"x^"+str(time2)
                        DrawNumbers = float(NumbersList[0])
                        ResultOutputList.append(ResultOutput)
                        DrawNumbersList.append(DrawNumbers)
                        popped = NumbersList.pop(0)
                        power.append(int(time2))
                        time2 = time2-1
                        Ctime = Ctime-1
                    elif float(NumbersList[0]) == 0:
                        popped = NumbersList.pop(0)
                        time2 = time2-1
                        Ctime = Ctime-1
                # 一次項計算
                if float(NumbersList[0]) > 0:
                    if num2 == 2:
                        ResultOutput = str(NumbersList[0])+"x"
                        DrawNumbers = float(NumbersList[0])
                        ResultOutputList.append(ResultOutput)
                        DrawNumbersList.append(DrawNumbers)
                        del NumbersList[0]
                        power.append(int(time2))
                        time2 = time2-1
                    if num2 != 2:
                        ResultOutput = "+"+str(NumbersList[0])+"x"
                        DrawNumbers = float(NumbersList[0])
                        ResultOutputList.append(ResultOutput)
                        DrawNumbersList.append(DrawNumbers)
                        popped = NumbersList.pop(0)
                        power.append(int(time2))
                        time2 = time2-1
                elif float(NumbersList[0]) < 0:
                    ResultOutput = str(NumbersList[0])+"x"
                    DrawNumbers = float(NumbersList[0])
                    ResultOutputList.append(ResultOutput)
                    DrawNumbersList.append(DrawNumbers)
                    popped = NumbersList.pop(0)
                    power.append(int(time2))
                    time2 = time2-1
                elif float(NumbersList[0]) == 0:
                    popped = NumbersList.pop(0)
                    time2 = time2-1
                # 常數項計算
                if float(NumbersList[0]) > 0:
                    ResultOutput = "+"+str(NumbersList[0])
                    DrawNumbers = float(NumbersList[0])
                    ResultOutputList.append(ResultOutput)
                    DrawNumbersList.append(DrawNumbers)
                    popped = NumbersList.pop(0)
                    power.append(int(time2))
                    time2 = time2-1
                elif float(NumbersList[0]) < 0:
                    ResultOutput = str(NumbersList[0])
                    DrawNumbers = float(NumbersList[0])
                    ResultOutputList.append(ResultOutput)
                    DrawNumbersList.append(DrawNumbers)
                    popped = NumbersList.pop(0)
                    power.append(int(time2))
                    time2 = time2-1
                elif float(NumbersList[0]) == 0:
                    popped = NumbersList.pop(0)
                    time2 = time2-1
                # 計算結束
                print("計算結果:")
                for AnswerEnd in ResultOutputList:
                    print(AnswerEnd, end="")
                    Result = Result+AnswerEnd
                HistoryList.insert(0, Result)
                print("\n\n歷史紀錄:")
                hnumber = 1
                for out in HistoryList:
                    print(str(hnumber)+". "+"\n"+HistoryList[hnumber-1]+"\n")
                    hnumber = hnumber+1
                print("--------------------------")
                # 保存歷史紀錄
                data = open("history.txt", mode="w")
                for save in HistoryList:
                    print(save, file=data)
                data.close()
                # 保存DrawHistoryNumbersList
                DrawHistoryNumbersList.insert(0,DrawNumbersList)
                filename = "number.json"
                with open(filename, "w") as file:
                    json.dump(DrawHistoryNumbersList, file)
                DrawHistoryNumbersList = []
                # 繪圖
                drawYN = input("是否要繪圖?(y:繪圖，n:不繪圖)")
                if drawYN == "y":
                    print("繪圖中......")
                    print("------------")
                    drawing = len(power)
                    x = np.linspace(-10, 10, 100)
                    y = DrawNumbersList[0]*x**power[0]
                    popped = DrawNumbersList.pop(0)
                    popped = power.pop(0)
                    drawing -= 1
                    while drawing >= 1:
                        y += DrawNumbersList[0]*x**power[0]
                        popped = DrawNumbersList.pop(0)
                        popped = power.pop(0)
                        drawing -= 1
                    plt.style.use('bmh')
                    fig = plt.figure()
                    ax = plt.axes()
                    plt.xlim(-10, 10)
                    plt.ylim(-100, 100)
                    xnew = np.arange(-10, 10, 0.01)
                    func = interpolate.interp1d(x, y, kind='cubic')
                    ynew = func(xnew)
                    plt.plot(xnew, ynew)
                    plt.show()
                    print("繪圖完成")
                    print("--------------")
                else:
                    print("不要繪圖")
                    print("----------")
        except:
            print("請輸入正確數字或功能")
            print("--------------------")
# 程式結束

import requests
import os
import re
import wget
import time
import sys
import random
import math

# 软件信息
ILikeZengQi = True
Version = "1.2b"
UpdateTime = "2022/6/14"
UpdateLog = "1.1\n" \
            "1,完善了引导\n" \
            "2,添加了b版\n" \
            "1.2\n" \
            "1,增加了根目录下载\n" \
            "1.3\n" \
            "1,优化UI\n" \
 \
    # 网站信息
UploadPageHtml_str = ""
UploadPage = ""
WebData_Line_and_Title = ""
WebData_Line = ""
WebData_Title = ""
WebData_Pic = ""
WebData_PageStr = ""
WebData_Page = 0

# 选择变量
DownloadStart = 0  # 开始的号码
DownloadNow = DownloadStart  # 现在正在处理的号码
DownloadEnd = 0  # 结束的号码
DownloadSum = 1
AlwaysDownload = False
input_int = 0

# 下载变量
DownloadSite = ""
Download_List = []  # 下载列表
Download_List.append("0")
DownloadSelect = ""

# 其他变量
NowTime = 0.0


# 核心函数
def uploadpage():
    global UploadPageHtml_str
    global UploadPage

    UploadPageHtml_str = requests.get('https://m.tuiimg.com/meinv/').content.decode()
    UploadPage = (''.join(re.findall(r'<ul class="main" id="main"><li><h2><a href="https://m.tuiimg.com/meinv/(.*?)/">',
                                     UploadPageHtml_str)))


def initialize():
    global WebData_Line_and_Title
    global WebData_Line
    global WebData_Title
    global WebData_Pic
    global WebData_PageStr
    global WebData_Page
    global DownloadStart

    global DownloadNow
    global DownloadEnd
    global DownloadSum
    global AlwaysDownload
    global DownloadSite

    global DownloadSelect
    global Download_List
    global DownloadSelect

    global NowTime

    # 网站信息
    WebData_Line_and_Title = ""
    WebData_Line = ""
    WebData_Title = ""
    WebData_Pic = ""
    WebData_PageStr = ""
    WebData_Page = 0

    # 选择变量
    DownloadStart = 0  # 开始的号码
    DownloadNow = DownloadStart  # 现在正在处理的号码
    DownloadEnd = 0  # 结束的号码
    DownloadSum = 1
    AlwaysDownload = False

    # 下载变量
    DownloadSite = ""
    DownloadSelect = False
    Download_List = []  # 下载列表
    Download_List.append("0")
    DownloadSelect = ""

    # 其他变量
    NowTime = 0.0


def inputint():
    global input_int
    global DownloadNow
    global UploadPage
    print(DownloadNow)

    try:

        input_int = int(DownloadNow)
        if input_int == int:

            if 1 <= input_int() <= UploadPage is True:
                return True

            else:
                return False
        else:
            return False
    except:
        return False


def gettime():
    global NowTime
    time_tuple = time.localtime(time.time())
    NowTime = "{}:{}:{}".format(time_tuple[3], time_tuple[4], time_tuple[5])


def getinformationa():  # 获取网站信息
    global DownloadNow
    global WebData_Line_and_Title
    global WebData_Line
    global WebData_Title
    global WebData_Pic
    global WebData_PageStr
    global WebData_Page

    html_str = requests.get('https://m.tuiimg.com/meinv/' + str(DownloadNow) + '/').content.decode()
    # 获取链接,标题,图片格式
    WebData_Line_and_Title = (''.join(re.findall(r'<div class="content" id="content"><img src=".*" id="', html_str)))
    WebData_Line = (''.join(re.findall(r'<div class="content" id="content"><img src=".* alt="', WebData_Line_and_Title))
                    )
    WebData_Title = (''.join(re.findall(r'" alt="(.*)" id="', WebData_Line_and_Title)))
    WebData_Pic = (''.join(re.findall(r'/1.(.*)" alt="', WebData_Line)))
    WebData_Line = (''.join(re.findall(r'<div class="content" id="content"><img src="(.*)1.', WebData_Line)))
    # 获取页数
    WebData_PageStr = (''.join(re.findall(r'展开全图(.*)</i></span><span class="next" id', html_str)))
    WebData_PageStr = (''.join(re.findall(r'/(.*)\)', WebData_PageStr)))
    WebData_Page = int(WebData_PageStr)
    print()
    print("////////////////////")
    print("图片服务器状态：已获取")
    print("标题：" + WebData_Title)
    print("页数：" + WebData_PageStr)
    print("图片格式为：" + "." + WebData_Pic)
    print("////////////////////")
    print()


def getImformationb():  # 获取网站信息
    global DownloadNow
    global WebData_Line_and_Title
    global WebData_Line
    global WebData_Title
    global WebData_Pic
    global WebData_PageStr
    global WebData_Page
    global DownloadSum

    html_str = requests.get('https://m.tuiimg.com/meinv/' + str(DownloadNow) + '/').content.decode()
    # 获取链接,标题,图片格式
    WebData_Line_and_Title = (''.join(re.findall(r'<div class="content" id="content"><img src=".*" id="', html_str)))
    WebData_Line = (''.join(re.findall(r'<div class="content" id="content"><img src=".* alt="', WebData_Line_and_Title))
                    )
    WebData_Title = (''.join(re.findall(r'" alt="(.*)" id="', WebData_Line_and_Title)))
    WebData_Pic = (''.join(re.findall(r'/1.(.*)" alt="', WebData_Line)))
    WebData_Line = (''.join(re.findall(r'<div class="content" id="content"><img src="(.*)1.', WebData_Line)))
    # 获取页数
    WebData_PageStr = (''.join(re.findall(r'展开全图(.*)</i></span><span class="next" id', html_str)))
    WebData_PageStr = (''.join(re.findall(r'/(.*)\)', WebData_PageStr)))
    WebData_Page = int(WebData_PageStr)

    print(str(DownloadNow) + ",标题：" + WebData_Title + "  页数：" + WebData_PageStr)
    print("图片服务器状态：已获取\n")


def downloadimage():  # 下载函数
    global WebData_Page
    global Download_List
    global DownloadSite
    global WebData_Title
    global WebData_PageStr
    global DownloadNow
    global DownloadEnd
    global DownloadStart

    listdownloadlist()
    path = DownloadSite + str(DownloadNow) + "、" + WebData_Title
    # 调用函数
    os.makedirs(path)

    gettime()
    print(str(NowTime) + "开始下载")

    n = 1
    for i in range(WebData_Page):
        gettime()
        print("\n")
        print(str(DownloadStart) + "-" + str(DownloadEnd) + "正在下载" + str(DownloadNow) + "(" + str(n) +
              "/" + WebData_PageStr + ")")
        wget.download(Download_List[n], DownloadSite + str(DownloadNow) + "、" + WebData_Title + "/" + str(n) + '.jpg')
        n = n + 1
    gettime()
    print("\n\n")
    print(str(NowTime) + "已储存至" + DownloadSite + str(DownloadNow) + "、" + WebData_Title + "/")

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def listdownloadlist():
    global WebData_Page
    global Download_List
    global DownloadNow
    Download_List = []
    Download_List.append("0")

    gettime()
    print(str(NowTime) + "正在读取下载列表")

    n = 1
    for i in range(WebData_Page):
        Download_List.append(WebData_Line + str(n) + ".jpg")
        n = n + 1

    print(str(NowTime) + "读取成功")


def downloadmodea():
    global DownloadNow
    global DownloadSelect
    global AlwaysDownload
    global WebData_Title
    global UploadPage

    while 1 == 1:

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        while 1 == 1:
            DownloadNow = input("请输入要下载的编号：")
            if DownloadNow == "":
                print("找不到您选择的册数！请选择规定册数以内的数字（1-" + str(UploadPage) + "）")
                continue

            inputint()
            if input_int:
                break

            if not input_int:
                print("找不到您选择的册数！请选择规定册数以内的数字（1-" + str(UploadPage) + "）")
                continue

        print("正在获取列表...")
        time.sleep(0.5)
        getinformationa()
        if AlwaysDownload:
            downloadimage()
        elif not AlwaysDownload:
            DownloadSelect = input("下载吗？\nY是/N否/A全是/C下载预览(其中随机一张):")
            if DownloadSelect == "Y":
                downloadimage()

                continue
            elif DownloadSelect == "N":
                continue
            elif DownloadSelect == "A":
                AlwaysDownload = True
                downloadimage()
            elif DownloadSelect == "C":
                gettime()
                print(str(NowTime) + "开始下载")

                gettime()
                print("\n")
                print(str(NowTime) + "正在下载" + "(1/1)")
                wget.download((WebData_Line + str(random.randint(1, WebData_Page)) + ".jpg"), DownloadSite
                              + str(DownloadNow) + str(WebData_Title) + '(预览).jpg')

                gettime()
                print("\n\n")
                print(str(NowTime) + "已储存至<" + DownloadSite + str(DownloadNow) + "," + WebData_Title + "(预览).jpg>")
                print(str(NowTime) + "下载完成,请按下Enter继续")
                input()
                print(
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                continue
            else:
                print("无法识别，请按下Enter继续并重新输入")
                input()
                print(
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                continue


def downloadmodeb():
    global DownloadStart
    global DownloadNow
    global DownloadEnd
    global DownloadSum
    global DownloadSelect

    while 1 == 1:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        DownloadStart = int(input("请输入要下载的编号头(包括)："))
        DownloadEnd = int(input("请输入要下载的编号尾(包括)："))
        DownloadSum = DownloadEnd - DownloadStart + 1
        DownloadNow = DownloadStart

        # print("正在获取列表...")
        # print()
        # print("////////////////////")
        # for i in range(DownloadSum):
        #    getImformationb()
        #    DownloadNow = DownloadNow + 1
        # DownloadNow = DownloadStart
        # print("////////////////////")
        print("总计：" + str(DownloadSum) + "(" + str(DownloadStart) + "-" + str(DownloadEnd) + ")")
        print("预计大小：" + str((math.ceil(4.475394378344913 * DownloadSum))) + "MB(" + str(math.ceil(4692791.135667396 *
                                                                                                  DownloadSum)) + "字节)")
        print("预计占用：" + str((math.ceil(4.541908848468271 * DownloadSum))) + "MB(" + str((math.ceil(4762536.612691466 *
                                                                                                   DownloadSum))) +
              "字节)")

        DownloadSelect = input("下载吗？Y是/N否")
        if DownloadSelect == "Y":
            for o in range(DownloadSum):
                getinformationa()
                listdownloadlist()
                downloadimage()
                DownloadNow = DownloadNow + 1

        elif DownloadSelect == "N":
            continue


print(str(time.time()) + "初始化中，请稍后...")
print(str(time.time()) + "正在初始化变量", end='')
initialize()
print("  成功")
print(str(time.time()) + "正在连接服务器", end='')
uploadpage()
print("  成功")
print("初始化成功！\n\n")
print("欢迎使用色色机器ヽ(✿ﾟ▽ﾟ)ノ")
print("版本" + str(Version))
print("更新时间" + UpdateTime + "")
print("目前一共收录" + UploadPage + "册\n")
print("我们将确认一些参数")
DownloadSite = input(r"请输入下载路径（例如E:\色图，如不输入则默认在根目录下载）：") + "\\"

DownloadSite = DownloadSite.replace("/", "\\")
print(os.path.isdir(DownloadSite))
print(DownloadSite)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("请选择下载模式：")
print("A.单个下载")
print("B.多个下载（例如114-514）")
DownloadMode = input()

while 1 == 1:  # 判断下载模式
    if DownloadMode == "A":
        downloadmodea()
    elif DownloadMode == "B":
        downloadmodeb()
    else:
        print("无法识别，请重新输入")
        DownloadMode = input()
        continue

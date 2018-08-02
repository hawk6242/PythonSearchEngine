from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests
from openpyxl import *
import sys

try:
    wb = load_workbook("ExcelSheet.xlsx")
    sheet = wb['TestingSheet']

    emp = None
    rows = 1149
    col = 6
    inc = 2
    lst = []
    codes = ["213", "310", "323", "818"]
    fb = "https://www.facebook.com/"
    yt = "https://www.youtube.com/"
    tw = "https://twitter.com/"
    ig = "https://www.instagram.com/"

    with open("Facebook.txt", "w+") as output:

        def Facebook(data):
            pass
            # url = data[0]
            # r = requests.get(url)
            # s = bs4(r.content, "html.parser")
            # div = s.find_all('div', class_="_4bl9")
            # a = s.find_all("a")
            # for item in a:
            #     if "schoolloop.com" in item.text:
            #         output.writelines('\t' + item.text + '\n')
            #         # print(item.text)
            #
            # for item in div:
            #     if "people like this" in item.text:
            #         output.writelines('\t' + item.text + '\n')
            #
            #     if "people follow this" in item.text:
            #         output.writelines('\t' + item.text + '\n')
            #
            #     if "Get Directions" in item.text:
            #         addr = item.text
            #         output.writelines('\t' + addr.replace("Get Directions", "") + '\n')
            #
            #     for c in codes:
            #         if c in item.text:
            #             # print(item.text)
            #             output.writelines('\t' + item.text + '\n')


        def YouTube(data):
            pass


        def Twitter(data):
            pass
            # url = data[0]
            # r = requests.get(url)
            # s = bs4(r.content, "html.parser")
            #
            # name = 'Twitter Username: @' + s.find('b', class_="u-linkComplex-target").text + '\n'
            # labels = s.find_all('span', class_="ProfileNav-label")
            # values = s.find_all('span', class_="ProfileNav-value")
            # location = s.find('div', class_="ProfileHeaderCard-location ")
            # website = s.find('span', class_='ProfileHeaderCard-urlText u-dir')
            # output.writelines('\t' + name.lstrip().rstrip() + '\n')
            #
            # if website:
            #     output.writelines('\t' + 'School Website: ' + website.text.lstrip().rstrip() + '\n')
            #
            # if location:
            #     output.writelines('\t' + 'Location: ' + location.text.lstrip().rstrip() + '\n')
            #
            # if len(labels) == 1:
            #     zipped = zip(labels[0], values[0])
            #     for l, v in zipped:
            #         output.writelines('\t' + l.text + ': ' + str(v.text).lstrip().rstrip() + '\n')
            #
            # if len(labels) <= 2:
            #     zipped = zip(labels[:1], values[:1])
            #     for l, v in zipped:
            #         output.writelines('\t' + l.text + ': ' + str(v.text).lstrip().rstrip() + '\n')
            #
            # if len(labels) <= 3:
            #     zipped = zip(labels[:2], values[:2])
            #     for l, v in zipped:
            #         output.writelines('\t' + l.text + ': ' + str(v.text).lstrip().rstrip() + '\n')
            #
            # if len(labels) >= 4:
            #     zipped = zip(labels[:3], values[:3])
            #     for l, v in zipped:
            #         output.writelines('\t' + l.text + ': ' + str(v.text).lstrip().rstrip() + '\n')


        def Instagram(data):
            url = data[0]
            path = './geckodriver'
            options = Options()
            options.add_argument('--headless')
            browser = webdriver.Firefox(executable_path=path, options=options)

            browser.get(url)
            html = browser.page_source

            s = bs4(html, 'html.parser')

            browser.close()
            name = s.find('h1', class_="AC5d8 notranslate")
            info = s.find_all('li', class_="Y8-fY")

            posts = info[0].text
            followers = info[1].text
            following = info[2].text

            print(name.text + '\n', posts, followers, following)


        def getData():
            for x in range(1, col):
                link = sheet.cell(row=inc, column=x)
                lst.append(link.value)
            return lst


        def removeNone():
            for x in range(1, len(lst)):
                if emp in lst:
                    lst.remove(emp)


        def SearchForLinks(filteredData):
            face = [f for f in filteredData if fb in f]
            you = [y for y in filteredData if yt in y]
            twit = [t for t in filteredData if tw in t]
            insta = [i for i in filteredData if ig in i]

            if face:
                name = lst[0]
                output.writelines('*****' + '\n')
                output.writelines("School Name: " + name + '\n')
                output.writelines('Facebook Information:' + '\n')
                Facebook(face)
                output.writelines('\n')
            if you:
                # print('*****')
                # print(lst[0])
                name = lst[0]
                output.writelines('*****' + '\n')
                output.writelines("School Name: " + name + '\n')
                YouTube(you)
            if twit:
                # print('*****')
                # print(lst[0])
                name = lst[0]
                output.writelines('*****' + '\n')
                output.writelines("School Name: " + name + '\n')
                output.writelines('Twitter Information:' + '\n')
                Twitter(twit)
            if insta:
                # print('*****')
                # print(lst[0])
                name = lst[0]
                output.writelines('*****' + '\n')
                output.writelines("School Name: " + name + '\n')
                output.writelines('Instagram Information:' + '\n')
                print(Instagram(insta))


        while inc != rows:
            getData()
            removeNone()

            if len(lst) == 1:
                inc += 1
                del lst[0]
                getData()
                removeNone()

            if len(lst) > 1:
                SearchForLinks(lst)
                inc += 1
                lst.clear()
                getData()
                removeNone()

            if inc == rows - 1:
                print("Done")

except KeyboardInterrupt:
    sys.exit(0)

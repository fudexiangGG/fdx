import requests as rq
from bs4 import BeautifulSoup as bs
import re

n=0
page=1
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
header2={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'}
search=input('输入需要搜索的公众号:')

def open_url():
    url='https://weixin.sogou.com/weixin?query=%s&_sug_type_=&s_from=input&_sug_=n&type=1&page=%s&ie=utf8' % (search,page)
    html=rq.get(url,headers=header2)
    data=bs(html.text,"html.parser")
    return data

data=open_url()
num=re.findall('\d+',data.find_all('div',class_='mun')[0].text)[0]
print("总共有%s条结果,你需要全部查看吗?" % num)
num2=int(input("输入需要查看的数量:"))


while n < num2:
    length=len(data.find_all('ul',class_='news-list2')[0].find_all('li'))

    i = 0
    while i != length:
        message=re.findall("认证|最近文章", data.find_all('ul', class_='news-list2')[0].find_all('li')[i].text)
        name = data.find_all('ul', class_='news-list2')[0].find_all('li')[i].find_all('p')[0].text.strip()
        Wechat_ID = data.find_all('ul', class_='news-list2')[0].find_all('li')[i].find_all('p')[1].text.strip()
        describe = data.find_all('ul', class_='news-list2')[0].find_all('li')[i].find_all('dl')[0].text.strip()
        if len(message) == 2:
            o=data.find_all('ul',class_='news-list2')[0].find_all('li')[i].find_all('dl')[1].text.strip()
            Wechat_auth=re.findall(r'document.write.*\)(.*\n.*)',o)[0]
            o=data.find_all('ul',class_='news-list2')[0].find_all('li')[i].find_all('dl')[2].text.strip()
            Newlog=re.findall("(.*\n\n.*)document.write.*\)",o)[0]
            print('''公众号名称:%s\n%s\n%s\n%s\n%s''' % (name,Wechat_ID,describe,Wechat_auth,Newlog))
            print("----------------------------------------------------------------------")
        elif "认证" in message:
            o = data.find_all('ul', class_='news-list2')[0].find_all('li')[i].find_all('dl')[1].text.strip()
            Wechat_auth = re.findall(r'document.write.*\)(.*\n.*)', o)[0]
            print('''公众号名称:%s\n%s\n%s\n%s''' % (name, Wechat_ID, describe, Wechat_auth))
            print("----------------------------------------------------------------------")
        elif "最近文章" in message:
            o = data.find_all('ul', class_='news-list2')[0].find_all('li')[i].find_all('dl')[1].text.strip()
            Newlog = re.findall("(.*\n\n.*)document.write.*\)", o)[0]
            print('''公众号名称:%s\n%s\n%s\n%s''' % (name, Wechat_ID, describe, Newlog))
            print("----------------------------------------------------------------------")
        else:
            print('''公众号名称:%s\n%s\n%s''' % (name, Wechat_ID, describe))
            print("----------------------------------------------------------------------")
        i=i+1
        n = n + 1
        if n == num2:break

    page=page+1
    data = open_url()
print("总共显示了%s条记录" % n)


import requests
from bs4 import BeautifulSoup
page = 150573
while page > 150510:
    init_url = "http://www.27270.com/word/dongwushijie/2016/"+str(page)+".html"
    init_request = requests.get(init_url).text   # test 源码(网页)  content 二进制（保存图片文件）
    # init_request.encode('utf-8')  或者gb312 来取得编码
    page_soup = BeautifulSoup(init_request, "html.parser")  # 解析结构 lxml :解析器  html.parser:解析器
    base_soup = page_soup.find('div', {'id': 'picBody'})  # 丢进beautiful soup 解析得到规整的数据流并寻找div键值
    img = base_soup.find_all('img')
    i = 0
    for each in img:
     # 在每个图片的url中查询src标签来获得真实路径
        url = each['src']
        # 伪装浏览器，添加UA 防止被ban
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"}
        img_source = requests.get(url, headers).content
        # 写入文件，命名规则为页数加上本页的第几张  0开始计数
        f = open('2016'+str(page)+str(i)+'.jpg', 'wb')
        f.write(img_source)
        f.close()
        print('finish'+str(i))   # 控制台输出当前完成进度
        i = i+1
    page = page - 1  # 对页数自动减一，为下一个url的构建提供参数


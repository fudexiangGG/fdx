# 爬虫小练习   
使用方法:python3 filename.py   
1、WechatSogou [1]– 微信公众号爬虫.  
基于搜狗微信搜索的微信公众号爬虫接口，可以扩展成基于搜狗搜索的爬虫，返回结果是列表，每一项均是公众号具体信息字典.  
wechat_vipcn_spider.py   

2.DouBanSpider [2]– 豆瓣读书爬虫。   
可以爬下豆瓣读书标签下的所有图书，存储到Excel中，可方便大家筛选搜罗，比如筛选评价人数>1000的高分书籍；可依据不同的主题存储到Excel不同的Sheet ，采用User Agent伪装为浏览器进行爬取，并加入随机延时来更好的模仿浏览器行为，避免爬虫被封。   
douban_spider.py     
>加入了`fake_useragent`模块 随机产生user-agent     
>使用`round(random.uniform(0.1, 2.0), 5)`随机延时  
>效果图:  
>><img src="https://github.com/fudexiangGG/fdx/blob/master/spider/image/douban.JPG?raw=true" height=50% width=60% alt="douban"/>   
>><img src="https://github.com/fudexiangGG/fdx/blob/master/spider/image/excel.JPG?raw=true" height=50% width=60% alt="excel"/>   

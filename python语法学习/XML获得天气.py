#coding=utf-8
#从yahoo获得天气xml,并且用ElementTree解析(cElementTree速度更快)
from urllib import request
def crawler():
    with request.urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml') as f:
        return f.read().decode('utf-8')
xml = crawler()
# print(xml) 浏览器中没有显示yweather的命名空间
def ET_parser(xml):
    import xml.etree.cElementTree as ET
    import time
    root = ET.fromstring(xml) #或者parse一个xml文件
    channel = root.find('results/channel')
    location = channel.find('{http://xml.weather.yahoo.com/ns/rss/1.0}location')
    city = location.attrib['city'] # 北京
    print('返回一个%s的天气dict' % city)
    l = []
    for node in channel.find('item').iter(tag='{http://xml.weather.yahoo.com/ns/rss/1.0}forecast'):
        date = time.strftime('%Y-%m-%d', time.strptime(node.attrib['date'], '%d %b %Y'))
        l.append({'date': date, 'high': node.attrib['high'], 'low': node.attrib['low']})
    return {
        'city': city,
        'forecast': l
    }
print(ET_parser(xml))

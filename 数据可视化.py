#-*- codeing = utf-8 -*-
import matplotlib.pyplot as plt
from lxml import etree
from selenium import webdriver
import re
import matplotlib
matplotlib.rc("font",family='YouYuan')

def bubble_sort(list_1):        #冒泡法排序
    for j in range(len(list_1)):
        for i in range(len(list_1)-1):
            if list_1[i]<list_1[i + 1]:
                k = list_1[i]
                list_1[i] = list_1[i+1]
                list_1[i+1] = k
        j=j+1
    return list_1

city = [''for n in range(34)]   #存放城市列表
rain = [''for n in range(34)]   #存放有关降雨量信息的数值

driver = webdriver.Chrome(executable_path='chromedriver')   #使用chrome浏览器打开

for a in range(1,5):      #直辖市数据
    url_a= f'http://www.weather.com.cn/weather1dn/1010{a}0100.shtml'  #网址
    driver.get(url_a)    #打开网址

    rain_list = []
    city_list = []
    resp_text = driver.page_source
    page_html = etree.HTML(resp_text)

    city_list = page_html.xpath('/html/body/div[4]/div[2]/a')[0]    #通过xpath爬取城市名称
    rain_list = page_html.xpath('//*[@id="weatherChart"]/div[2]/p[5]')[0]   #通过xpath爬取降雨量数据
    city[a-1] = city_list.text  #存入城市列表
    rain[a-1] = re.findall(r"\d+\.?\d*",rain_list.text)[0] #存入数值



for a in range(5,10):      #非直辖一位数字网址数据
    url_a= f'http://www.weather.com.cn/weather1dn/1010{a}0101.shtml'
    driver.get(url_a)

    rain_list = []
    city_list = []
    resp_text = driver.page_source
    page_html = etree.HTML(resp_text)

    city_list = page_html.xpath('/html/body/div[4]/div[2]/a')[0]    #通过xpath爬取城市名称
    rain_list = page_html.xpath('//*[@id="weatherChart"]/div[2]/p[5]')[0]   #通过xpath爬取降雨量数据
    city[a-1] = city_list.text  #存入城市列表
    rain[a-1] = re.findall(r"\d+\.?\d*",rain_list.text)[0] #存入数值


for a in range(10,35):      #非直辖二位数字网址数据
    url_a= f'http://www.weather.com.cn/weather1dn/101{a}0101.shtml'
    driver.get(url_a)

    rain_list = []
    city_list = []
    resp_text = driver.page_source
    page_html = etree.HTML(resp_text)

    city_list = page_html.xpath('/html/body/div[4]/div[2]/a')[0]    #通过xpath爬取城市名称
    rain_list = page_html.xpath('//*[@id="weatherChart"]/div[2]/p[5]')[0]   #通过xpath爬取降雨量数据
    city[a-1] = city_list.text  #存入城市列表
    rain[a-1] = re.findall(r"\d+\.?\d*",rain_list.text)[0] #存入数值

# print(bubble_sort(rain))    #打印从大到小排序后的降水量顺序

if len(rain)%2 == 0:        #寻找中值
    medium = int(len(rain)/2)
else:
    medium = int(len(rain)/2)+1
medium_text = "中位值：" + rain[medium]

d = dict(zip(city,rain))  #将城市和降水量的列表合成为字典

rain_item = []
city_min = []
city_max = []

for k,v in d.items():
    rain_item.append(float(v))

average_rain = sum(rain_item)/len(rain_item)
average_text = "平均值："+ str(average_rain)

max_rain = max(rain_item)  #最大值
min_rain = min(rain_item)  #最小值

for k,v in d.items():
    if float(v) == min_rain:
        city_min.append(k)

min_text = "降雨量最小的城市："+str(city_min)+" 最小值："+str(min_rain)

for k,v in d.items():
    if float(v) ==max_rain:
        city_max.append(k)
max_text = "降雨量最大的城市："+str(city_max)+" 最大值："+str(max_rain)

plt.bar(range(len(d)), rain_item, align='center')
plt.xticks(range(len(d)), list(d.keys()))
plt.xlabel('城市',fontsize=20)
plt.ylabel('降水量',fontsize=20)
plt.text(0,12,average_text,fontsize=6)
plt.text(0,13,medium_text,fontsize=6)
plt.text(0,14,max_text,fontsize=6)
plt.text(0,15,min_text,fontsize=6)

plt.show()

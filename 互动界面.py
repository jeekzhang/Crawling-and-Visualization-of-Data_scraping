#-*- codeing = utf-8 -*-
from lxml import etree
from selenium import webdriver
import re
import matplotlib
matplotlib.rc("font",family='YouYuan')
from tkinter import *
import tkinter as tk


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


d = dict(zip(city,rain))  #将城市和降水量的列表合成为字典

root=tk.Tk()
root.title('降水量查询')
root.geometry('500x200')

def get():
    values = entry.get()
    for k,v in d.items():
        if k == values:
            label = Label(root, text= v+'mm')
            label.pack()

frame = Frame(root)
frame.pack()
u1 = tk.StringVar()
entry = tk.Entry(frame, width=20, textvariable=u1,  relief="sunken")
entry.pack(side="left")

frame1 = Frame(root)
frame1.pack()
btn1=Button(frame1, text="查询", width=20, height=1, relief=GROOVE, command=lambda :get())
btn1.pack(side="left")

root.mainloop()

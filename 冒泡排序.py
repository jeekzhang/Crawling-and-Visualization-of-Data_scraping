import xlrd as xd

def bubble_sort(list_1):              #冒泡排序
    for j in range(len(list_1)):
        for i in range(len(list_1)-1):
            if list_1[i]<list_1[i+1]:
                k = list_1[i]
                list_1[i] = list_1[i+1]
                list_1[i+1] = k
    return list_1

data =xd.open_workbook (r"C:\Users\14588\Documents\Tencent Files\1458836984\FileRecv\MobileFile\2019.xls")     #打开excel表所在路径
sheet = data.sheet_by_name('Sheet1')  #读取数据，以excel表名来打开
d = []
for r in range(sheet.nrows):          #将表中数据按行逐步添加到列表中，最后转换为list结构
    data1 = []
    for c in range(2,3):              #读取第三列数据
        data1.append(sheet.cell_value(r,c))
    d.append(list(data1))

print(d)                              #打印原始数据
print(bubble_sort(d))                 #打印排序后数据

import wget
import pandas as pd
import bs4
import requests
import os
import csv


def read_data():
    #到文件夹的连接
    link = "http://localhost:8000/"
    #文件储存路径
    dir = 'G:/TE/TE_Project_V1.0/data'
    try:
        contents = requests.get(link)
    except:
        print('连接失败')
        return None

    soup = bs4.BeautifulSoup(contents.text)
    lis = soup.select('li')
    filename = lis[0].text
    #判断是否已经存在
    if os.path.exists(os.path.join('G:/TE/TE_Project_V1.0/data',filename)):
        print('有了')
    else:
        print('还没')
        #download到本地
        wget.download(link + "/" + filename,out='G:/TE/TE_Project_V1.0/data')

    dat = jointDataFrame(os.path.join(dir,filename))
    #读取相关数据
    progarmTime = dat.iloc[2, 1]
    progarmData = dat.iloc[11:, 6:11]
    progarmData.reset_index(drop=True, inplace=True)  # 重设索引
    progarmData.columns = ['position', 'force', 'analog', 'time', 'speed']

    total_data = {
            'filename':filename,
            'time':progarmTime,
            'data':progarmData
        }

    return total_data


def jointDataFrame(dir):
    data = []
    with open(dir) as file:
        reader = csv.reader(file)
        for x in reader:
            data.append(x)
        # for line in file:
        #     data.append(list(line.strip().split(',')))
    dataset = pd.DataFrame(data)

    return dataset

def get_latest_filename():
    pass


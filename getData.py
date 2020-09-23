import wget
import pandas as pd
import bs4


# link = "http://localhost:12345/wenjianceshi"
# contents = requests.get(link)
# soup = bs4.BeautifulSoup(contents.text)
# lis = soup.select('li')
# filename = lis[0].text
# wget.download(link+'/'+filename,'ceshide.csv')
dat = pd.read_csv('ceshide (1).csv')
progarmTime = dat.iloc[1,1]
progarmData = dat.iloc[11:,6:11]
progarmData.reset_index(drop=True,inplace=True)     #重设索引
progarmData.columns = ['Position','Force','Analog','Time','Speed']
print(progarmData)


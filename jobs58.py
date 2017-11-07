import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    r = requests.get(url, headers = headers)
    r.encoding = r.apparent_encoding
    return r.text

def get_url(city, work_type, page=1):
    url = 'http://'+city+'.58.com/job/pn'+str(page)+'/?key='+work_type+'&final=1&jump=1'
    return url

def next_page():
    global page
    page = page + 1
    return page


url = get_url('gz', '数据分析')
soup = BeautifulSoup(get_html(url), 'html.parser')
jobInfo = soup.find('div',{'class':'item_con job_title'})
print(jobInfo)
job_url = jobInfo.a['href']#职位的详细页面
print(job_url)
address = jobInfo.find('span', {'class':'address'}).string
print(address)

#page=1
#for i in range(10):
#    url = get_url('gz', '数据分析', page)
#    next_page()
#    print(url)






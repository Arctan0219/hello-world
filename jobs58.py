import requests
import csv
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
#print(jobInfo)
job_url = jobInfo.a['href']#职位的详细页面
#print(job_url)
#address = jobInfo.find('span', {'class':'address'}).string
#print(address.split()[0])
job_soup = BeautifulSoup(get_html(job_url), 'html.parser')

job_title = job_soup.find('span', {'class':'pos_title'}).string#招聘的职位
job_name = job_soup.find('span', {'class':'pos_name'}).string
job_salary = job_soup.find('span', {'class':'pos_salary'}).get_text()#薪酬
job_welfare = job_soup.find('div', {'class':'pos_welfare'}).get_text()#福利
#print(job_welfare)
job_Con = job_soup.find('div', {'class':'rightCon'}).get_text().split()[0]#单位名称
#print(job_Con)
job_address = job_soup.find('div',{'class':'pos-area'}).find('span',{'class':None}).string#地址
#print(job_title, job_name, job_salary, job_address)
job_Des = job_soup.find('div', {'class':'des'}).get_text()#职位描述****编码问题
#print(job_Des)


with open('job.csv', 'a') as c:
    fieldnames = ['单位', '职位', '薪酬', '福利', '地址', '职位描述']
    writer = csv.DictWriter(c, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerow({'单位': job_Con, '职位': job_title, '薪酬': job_salary,
                     '福利': job_welfare, '地址': job_address, '职位描述': job_Des})













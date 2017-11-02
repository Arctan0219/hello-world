# -*- coding: utf-8 -*-
#爬取煎蛋网段子区指定前多少页的段子
import urllib.request
import re

def get_html(url):#输入地址得到该页面的html
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
	response = urllib.request.urlopen(req)
	return response.read().decode('utf8','ignore')#.encode('gbk','ignore')

	
def get_text(html):#输入html得到该页面的文本
	num = html.count('</a></span><p>') #该网页中段子的个数
	a, b = 0, 0
	text = ''
	for _ in range(num):	
		html = html[a+b:]
		a = html.find('</a></span><p>') + len('</a></span><p>')
		b = html[a:].find('</p>')
		text = text + html[a:a+b] + '\n'*5
	return text


def get_page(html):#获取当前页面的页码
	a = html.find('current-comment-page">[') + len('current-comment-page">[')
	b = html[a:].find(']</span>')
	return html[a:a+b]
	
def save_file(file_name, text):
	f = open(file_name, 'a', encoding='utf-8')
	f.write(text)
	f.close()

def main(num):
	url = "http://jandan.net/duan"
	html = get_html(url)
	page = get_page(html)
	page = int(page)#将页码转换为int类型
	for i in range(num):
		current_page = page - i
		current_url = url + '/page-' + str(current_page) + '#comments'#利用拼接的url实现翻页的效果
		html = get_html(current_url)
		text = get_text(html)
		r = '<[\w\s/]*>'
		text = re.sub(r, '', text)#除去文本中的一些乱码
		save_file('duanzi.txt', text)

if __name__ == '__main__':
	num = int(input('请输入需要下载多少页段子：'))
	main(num)
# 处理分页
# base_url 是带有分页参数的URL。
# scrape_quotes 函数遍历指定的页码范围，从start_page到end_page。
# 增加异常处理
# 使用try-except捕获并处理网络请求的异常，防止程序因请求错误而崩溃。
# 捕获requests.exceptions.RequestException以处理各种网络请求异常。
# 捕获通用的Exception来处理其他可能的错误。
# 多线程爬取
# 使用threading.Thread创建多个线程，每个线程负责爬取一个页面。
# 使用线程锁lock来确保多线程环境下文件写操作的安全性。
# 控制线程数量：num_threads参数限制同时运行的线程数量，避免过多线程导致系统资源耗尽。
# import requests
# from bs4 import BeautifulSoup
# import csv
# import threading
# import time
#
# # 基础URL
# base_url = "http://quotes.toscrape.com/page/{}/"
#
# # 定义一个线程锁
# lock = threading.Lock()
# # 函数：爬取单个页面数据
# def scrape_page(page_number):
#     url = base_url.format(page_number)
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # 如果请求失败则抛出异常
#         response.encoding = 'utf-8'
#
#         soup = BeautifulSoup(response.text, 'html.parser')
#         quotes = soup.find_all('div', class_='quote')
#
#         # 使用锁来防止多个线程同时写入CSV文件
#         with lock:
#             with open('quotes.csv', 'a', newline='', encoding='utf-8') as csvfile:
#                 writer = csv.writer(csvfile)
#                 for quote in quotes:
#                     text = quote.find('span', class_='text').get_text()
#                     author = quote.find('small', class_='author').get_text()
#                     tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
#                     writer.writerow([text, author, ', '.join(tags)])
#
#         print(f"第 {page_number} 页爬取完成")
#
#     except requests.exceptions.RequestException as e:
#         print(f"请求第 {page_number} 页时出现问题：{e}")
#     except Exception as e:
#         print(f"处理第 {page_number} 页数据时出现问题：{e}")
# # 函数：启动多线程爬取
# def scrape_quotes(start_page, end_page, num_threads=5):
#     # 先清空CSV文件并写入表头
#     with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['quote', 'author', 'tags'])
#
#     threads = []
#     for page_number in range(start_page, end_page + 1):
#         # 为每个页面启动一个线程
#         thread = threading.Thread(target=scrape_page, args=(page_number,))
#         threads.append(thread)
#         thread.start()
#
#         # 控制线程数量，防止过多线程导致资源耗尽
#         if len(threads) >= num_threads:
#             for thread in threads:
#                 thread.join()
#             threads = []
#
#     # 确保所有线程都完成
#     for thread in threads:
#         thread.join()
#
#
# if __name__ == "__main__":
#     start_time = time.time()
#     # 设置要爬取的页面范围
#     start_page = 1
#     end_page = 10  # 根据实际需要调整范围
#     # 启动爬虫
#     scrape_quotes(start_page, end_page, num_threads=5)
#     end_time = time.time()
#     print(f"爬取完成，耗时 {end_time - start_time:.2f} 秒")


# 首先，我们导入了需要用到的三个Python模块：requests、lxml和csv。
# 然后，我们定义了豆瓣电影TOP250页面的URL地址，并使用getSource(url)
# 函数获取网页源码。
# 接着，我们定义了一个getEveryItem(source)
# 函数，它使用XPath表达式从HTML源码中提取出每部电影的标题、URL、评分和引言，并将这些信息存储到一个字典中，最后将所有电影的字典存储到一个列表中并返回。
# 然后，我们定义了一个writeData(movieList)
# 函数，它使用csv库的DictWriter类创建一个CSV写入对象，然后将电影信息列表逐行写入CSV文件。
# 最后，在if__name__ == '__main__'
# 语句块中，我们定义了一个空的电影信息列表movieList，然后循环遍历前10页豆瓣电影TOP250页面，分别抓取每一页的网页源码，并使用getEveryItem()
# 函数解析出电影信息并存储到movieList中，最后使用writeData()
# 函数将电影信息写入CSV文件。
import requests

# from lxml import etree
# import csv
# doubanUrl = 'https://movie.douban.com/top250?start={}&filter='
#
# # 然后定义了豆瓣电影TOP250页面的URL地址，并实现了一个函数getSource(url)来获取网页的源码。该函数发送HTTP请求，添加了请求头信息以防止被网站识别为爬虫，并通过requests.get()方法获取网页源码。
# def getSource(url):
#     # 反爬 填写headers请求头
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
#     }
#     response = requests.get(url, headers=headers)
#     # 防止出现乱码
#     response.encoding = 'utf-8'
#     print(response.text)
#     return response.text
# # 定义了一个函数getEveryItem(source)来解析每个电影的信息。首先，使用lxml库的etree模块将源码转换为HTML元素对象。然后，使用XPath表达式定位到包含电影信息的每个HTML元素。通过对每个元素进行XPath查询，提取出电影的标题、副标题、URL、评分和引言等信息。最后，将这些信息存储在一个字典中，并将所有电影的字典存储在一个列表中。
# def getEveryItem(source):
#     html_element = etree.HTML(source)
#     movieItemList = html_element.xpath('//div[@class="info"]')
#     # 定义一个空的列表
#     movieList = []
#     for eachMoive in movieItemList:
#
#         # 创建一个字典 像列表中存储数据[{电影一},{电影二}......]
#         movieDict = {}
#
#         title = eachMoive.xpath('div[@class="hd"]/a/span[@class="title"]/text()')  # 标题
#         otherTitle = eachMoive.xpath('div[@class="hd"]/a/span[@class="other"]/text()')  # 副标题
#         link = eachMoive.xpath('div[@class="hd"]/a/@href')[0]  # url
#         star = eachMoive.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')[0]  # 评分
#         quote = eachMoive.xpath('div[@class="bd"]/p[@class="quote"]/span/text()')  # 引言（名句）
#
#         if quote:
#             quote = quote[0]
#         else:
#             quote = ''
#         # 保存数据
#         movieDict['title'] = ''.join(title + otherTitle)
#         movieDict['url'] = link
#         movieDict['star'] = star
#         movieDict['quote'] = quote
#         movieList.append(movieDict)
#         print(movieList)
#     return movieList
#
#
# # 保存数据
# def writeData(movieList):
#     with open('douban.csv', 'w', encoding='utf-8', newline='') as f:
#         writer = csv.DictWriter(f, fieldnames=['title', 'star', 'quote', 'url'])
#
#         writer.writeheader()  # 写入表头
#
#         for each in movieList:
#             writer.writerow(each)
# if __name__ == '__main__':
#     movieList = []
#     # 一共有10页
#     for i in range(10):
#         pageLink = doubanUrl.format(i * 25)
#         source = getSource(pageLink)
#         movieList += getEveryItem(source)
#
#     writeData(movieList)

# 导入了必要的模块requests和os
import requests
import os

# 定义了一个函数get_html(url)，
# 用于发送GET请求获取指定URL的响应数据。函数中设置了请求头部信息，
# 以模拟浏览器的请求。函数返回响应数据的JSON格式内容
def get_html(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    response = requests.get(url=url, headers=header)
    # print(response.json())
    html = response.json()
    return html

# 定义了一个函数parse_html(html)，
# 用于解析响应数据中的图片信息。通过分析响应数据的结构，
# 提取出每个图片的URL和标题，并将其存储在一个字典中，然后将所有字典组成的列表返回
def parse_html(html):
    rl_list = html['data']['rl']
    print(rl_list)
    img_info_list = []
    for rl in rl_list:
        img_info = {}
        img_info['img_url'] = rl['rs1']
        img_info['title'] = rl['nn']
        # print(img_url)
        # exit()
        img_info_list.append(img_info)
    # print(img_info_list)
    return img_info_list

# 定义了一个函数save_to_images(img_info_list)，用于保存图片到本地。
# 首先创建一个目录"directory"，如果目录不存在的话。然后遍历图片信息列表，
# 依次下载每个图片并保存到目录中，图片的文件名为标题加上".jpg"后缀。
def save_to_images(img_info_list):
    dir_path = 'directory'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    for img_info in img_info_list:
        img_path = os.path.join(dir_path, img_info['title'] + '.jpg')
        res = requests.get(img_info['img_url'])
        res_img = res.content
        with open(img_path, 'wb') as f:
            f.write(res_img)
        # exit()

# 在主程序中，设置了要爬取的URL，并调用前面定义的函数来执行爬取、解析和保存操作。
if __name__ == '__main__':
    url = 'https://www.douyu.com/gapi/rknc/directory/yzRec/1'
    html = get_html(url)
    img_info_list = parse_html(html)
    save_to_images(img_info_list)
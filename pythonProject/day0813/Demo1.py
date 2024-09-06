import requests
from bs4 import BeautifulSoup

# 目标网页url
url = ('https://www.bilibili.com')

# 发起HTTP请求，获取网页内容
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(url, headers=headers)
# 检查请求是否成功
if response.status_code == 200:
    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')
    # 查找所有<a>标签
    for link in soup.find_all('a'):
        # 获取并输出链接地址href属性）
        print(link.get('href'))
else:
    print(f"请求失败，状态码：{response.status_code}")
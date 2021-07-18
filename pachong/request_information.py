import requests
import json


# 第一步：指定url
# 第二步：发起请求
# 第三步：获取响应数据
# 第四步：持久化存储
# 如何获取浏览器的User-Agent:
#     在浏览器中搜索网页：chrome://version/
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    }
def request_sogou():
    url = 'https://www.sogou.com/web'

    key_word = input('输入一个关键字：')
    param = {
        'query': key_word
    }
    response = requests.get(url=url, params=param, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    print(page_text)
    with open('./baidu.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束')

def request_baidufanyi():
    post_url = 'https://fanyi.baidu.com/sug'
    key_word = input('请输入一个关键字：')
    data = {
        'kw' : key_word
    }
    response = requests.post(url=post_url,data = data,headers = headers)
    response.encoding = 'utf-8'
    response_dict = response.json()
    print(response_dict)
#   持久化存储
    file_name = key_word + '.json'
    with open(file_name,'w',encoding='utf-8') as fp:
        json.dump(response_dict,fp)

def request_doubanmovie():
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type':'12',
        'interval_id':'100:90',
        'action': '',
        'start': '1',
        'limit': '20'
    }
    response = requests.get(url=url,params=param,headers=headers)
    data_list = response.json()
    print(data_list)

    file_name = '.\douban.json'
    with open(file_name,'w') as fp:
        json.dump(data_list,fp,ensure_ascii=False)
    print('爬虫结束')


def request_zhenhua():
    url = 'https://cn.zpmc.com/party/cont.aspx'
    param = {
        'id': '1070'
    }
    reponse = requests.get(url=url,params=param,headers = headers)
    reponse.encoding = 'utf-8'
    reponse_text = reponse.text
    print(reponse_text)
    file_name = param['id'] + '.html'
    with open(file_name,'w') as fp:
        fp.write(reponse_text)

def zhengzebiaoge():
    pass







if __name__ == '__main__':
    request_zhenhua()
    pass


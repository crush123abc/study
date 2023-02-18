import uuid
import faker
import requests
import random
import time
import json
uri = 'http://106.55.186.222'
fk=faker.Faker(locale='zh-CN')


def add_interface(index):
    url = uri + '/path/interface/'
    headers = {'Content-Type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    request_type = random.choice(['post', 'get', 'delete', 'put'])
    data = {"name": f'测试{fk.date()}{index}'[:20],
            "describe": f'测试_接口描述{fk.address()}',
            "type": request_type,
            "uri": "1231",
            "path": fk.uri_path(),
            "body": f'{fk.company()}' if request_type == 'post' or request_type == 'put' else ''
            }
    result = requests.request(method='post', url=url, headers=headers, json=data)
    # print(result.text)
    # print(result.status_code)
    if result.status_code != 200 and result.status_code != 201:
        raise Exception(f'响应code异常：{result.status_code},code响应体：{result.text}')

    # if result.json().get('code')!='0':
    #     raise Exception(f'响应体异常：{result.text}')
    return result.json()

def delete_interface(id):
    url=uri+f'/path/interface/{id}/'
    headers={'Content-Type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    result = requests.request(method='delete', url=url, headers=headers)
    if result.status_code != 204:
        raise Exception(f'响应code异常：{result.status_code},code响应体：{result.text}')
def select_interface():
    url=uri+f'/path/interface/'
    headers = {'Content-Type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    result = requests.request(method='get', url=url, headers=headers)
    if result.status_code != 200 and result.status_code != 201:
        raise Exception(f'响应code异常：{result.status_code},code响应体：{result.text}')
    return result.json()



if __name__ == '__main__':
    ##删除数据
    # while True:
    #     s=select_interface()
    #     print(s)
    #     if not s.get('results'):
    #         break
    #     for i in s.get('results'):
    #         id = i.get('id')
    #         delete_interface(id)

    ##随机取请求类型
    # x=random.choice(['post','get','delete','put'])

    # print(x)
    # print(add())
    # x=json.loads(fk.profile())
    # x=str(fk.profile())
    # print(type(x))
    # print(x)

    ##增加数据
    # for i in range(200):
    #     add_interface(i)
    #     print(i)

    # add()
    # print(time.time())
    # time.sleep(1)
    # print(time.time())
    # print(str(uuid.uuid1())[:20])

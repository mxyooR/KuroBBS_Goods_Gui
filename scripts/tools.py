import json
import os
import global_vars
from datetime import datetime

# 获取当前文件的绝对路径
base_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(base_dir)
goodslist_path = os.path.join(parent_dir, 'goodslist.json')
config_path = os.path.join(parent_dir, 'config.json')
tasklistpath = os.path.join(parent_dir, 'tasklist.json')




def convert_timestamp_to_string(timestamp_ms:int):
    """
    转化时间戳为字符串
    """
    dt_object = datetime.fromtimestamp(timestamp_ms / 1000)
    formatted_date = dt_object.strftime('%Y-%m-%dT%H:%M:%S')
    return formatted_date





def add_to_wishlist(commodityCode, saleTime, commodityName, gameId):
    """
    将商品添加到备选清单中
    """
    try:
        with open(goodslist_path, 'r', encoding='utf-8') as f:
            goods_list = json.load(f)
            print(goods_list)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Failed to read goodslist.json")
        goods_list = []

    # 添加新商品到备选清单
    new_item = {
        "commodityName": commodityName,
        "commodityCode": commodityCode,
        "saleTime": saleTime,
        "gameId":gameId
    }
    goods_list.append(new_item)

    # 写入goodslist.json文件
    with open(goodslist_path, 'w', encoding='utf-8') as f:
        json.dump(goods_list, f, ensure_ascii=False, indent=4)


def clear_goodslist():
    with open(goodslist_path, 'w') as file:
        file.write('')

def clear_tasklist():
    with open(tasklistpath, 'w') as file:
        file.write('')


def format_cookie_string(cookie):
    return '; '.join([f"{key}={value}" for key, value in cookie.items()])



def add_to_tasklist(commodityCode:str,address:dict,gameId:str,time:str,name:str,count:int):
    """
    将任务添加到任务清单中
    """

    payload = {
        "commodityCode": commodityCode,
        "commodityNum": "1",
        "geeTestData": {}, # 该字段先空着 到兑换前再填
        "province": address["province"],
        "city": address["city"],
        "area": address["district"],
        "detail": address["fullAddress"],
        "mobile": int(address["tel"]),
        "receiver": address["name"],
        "gameId": gameId
    }
    headers = {
        "devcode":  global_vars.devcode,
        "ip": "219.142.99.8",
        "source": "android",
        "version": "2.2.1",
        "versioncode": "2210",
        "token": global_vars.token,
        "osversion": "Android",
        "distinct_id": global_vars.distinct_id,
        "countrycode": "CN",
        "model": "2203121C",
        "lang": "zh-Hans",
        "channelid": "2",
        "content-type": "application/x-www-form-urlencoded",
        "accept-encoding": "gzip",
        "cookie": "user_token="+global_vars.token,
        "user-agent": "okhttp/3.11.0"
    }
    #生成格式
    task = {
        "name": name,
        "payload": payload,
        "headers": headers,
        "time": time,
        "count":count
    }
    try:
        with open(tasklistpath, 'r', encoding='utf-8') as file:
            tasklist = json.load(file)
    except Exception as e:
        tasklist = []
        print(f"Failed to read tasklist.json: {str(e)}")

    # Append the new task to the tasklist
    tasklist.append(task)

    # Save the updated tasklist back to tasklist.json
    with open(tasklistpath, 'w', encoding='utf-8') as file:
        json.dump(tasklist, file, ensure_ascii=False, indent=4)

    return tasklist


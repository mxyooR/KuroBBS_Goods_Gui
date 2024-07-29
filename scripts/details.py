import requests
from .log import log_message


def get_goods_list(gameId:int,headers:dict)->dict:
    url="https://api.kurobbs.com/encourage/commodity/list"
    data={
        "gameId":gameId,
        "pageIndex":1,
        "pageSize":20
    }
    try:
        response=requests.post(url,headers=headers,data=data)
        res=response.json()
        return res["data"]["commodityList"]
    except Exception as e:
        log_message(f"获取商品列表失败:{e}")
        return None



def get_accesstooken_by_token(headers:dict):
    url="https://api.kurobbs.com/encourage/order/beforeCreate"
    res=requests.post(url,headers=headers)
    try:
        access_token=res.json()["data"]["permitToken"]
        return access_token
    except Exception as e:
        log_message(f"获取access_token失败:{res.json()}")
        return None

    



def get_address_by_accesstoken(access_token):
    url="https://user-zone-api.kurogame.com/logistics/delivery-address/list.lg"
    headers={
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "accesstoken": access_token,
        "kr-ver": "1.1.0",
        "accept-language": "zh-Hans,zh-CN,en-US",
        
        "user-agent": "Mozilla/5.0 (Linux; Android 9; 2203121C Build/PQ3A.190605.06171613; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 Kuro/2.2.2 KuroGameBox/2.2.2",
        
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "accept": "*/*",
        "origin": "https://web-static.kurobbs.com",
        "x-requested-with": "com.kurogame.kjq",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://web-static.kurobbs.com/",
        "accept-encoding": "gzip, deflate"
  }
    res=requests.get(url,headers=headers)
    try:
        address=res.json()["data"]
        log_message("成功获取地址:")
        return address
    except Exception as e:
        log_message(f"get address failed{e}")
        return None
    

    

def get_total_gold(headers:dict):
    url="https://api.kurobbs.com/encourage/gold/getTotalGold"
    res=requests.post(url,headers=headers)
    try:
        gold=res.json()["data"]["goldNum"]
        log_message(f"成功获取总金币数:{gold}")
        return gold
    except Exception as e:
        log_message(f"获取总金币数失败:{res.json()}")
        return None
    

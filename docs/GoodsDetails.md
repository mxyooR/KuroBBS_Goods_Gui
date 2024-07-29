# 商品详情post

## 请求部分

### 基本信息
- **方法**: POST
- **URL**: `https://api.kurobbs.com/encourage/commodity/detail`
- **HTTP 版本**: HTTP/2.0

### 请求头
以下是该请求包含的请求头信息：

| 请求头字段       | 值                                                                                     |
| ---------------- | -------------------------------------------------------------------------------------- |
| `:authority`     | api.kurobbs.com                                                                        |
| `:method`        | POST                                                                                   |
| `:path`          | /encourage/commodity/detail                                                            |
| `:scheme`        | https                                                                                  |
| `devcode`        | 设备id                                                                                 |
| `ip`             | 172.16.1.45                                                                            |
| `source`         | android                                                                                |
| `version`        | 2.2.1                                                                                  |
| `versioncode`    | 2210                                                                                   |
| `token`          | 你的token |
| `osversion`      | Android                                                                                |
| `distinct_id`    | distinct_id                                                  |
| `countrycode`    | CN                                                                                     |
| `model`          | 2203121C                                                                               |
| `lang`           | zh-Hans                                                                                |
| `channelid`      | 2                                                                                      |
| `content-type`   | application/x-www-form-urlencoded                                                      |
| `content-length` | 33                                                                                     |
| `accept-encoding`| gzip                                                                                   |
| `cookie`         | user_token=   `token` |
| `user-agent`     | okhttp/3.11.0                                                                          |

### 请求体
- **MIME 类型**: application/x-www-form-urlencoded
- **内容**: `commodityCode=1255139293048791040`  商品代码

## 响应部分

### 状态信息
- **状态码**: 200
- **状态文本**: OK
- **HTTP 版本**: HTTP/2.0

### 响应头
以下是该响应包含的响应头信息：

| 响应头字段                  | 值                                |
| --------------------------- | --------------------------------- |
| `:status`                   | 200                               |
| `date`                      | Sat, 27 Jul 2024 12:56:12 GMT     |
| `content-type`              | application/json;charset=UTF-8    |
| `vary`                      | Origin                            |
| `vary`                      | Access-Control-Request-Method     |
| `vary`                      | Access-Control-Request-Headers    |
| `x-content-type-options`    | nosniff                           |
| `x-xss-protection`          | 1; mode=block                     |
| `cache-control`             | no-cache, no-store, max-age=0, must-revalidate |
| `pragma`                    | no-cache                          |
| `expires`                   | 0                                 |
| `strict-transport-security` | max-age=15724800; includeSubDomains|
| `content-length`            | 866                               |

### 响应体
- **大小**: 866 字节
- **MIME 类型**: application/json
- **内容**: 

  ```json
    {
  "code": 200,
  "data": {
    "commodityCode": "1265985188547989504",
    "commodityDesc": "商品描述：鸣潮共鸣者主题金属徽章 忌炎款\n品牌：薪火创未\n兑换限制：每个社区账号仅可兑换一次，限量兑换，兑完即止。\n发货时间：成功兑换后，预计在出货后陆续发出。\n*图片仅供参考，请以实物为准",
    "commodityLimit": 1,
    "commodityLimitStrategy": 1,
    "commodityLimitType": 1,
    "commodityName": "鸣潮共鸣者主题金属徽章 忌炎款",
    "commodityPrice": 11800,
    "commodityStatus": 0, //0可以兑换 1限制兑换 2还没开始 3已下架 4待上架
    "commodityType": 2,
    "currentUserLimitBuy": 1,
    "gameId": 3,
    "gameName": "鸣潮",
    "isSellout": false,
    "offShelveTime": 1724687999000,  //下架时间  时间戳毫秒表示
    "pictureUrl": "https://prod-alicdn-community.kurobbs.com/product/1721875981918750866.jpg",
    "saleTime": 1719763200000,
    "shelveTime": 1719763200000,
    "totalStock": 10, //总共个数
    "totalSurplusStock": 10
  },
  "msg": "请求成功",
  "success": true
    }
    

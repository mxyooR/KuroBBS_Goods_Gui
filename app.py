"""
@Author:  mxyooR
@Creation Date: 2024-07-28
@License: GPL-3.0
"""

import json
from flask import Flask, render_template, request, redirect, url_for, jsonify,send_file
from scripts import details, tools,exchange
from scripts.log import log_message,setup_logger
import os
import global_vars
import asyncio
from concurrent.futures import ThreadPoolExecutor
import webbrowser

tasks = {}
executor = ThreadPoolExecutor(max_workers=1)
app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(base_dir)
goodslist_path = os.path.join(base_dir, 'goodslist.json')
config_path = os.path.join(base_dir, 'config.json')
tasklistpath = os.path.join(base_dir, 'tasklist.json')




def set_globalvars(data):
    global_vars.token = data["token"]
    global_vars.devcode = data["devcode"]
    global_vars.distinct_id = data["distinct_id"]
    global_vars.headers = {
    "devcode": global_vars.devcode,
    "ip": tools.get_ip_address(),
    "source": "android",
    "version": "2.2.2",
    "versioncode": "2220",
    "token": global_vars.token,
    "osversion": "Android",
    "distinct_id": global_vars.distinct_id,
    "countrycode": "CN",
    "model": "2203121C",
    "lang": "zh-Hans",
    "channelid": "2",
    "content-type": "application/x-www-form-urlencoded",
    "accept-encoding": "gzip",
    "cookie": "user_token=" + global_vars.token,
    "user-agent": "okhttp/3.11.0"
    }

    global_vars.access_token = details.get_accesstooken_by_token(global_vars.headers)
    log_message(f"成功获取access_token:{global_vars.access_token}")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view_log')
def view_log():
    log_path = os.path.join(app.root_path, 'log.log')
    return send_file(log_path, mimetype='text/plain')

#####################
#获取商品列表
#####################
@app.route('/product_list', methods=['GET', 'POST'])
def product_list_view():
    if not global_vars.CorrectProfile:
        return redirect(url_for('get_user_info',alert="请先填写个人信息"))
    products = []
    golds=details.get_total_gold(global_vars.headers)
    # 如果是 POST 请求，说明用户选择了一个游戏,否则返回空列表
    if request.method == 'POST':
        selected_category = request.form.get('category')
        global_vars.gameId = selected_category
        products_list = details.get_goods_list( selected_category,global_vars.headers)
        for products in products_list:
            products['saleTime'] = tools.convert_timestamp_to_string(products['saleTime'])
        return render_template('product_list.html', products=products_list, gameId=global_vars.gameId,golds=golds)
    return render_template('product_list.html', products=[], gameId=global_vars.gameId,golds=golds)

#添加到心愿单
@app.route('/add_to_wishlist', methods=['POST'])
def add_to_wishlist():
    commodityCode = request.form.get('commodityCode')
    saleTime = request.form.get('saleTime')
    commodityName = request.form.get('commodityName')
    gameId = request.form.get('gameId')

    # 使用 tools.py 中的 add_to_wishlist 函数
    tools.add_to_wishlist(commodityCode, saleTime, commodityName, gameId)
    log_message(f"商品已经添加到备选清单:  {commodityName}")
    return jsonify({'status': 'success', 'message': '已成功添加到备选清单'})



# 删除心愿单中的商品
@app.route('/clear_wishlist', methods=['POST'])
def clear_wishlist():
    tools.clear_goodslist()
    log_message("备选清单已经清空")
    return jsonify({"message": "备选清单已经清空"}), 200

#####################
#获取个人信息
#####################

@app.route('/get_user_info', methods=['GET', 'POST'])
def get_user_info():
    if request.method == 'POST':
        devcode = request.form.get('devcode')
        distinct_id = request.form.get('distinct_id')
        token = request.form.get('token')
        data = {
            "devcode": devcode,
            "distinct_id": distinct_id,
            "token": token
        }
        with open(config_path, "w") as f:
            json.dump(data, f)
        set_globalvars(data)
        global_vars.CorrectProfile= True
        log_message("个人信息已经设置")
        return render_template('get_user_info.html', alert="个人信息已经设置")
    return render_template('get_user_info.html')




#####################
#新建任务
#####################

@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
    if request.method == 'GET':
        # 检查是否已登录
        if not global_vars.CorrectProfile:
            log_message(global_vars.CorrectProfile)
            return redirect(url_for('get_user_info', alert="请先填写个人信息"))
        # 获取地址
        addresses= details.get_address_by_accesstoken(global_vars.access_token)
        log_message(f"成功获取地址{addresses}")
        try:
            with open(goodslist_path, 'r', encoding='utf-8') as f:
                goods_list = json.load(f)
        except json.JSONDecodeError as e:
            # 处理JSON解码错误
            log_message(f"Error decoding JSON from {goodslist_path}: {e}")
            goods_list = []

        addresses.append({'id': "", 'uid': "", 'name': '', 'tel': '', 'province': '', 'city': '', 'district': '', 'fullAddress': '', 'isDefault': False, 'createTime': '', 'updateTime': '', 'area': None, 'areaCode': None, 'postCode': None})

        # 设置默认时间
        default_time = goods_list[0]['saleTime'] if goods_list else ''
        # 渲染创建任务的页面
        return render_template('create_task.html', addresses=addresses, goods_list=goods_list, default_time=default_time)
    


#新建任务清单 starttask从任务清单里面读取
@app.route('/add_to_tasklist', methods=['POST'])
def add_to_tasklist():
    

    # 从请求中获取其他参数
    commodityCode = str(request.json.get('commodityCode'))
    #address返回的是字符串，需要转换成字典
    address_str = request.json.get('address')
    address_str = address_str.replace("True", "true").replace("None", "null").replace("'", '"')
    address = json.loads(address_str)

    time = request.json.get('task_time')
    name = request.json.get('task_name')
    count = int(request.json.get('count'))
    gameId = int(request.json.get('gameId'))

    if not commodityCode or not address or not time or not name  or not count:
        log_message("Missing required parameters")
        return jsonify({'status': 'error', 'message': '请求数据缺失'}), 400

    try:
        tools.add_to_tasklist(commodityCode,address,gameId,time,name,count)
        log_message(f"Task added successfully: {name}")
        return jsonify({'status': 'success', 'message': '已成功添加到任务清单'})
    except Exception as e:
        log_message(f"Error adding task: {e}")
        return jsonify({'status': 'error', 'message': f'添加任务时发生错误: {str(e)}'}), 500


# 删除任务清单中的任务
@app.route('/clear_tasklist', methods=['POST'])
def clear_tasklist():
    tools.clear_tasklist()
    log_message("任务清单已经清空")
    return jsonify({"message": "任务清单已经清空"}), 200

#####################
#开始任务#
#####################

@app.route('/start_task', methods=['GET', 'POST'])
async def start_task():
    try:
        with open(tasklistpath, 'r', encoding='utf-8') as f:
            tasks = json.load(f)
            log_message("成功读取任务清单")
    except Exception as e:
        log_message(f"Error loading tasklist.json: {e}")
        return redirect(url_for('create_task', alert="请先创建任务清单"))

    return render_template('start_task.html', tasks=tasks, current_time=await exchange.get_ntp_time(),task_running=global_vars.task_running)

@app.route('/get_current_time')
async def get_current_time():
    ntp_time = await exchange.get_ntp_time()
    if ntp_time is not None:
        formatted_time = ntp_time.strftime('%Y-%m-%d %H:%M:%S')
    else:
        formatted_time = "Error fetching NTP time"
    
    return jsonify(current_time=formatted_time)

@app.route('/get_task_status', methods=['GET'])
def get_task_status():
    return jsonify(task_running=global_vars.task_running)



def run_asyncio_task(task_name,count):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(exchange.schedule_task(task_name,count))
    loop.close()

@app.route('/run_task', methods=['POST'])
def run_task():
    with open(tasklistpath, 'r', encoding="utf-8") as f:
        tasks = json.load(f)
    selected_task_time = request.form.get('task')
    selected_task = next((task for task in tasks if task['time'] == selected_task_time), None)
    
    if selected_task:
        count = selected_task.get('count', 5)  # 默认值为1，如果count不存在
        try:
            count = int(count)
        except Exception as e:
            log_message(f"Error converting count to integer: {e}")
            log_message(f"自动改成默认值count: {count}")
            count = 5
        log_message(f"任务已经开始: {selected_task.get('name')}")
        global_vars.task_running = True
        executor.submit(run_asyncio_task, selected_task, count)
        return "Task is running"
    else:
        return "Task not found", 404



@app.route('/get_task_messages', methods=['GET'])
def get_task_messages():
    # 获取并清理任务消息
    messages = exchange.task_messages.copy()
    exchange.task_messages.clear()
    return jsonify(messages=messages)

# 停止任务
@app.route('/stop_task', methods=['POST'])
def stop_task():
    global_vars.task_running = False
    messages = "任务已经停止"
    log_message(messages)
    return jsonify(messages=messages)





#####################
#程序入口
#####################
if __name__ == '__main__':
    setup_logger() 
    # 检查 goodslist.json 是否存在，不存在则创建  不然会报错
    if not os.path.exists(goodslist_path):
        with open(goodslist_path, 'w') as f:
            json.dump([], f)  
        log_message(f"goodlist不存在，已创建文件：{goodslist_path}")
    try:
        with open(config_path, "r") as f:
            data = json.load(f)
            set_globalvars(data)
            global_vars.CorrectProfile= True
    except Exception as e:
        log_message(f"读取配置文件失败:{e}")
        global_vars.CorrectProfile= False
    webbrowser.open('http://127.0.0.1:5001')
    app.run(debug=True,port=5001)
    

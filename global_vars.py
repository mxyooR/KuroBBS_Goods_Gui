#全局变量
import os
token=""
devcode=""
access_token=""
distinct_id=""
headers={}
gameId=0
CorrectProfile= False
base_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(base_dir)
goodslist_path = os.path.join(base_dir, 'goodslist.json')
config_path = os.path.join(base_dir, 'config.json')
tasklistpath = os.path.join(base_dir, 'tasklist.json')
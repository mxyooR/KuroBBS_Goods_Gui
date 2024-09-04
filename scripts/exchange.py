import httpx
import asyncio
import json
from datetime import datetime, timedelta
import ntplib
from concurrent.futures import ThreadPoolExecutor
from .log import log_message
from .captcha import get_geeTestData
import global_vars


task_messages = []


executor = ThreadPoolExecutor()

class ExchangeTask:
    def __init__(self, task):
        self.payload = task["payload"]
        self.headers = task["headers"]
        self.target_time = datetime.fromisoformat(task["time"])
        self.name = task["name"]
        self.count = task["count"]
        self.task_messages = []
        self.executor = ThreadPoolExecutor()
        self.task_running = True

    async def get_ntp_time(self):
        """
        获取NTP时间
        """
        client = ntplib.NTPClient()

        def fetch_ntp_time():
            try:
                response = client.request('ntp.aliyun.com')
                # 时区转换
                return datetime.utcfromtimestamp(response.tx_time) + timedelta(hours=8)
            except Exception as e:
                return None

        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(self.executor, fetch_ntp_time)




    async def orderbeforeCreate(headers):
        url = "https://api.kurobbs.com/encourage/order/beforeCreate"
        async with httpx.AsyncClient() as client:
            try:
                res = await client.post(url, headers=headers)
                #print(res.text)
                return None
            except Exception as e:
                log_message(f"发起order前置步骤失败:{e}")
                return None
        
    async def exchange_goods(self):
        """
        兑换商品
        """
        url = "https://api.kurobbs.com/encourage/order/create"

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, data=self.payload, headers=self.headers)
                self.task_messages.append(f"任务 {self.name}返回：{response.text}")
                log_message(f"任务 {self.name}返回：{response.text}")
            except httpx.HTTPStatusError as e:
                self.task_messages.append(f"任务 {self.name}HTTP error occurred: {e}")
                log_message(f"任务 {self.name}HTTP error occurred: {e}")
            except Exception as e:
                self.task_messages.append(f"任务 {self.name}An error occurred: {e}")
                log_message(f"任务 {self.name}An error occurred: {e}")

    async def schedule_task(self):
        """
        调度任务
        """
        tasks = [self.exchange_goods() for _ in range(self.count)]
        log_message(f"任务 {self.name} 已添加到任务清单中, 将在 {self.target_time} 执行, {tasks}")
        while self.task_running:
            ntp_time = await self.get_ntp_time()
            if ntp_time:
                self.task_messages.append(f"现在是北京时间： {ntp_time}")
                delay = (self.target_time - ntp_time).total_seconds()
                # 注意 由于日志输出使用的是电脑时间 而兑换时间使用的是ntp时间 所以日志上的时间会有所偏差
                if delay <= 60:
                    #await self.orderbeforeCreate(global_vars.headers)
                    await asyncio.sleep(delay)
                    self.payload["geeTestData"]= get_geeTestData()
                    print(self.payload)
                    print(self.headers)
                    await asyncio.gather(*tasks)
                    log_message(f"{await self.get_ntp_time()} 任务 {self.name} 已执行完成")
                    self.task_running = False
                    break
                else:
                    self.task_messages.append(f"目前还剩余 {delay} 秒. 30秒后重新校准时间")
                    await asyncio.sleep(30)
            else:
                self.task_messages.append("获取NTP时间失败. 1秒后重试")
                await asyncio.sleep(1)

# KuroBBS Goods GUI

一个基于Python、Flask(和Electron 后续可能会加)的桌面应用，用于自动兑换库街区商品。

## 写在前面
## ⚠️由于本项目处于开发阶段从理论层面开发，未实际测试过，可能会存在bug，库洛币够的用户可以试一下反馈issue

感谢你使用KuroBBS Goods GUI。由于本人能力有限，项目可能仍然存在一些bug，欢迎提交issue，也请勿将本项目用于非法用途。希望这个项目对你有所帮助，并且欢迎提出改进建议。

## Todolist

### 功能开发

- [ ] 优化ui界面
- [ ] 加release
- [ ] 增加多用户功能
- [ ] 加入获取用户信息的模块
- [x] 处理任务停止和重新开始
- [x] 增加自定义兑换时post次数的选项

### 开发文档
[GoodsDetails](/docs/GoodsDetails.md)
[Exchange](/docs/Exchange.md)



## 安装与运行

### 普通用户

- ~~直接在 release 页面下载最新版本即可~~ (还没写)。

### 开发者

#### 先决条件

- Python 
- Node.js 

#### 安装步骤

1. 克隆本仓库：

    ```bash
    git clone https://github.com/mxyooR/KuroBBS_Goods_Gui
    cd Mys_Goods_Gui
    ```

2. 安装 Python 依赖：

    ```bash

    pip install -r requirements.txt
    ```


#### 运行应用

1. 启动 Flask 后端：

    ```bash

    python app.py
    ```
    在浏览器打开 `127.0.0.1:5001`



## 参考项目

本项目参考~~CTRL+C~~了以下开源项目(反正差不多)：

- [Mys_Goods_Gui](https://github.com/mxyooR/Mys_Goods_Gui)

感谢[@Ko-Koa](https://github.com/Ko-Koa)提供的打码代码，来源[Kuro-autosignin](https://github.com/mxyooR/Kuro-autosignin)


## 注意事项

- 由于日志输出使用的是电脑时间，而兑换时间使用的是 NTP 时间，所以日志上的时间会有所偏差。
- 请到库街区app内把要收货的地址设置成默认地址(最好)

## 免责声明

- 本 KuroBBS Goods GUI 程序（以下简称“程序”）由用户编写，仅供学习和研究目的使用。在使用本程序前，请仔细阅读以下免责声明：

1. **使用风险**  
   使用本程序的风险由用户自行承担。程序的开发者不对因使用或无法使用本程序而产生的任何直接或间接损失承担任何责任。

2. **合法性**  
   用户在使用本程序时应遵守相关法律法规及服务提供商的使用条款。程序的开发者不对用户因使用本程序而违反任何法律法规或服务条款承担责任。

3. **责任限制**  
   在适用法律允许的最大范围内，程序的开发者不对因使用或无法使用本程序而导致的任何损害承担责任，包括但不限于利润损失、数据丢失或业务中断等。

通过下载、安装或使用本程序，用户即表示已阅读、理解并同意本免责声明的所有条款。如果用户不同意本免责声明中的任何条款，请不要使用本程序。
同意本免责声明的所有条款。如果用户不同意本免责声明中的任何条款，请不要使用本程序。
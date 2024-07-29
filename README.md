
# KuroBBS Goods GUI

一个基于Python、Flask(和Electron 后续可能会加)的桌面应用，用于自动兑换库街区商品。

## 写在前面
## 由于本项目处于开发阶段从理论层面开发，未实际测试过，可能会存在bug，库洛币够的用户可以试一下反馈issue

感谢你使用KuroBBS Goods GUI。本项目旨在帮助用户自动兑换库街区商品，提高兑换效率。由于本人能力有限，项目可能仍然存在一些bug，欢迎提交issue，也请勿将本项目用于非法用途。希望这个项目对你有所帮助，并且欢迎提出改进建议。

## Todolist

### 功能开发

- [ ] 优化ui界面
- [ ] 加release
- [ ] 增加多用户功能
- [x] 处理任务停止和重新开始
- [x] 增加自定义兑换时post次数的选项

### 开发文档
[GoodsDetails](/docs/GoodsDetails.md)
[Exchange] (还没写)



## 安装与运行

### 普通用户

- ~~ 直接在 release 页面下载最新版本即可~~ (还没写)。

### 开发者

#### 先决条件

- Python 
- Node.js 

#### 安装步骤

1. 克隆本仓库：

    ```bash
    git clone https://github.com/mxyooR/Mys_Goods_Gui
    cd Mys_Goods_Gui
    ```

2. 安装 Python 依赖：

    ```bash
    cd flask_app
    pip install -r requirements.txt
    ```

3. 安装 Electron 依赖：

    ```bash
    cd ..
    npm install
    ```

#### 运行应用

1. 启动 Flask 后端：

    ```bash
    cd flask_app
    python app.py
    ```
    若无需 Electron，可直接在浏览器打开 `127.0.0.1:5000`

2. 启动 Electron 前端：

    ```bash
    cd ..
    npm start
    ```

## 参考项目

本项目参考~~ ctrl+c~~ 了以下开源项目(反正差不多)：

- [Mys_Goods_Gui](https://github.com/mxyooR/Mys_Goods_Gui)

## 注意事项

- 本项目仅供学习使用，请勿用于非法用途。
- 由于日志输出使用的是电脑时间，而兑换时间使用的是 NTP 时间，所以日志上的时间会有所偏差。


# ListenShutdow
局域网内实现使用ios对电脑进行遥控关机

# 原理：
    通过启动一个服务端口12345，进行监听请求。当接收请求，执行关机命令

# 步骤
1、安装打包工具
```
pip install pyinstaller
```
2、打包
```
pyinstaller --onefile --noconsole -n shutdown_service index.py
```
--onefile：生成单个独立的可执行文件。
--noconsole：禁用控制台窗口的显示。
3、设置开机执行
    有多种方式，比价简单的为：win+R 输入shell:startUp,然后对打包好的exe创建快捷方式，将快捷方式放入到shell:startUp打开的目录下就行。

# 如何使用：
    1、查看需要关机的目标的ip（安装本exe的电脑）。
    2、连上局域网，然后发起get请求：http://[ip]:12345/shutdown  即可关机

## ios使用快捷指令方式：
    1. 打开快捷指令
    2. 点击右上角：添加
    3. 点击：添加操作
    4. 点击：网页
    5. 点击：获取URL内容
    6. 然后将URL替换为上方的get请求地址即可。
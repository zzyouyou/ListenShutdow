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
# LusPic
Online image storage for [personal blog](https://blog.luspock.com)

## 修改记录
* 添加Qt界面
* 可以修改上传的Url地址，提高安全

## 安装
分别为服务器和客户端建立python虚拟环境，安装Server和Client下的requirements.txt
## 配置

### 服务器端

1. 修改db_init.py 中用户名及密码
2. 运行db_init.py 生成数据库文件
3. 修改server.py 中SECRET_KEY和UPLOAD_URL
4. 运行server.py （可能需要nginx与uwsgi或者其他工具）

### 客户端

1. 修改config.py中用户名和密码，要与服务器端一致
2. 修改config.py中url，与你自己的域名一致，比如：
>https://pic.luspock.com
3. 修改config.py中upload_url，与服务器端一致
4. 客户端目录下运行
>PyInstaller client.py

在dist目录下找到.exe并运行。


## 参考
[MdPic](https://github.com/alinuxsa/MdPic)


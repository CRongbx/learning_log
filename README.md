# Web_learning_log
python django 项目实践学习

## 环境说明

OS：macOS Catalina 10.15

Python 3.7

Django 2.2.6

Django-bootstrap3

```bash
#安装Django
pip install Django==2.2.6
#安装bootstrap3
pip install Django-bootstrap3
```

## 如何运行

```bash
git clone https://github.com/CRongbx/web_log.git
cd web_log
```

```bash
#激活虚拟环境
source ll_env/bin/activate
#退出该虚拟环境 deavtivate

#本地运行
python manage.py runserver

```

管理员界面：

http://127.0.0.1:8000/admin

​	这里我默认创建了一个管理员账号：

	>账号：crong
	>
	>密码：crong_admin

普通用户界面：

http://127.0.0.1:8000



## 注意

runserver时可能会出现如下报错：

```bash
You have 19 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, learning_logs, sessions.
Run 'python manage.py migrate' to apply them.
```

执行如下命令后再重新runserver即可：

```bash
python manage.py migrate
```








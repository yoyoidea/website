# Website

网址导航工具， 基于html + django的后台可配置网址导航管理工具。

### 使用方法

1. clone 项目：

```bash
git clone https://github.com/yoyoidea/website.git
```
1. 在setting中修改mysql配置：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'website',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

2. 执行数据表生成命令：

```bash
python manage.py makemigrations
python manage.py migrate
```
3. 创建超级用户：

```bash
python manage.py createsuperuser
```

4. 镜像构建：

```bash
cd website
docker build -t website .
```

5. 启动项目

```bash
docker run --rm --name website -p 80:80 -d website
```

6. 请求http://127.0.0.1/admin 输入步骤3中的账号和密码添加网站信息

 ![image](https://github.com/yoyoidea/website/raw/master/managecenter/static/images/website_admin.png)

7. 最后访问http://127.0.0.1 的效果图如下：

 ![image](https://github.com/yoyoidea/website/raw/master/managecenter/static/images/website.png)
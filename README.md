# 制作可执行的 python 程序

使用 pyz.py 脚本将一个 python 程序和他的依赖打成一个可执行地 app, 使用方式:

```bash
  python pyz.py app.pyz app
```

app.pyz 是想要生成的应用文件,可以不带后缀, app 是应用的源码目录,要求 app 目录下存在 \_\_main\_\_.py 文件

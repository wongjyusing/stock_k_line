# stock_k_line
历史数据已成功，现在学习实时绘制K图
# 必要的包
`pip install bs4 lxml tushare tornado `  
# 启动
在当前目录下，`python server.py`  

# 文件介绍

```tree
├── applications.py    # 应用文件，可填写数据库连接等方法
├── config.py          # 项目配置，端口号debug等都在里面定义
├── README.md          # 说明书
├── server.py          # 项目启动文件
├── static             # 静态文件目录
│   ├── css
│   ├── data
│   │   ├── detail.json
│   │   └── ok.json
│   └── js
├── templates          # 模板文件目录
│   ├── home.html      # 首页（未完成）
│   ├── range.html        # 范围选择器
│   ├── range_k_line.html # k线数据（未完成）
│   └── test.html         
├── test.py             # 测试文件 后期会整合到项目启动中，用于获取股票详细数据
├── urls.py             # 路由文件
└── views               #  视图目录
    ├── index.py        # 暂时集中写成一个文件，后期分离
    ├── __init__.py     # 声明该目录是一个python包


```

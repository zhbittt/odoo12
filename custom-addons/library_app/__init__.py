from . import models
from . import controllers
"""
    'name': 'Library Management', # 必填 插件模块标题字符串
    'description': 'Manage library book catalogue and lending.', # 功能描述长文件，通常为RST格式
    'author': 'minwen', # 作者姓名，本处为一个字符串，可以是逗号分隔的一系列姓名
    'depends': ['base'], # 一个依赖插件模块列表，在模块安装时会先安装这些插件
    'application': True, # 一个布尔型标记，代表模块是否在应用列表中以 app 展现
    # summary：显示为模块副标题的字符串
    # version: 建议在模块版本号前加上 Odoo 版本，如12.0.1.0
    # license:：默认为LGPL-3
    # website：了解模块更多信息的 URL，可以帮助人们查看更多文档或提供文件 bug 和建议的跟踪
    # category:：带有模块功能性分类字符串，缺省为Uncategorized。
    # 已有分类可通过安全组表单（位于Settings > Users & Companies > Groups）
    # 的 Application字段下拉列表查看（需开启调试模式）
"""
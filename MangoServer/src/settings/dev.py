# -*- coding: utf-8 -*-
# @Project: 芒果测试平台
# @Description:
# @Time   : 2024-07-12 14:13
# @Author : 毛鹏
import json
import os

# ************************ 数据源类型 ************************ #

IS_SQLITE = False  # 是否选用sqlite作为数据源，默认使用mysql

# ************************ Mysql配置 ************************ #
MYSQL_PORT = 3306
MYSQL_DB_NAME = 'dev_mango_server'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'admin'
MYSQL_IP = '127.0.0.1'

# ************************ DEBUG配置 ************************ #
# 控制django是否debug
DEBUG = True
# 控制日志是否输出debug
IS_DEBUG_LOG = True
# ************************ REDIS配置 ************************ #

REDIS = False
# ************************ Minio配置 ************************ #
IS_MINIO = False
if IS_MINIO:
    MINIO_STORAGE_ENDPOINT = '312404.xyz:9000'
    MINIO_STORAGE_ACCESS_KEY = 'minioadmin'  # ACCESS_KEY
    MINIO_STORAGE_SECRET_KEY = 'Ghc312404@'  # SECRET_KEY
    MINIO_STORAGE_USE_HTTPS = False  # 如果使用 HTTPS，设置为 True
    MINIO_STORAGE_MEDIA_BUCKET_NAME = 'mango-dev'  # 桶名称
    MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True  # 桶不存在时自动创建

# ************************ 是否允许删除 ************************ #
IS_DELETE = True
# *************** 是否发送error日志协助芒果修复问题 *************** #
IS_SEND_MAIL = False

# **************** 个人配置，开源用户忽略这部分代码 **************** #
IS_TRUE = True
file_name = 'src/settings/database.json'
if os.path.exists(file_name) and IS_TRUE:
    # 读取数据
    with open(file_name, 'r') as file:
        data = json.load(file)

    MYSQL_PORT = data.get('mysql_port', MYSQL_PORT)
    MYSQL_DB_NAME = data.get('mysql_db_name', MYSQL_DB_NAME)
    MYSQL_USER = data.get('mysql_user', MYSQL_USER)
    MYSQL_PASSWORD = data.get('mysql_password', MYSQL_PASSWORD)
    MYSQL_IP = data.get('mysql_ip', MYSQL_IP)

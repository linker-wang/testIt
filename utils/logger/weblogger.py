import logging
import logging.config
import os

# 文件路径
config_path=os.path.dirname(__file__)+"/logging.conf"

# 配置logging
logging.config.fileConfig(config_path)

# 获取weblog
weblog=logging.getLogger("weblog")
from utils.browser import Browser
import pytest
import json
from time import sleep
from utils.load_cases import load_json_cases
from utils.case_handler import run_front
from utils.case_handler import run_end
from utils.logger.weblogger import weblog

# 加载配置信息
with open("config.json", 'r') as file:
    config=json.load(file)

# 解包配置文件
driver_path=config["driver_path"]
json_case_path=config["json_case_path"]
    
# 打开浏览器的夹具（会话级别）
@pytest.fixture(scope="session", autouse=True)
def browser(request):
    global driver
    driver=Browser(driver_path=driver_path)
    def end():
        driver.quit()
    request.addfinalizer(end)
    return driver

# 返回日志器
@pytest.fixture(scope="function", autouse=True)
def get_logger():
    return weblog

# 获取所有测试用例
cases_params=load_json_cases(json_case_path)
@pytest.fixture(scope="function", autouse=True, params=cases_params)
def get_case(request, browser):
    print("================================================================================")
    weblog.debug(f"正在执行{request.param['module']}")
    weblog.debug(f"前置条件：{request.param['preconditions']}")
    
    # 执行前置操作
    run_front(browser, request.param["front"], weblog)
    
    yield request.param
    # 执行后置操作
    run_end(browser, request.param["end"], weblog)
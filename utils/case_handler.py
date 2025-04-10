from selenium.webdriver.common.by import By

def run_step(browser, steps, logger):
    for step in steps:
        # 打印描述信息
        logger.debug(step["desc"])
        
        # 获取valus
        values=step["values"]
        
        # 判断opentype
        open_type=step["open_type"]
        if open_type=="get":
            url=values["url"]
            browser.get(url)
            
        elif open_type=="click":
            browser.click((values["locale_basis"], values["locale_value"]))
            
        elif open_type=="input":
            browser.send_keys((values["locale_basis"], values["locale_value"]), values["input_value"])
        
        else:
            pass
        
def judgment_result(browser, expected_result, logger):
    for item in expected_result:
        if item["type"] == "element exist":
            assert len(browser.locate_elements(item["locale_basis"], item["locale_value"])) != 0  
            
def run_front(browser, front, logger):
    print("")
    logger.debug("正在执行前置操作")
    run_step(browser, front, logger)
    logger.debug("前置操作执行完毕")

def run_end(browser, end, logger):
    print("")
    logger.debug("正在执行后置操作")
    run_step(browser, end, logger)
    logger.debug("后置操作执行完毕")
    
if __name__ == '__main__' :
    run_step("docs/ddt/cases.json")
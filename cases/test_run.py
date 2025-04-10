from utils.case_handler import run_step, judgment_result

def test_run(browser, get_case, get_logger):
    # 解包用例    
    steps=get_case["steps"]
    expected_result=get_case["expected_result"]
    
    # 执行步骤
    get_logger.debug("正在执行测试步骤")
    run_step(browser, steps, get_logger)
    get_logger.debug("测试步骤执行完毕")
    
    # 判断结果
    judgment_result(browser, expected_result, get_logger)
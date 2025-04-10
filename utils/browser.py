from selenium import webdriver

class Browser:
    def __init__(self, driver_path, broswer_name=None, service=None, options=None):
        self.driver=self.open_Browser(driver_path, broswer_name=broswer_name, service=service, options=options)
        
    # 打开浏览器
    def open_Browser(self, driver_path=None, broswer_name=None, service=None, options=None):
        # 获取浏览器名_默认为Chrome
        if broswer_name==None:
            self.broswer_name="Chrome"
        else:
            self.broswer_name=broswer_name
            
        # 设置浏览器与模块
        self.broswer=getattr(webdriver, self.broswer_name)
        self.broswer_module=getattr(webdriver, self.broswer_name.lower())
        
        # 防止驱动路径未传入
        assert driver_path != None
        
        # 设置service
        if service==None:
            self.service=getattr(self.broswer_module.service, "Service")(executable_path=driver_path)
        else:
            self.service=service
            
        # 设置options
        if options==None:
            self.options=getattr(self.broswer_module.options, "Options")()
        else:
            self.options=options
        
        # 打开浏览器后不自动关闭浏览器
        self.options.add_experimental_option('detach', True)
        
        # 获取浏览器驱动
        driver=self.broswer(service=self.service, options=self.options)
                
        # 浏览器窗口最大化
        driver.maximize_window()
        
        # 设置隐式等待
        driver.implicitly_wait(5)
        
        return driver
    
    # 访问网页
    def get(self, url=None):
        assert url!=None
        self.driver.get(url)
    
    # 关闭浏览器
    def quit(self):
        self.driver.quit()
    
    # 定位单个元素
    def locate_element(self, *args):
        return self.driver.find_element(*args)
    
    # 定位一组元素
    def locate_elements(self, *args):
        return self.driver.find_elements(*args)
    
    # 元素设置值
    def send_keys(self, locate_tuple=None, content="", element=None):
        if element==None:
            self.locate_element(*locate_tuple).send_keys(content)
        else:
            element.send_keys(content)
    
    # 元素点击
    def click(self, locate_tuple=None, element=None):
        if element==None:
            self.locate_element(*locate_tuple).click()
        else:
            element.click()
    
    # 获取元素文本内容:
    def get_text(self, locate_tuple):
        return self.locate_element(*locate_tuple).text
    
    # 切换到frame
    def switch_to_frame(self, keyword):
        self.driver.switch_to.frame(keyword)
    
    # 切换回默认上下文
    def switch_to_default(self):
        self.driver.switch_to.default_content()
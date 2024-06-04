from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager

options = EdgeOptions()
# 在这里添加你需要的选项，例如：options.add_argument('--headless')

# Selenium 4之后，可以使用WebDriverManager自动处理驱动程序的下载和路径问题
service = EdgeService(EdgeChromiumDriverManager().install())

driver = webdriver.Edge(service=service, options=options)

try:
    driver.get("https://www.baidu.com")
    # 你的自动化测试代码放在这里...
finally:
    driver.quit()

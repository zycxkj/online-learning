from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from selenium.webdriver.common.by import By

#构造浏览器
option = webdriver.ChromeOptions()
option.add_argument("--mute-audio")#浏览器静音
option.add_experimental_option("detach", True)#防止浏览器自动关闭
bro: WebDriver = webdriver.Chrome(options=option)

#定义登录页面
home_url = ('https://www.sqgj.gov.cn/')
#打开登录页面
bro.get (home_url)
bro.maximize_window()#最大化窗口
time.sleep(1)
#输入用户名
# 输入用户名
bro.find_element(By.XPATH, '//input[@placeholder="请输入手机号"]').send_keys('13992554268')
time.sleep(1)
# 输入密码
bro.find_element(By.XPATH, '//input[@placeholder="请输入密码"]').send_keys('Ly187714.')
time.sleep(10)
#机器识别验证码准确率不高，所以改为手动输入验证码，
# url= (bro.current_url)#读取当前网页地址，
#这里会在当前页面刷新出菜单，点击学习课程,下面的代码是通过xpath定位a标签，如果a标签名称发生变化，需要修改
i=1
while i < 60:
    #刷新页面
    windows = bro.window_handles
    bro.switch_to.window(windows[0])
    bro.refresh()
    time.sleep(3)
    #点击学习课程，如果a标签名称发生变化，需要修改
    bro.find_element(By.XPATH,"//a[contains(text(),'学习课堂')]").click()
    #点击学习课程后，进入页面，再次点击进入学习
    time.sleep(2)
    bro.find_element(By.XPATH, "//div[@class='irr']/div/div[@class='btn']").click()
    time.sleep(3)
    #点击当前页面第一个课程，因为新框架没有对按钮进行分类，所以只能选择class name为btn的第一个按钮
    bro.find_element(By.XPATH,"(//div[@class='btn'])[1]").click()
    #切换到视频播放窗口
    time.sleep(3)
    windows = bro.window_handles
    # 切换到当前最新打开的窗口
    bro.switch_to.window(windows[-1])
    time.sleep(3)
    #点击第一个视频链接
    # 获取当前页面有几个视频
    sp=bro.execute_script("return document.getElementsByClassName('vvitemtitle').length")#获取当前页面有多少视频
    spxl=1#定义循环次数
    while spxl <= sp:
        time.sleep(3)
        print ('当前视频编号为', spxl)
        #点击第N个视频链接，N=spxl-1,也就是按序号，从0开始
        bro.execute_script("return document.getElementsByClassName('vvitemtitle')["+str(spxl-1)+"].click()")
        #读取当前视频是否播放完毕，返回值为F,T，而且当前视频播放完毕后，会自动跳转到下一个视频
        time.sleep(3)
        end_flag=bro.execute_script("return document.getElementsByClassName('videoplayer')[0].ended")
        #每2分钟读取一次视频播放进度，如果第一个视频播放完毕，则开始播放第二个，以此类推，如果当前视频播放完毕，则跳出循环
        time.sleep(3)
        xxsc = 0
        while end_flag == False: #如果播放结束标志为F，则进入循环，每2分钟读取一次视频播放进度，如果当前视频播放完毕，则跳出循环
            time.sleep(120)
            xxsc = xxsc + 2
            print('本视频已经学习', xxsc, '分钟')
            end_flag=bro.execute_script("return document.getElementsByClassName('videoplayer')[0].ended")
        else:
            print('视频编号', spxl, '播放完毕')
            spxl = spxl + 1
            pass
    else:
        # 关闭视频播放窗口
        windows = bro.window_handles
        #关闭当前窗口
        bro.close()
        print('今日已学习',i,'次课程')
        i=i+1

bro.quit()

'''
---------------------------
File Name:study1
Author:FENGXIN
date:2022/3/16-22:35

---------------------------

'''
# id 相当于位置，身份证号，
# name 相当于姓名，可能会有重名
# 找到输入框,输入内容send_keys  点击 click()
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()

# class属性 进行定位 在页面上会有重复的
# class1 = driver.find_element_by_class_name("title-content-title")

# 文本内容打印出来
# print(class1.text)
# 属性值 默认找第一个属性的值  find_element_by_class_name默认第一个class属性
# class2 = driver.find_element_by_class_name("title-content-title")
# print(class2.text)

# 多一个S 复数，可以找到很多个值，是一个列表['']
#

# tagName 标签进行元素定位  标签是重复的 input span div
# 文本内容 设置
#
# span1=driver.find_element_by_tag_name('span')
# print(span1.text)

# 有很多内容都有span标签 span打印出来
# span2 =driver.find_elements_by_tag_name("span")
# 循环进行答应  也是一样可以通过下标 class tagname应用的比较少
# for i in span2:
#     print(i.text)


# link和partial_link定位 超链接标签<a href='http:www.baidu.com'></a>
# link1 = driver.find_element_by_link_text('新闻')
# link1.click()

# partial_link  超链接定位 link和partial_link的区别  文本值，link必须写全，partial_link不需要全部写全
# link2 = driver.find_element_by_partial_link_text("学术")
# link2.click()

# xpath 定位 id,name,class,tagname 都没有
# 页面 会很不好定位
# xpath  定位，在工作中应用的比较多  绝对路径的写法，表达式的写法
# input1=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input")
# input1.send_keys("Selenium")

# 表达式写法 按照属性来定位 格式[@属性='属性值'] /跟节点  //代表所有的节点  *所有元素
# input2 = driver.find_element_by_xpath('//*[@id="kw"]') id 要是数字不要用
# input2.send_keys("selenium")

# css表达式定位输入框  id定位 要加#,输入#加上值  class、标签定位
# element=driver.find_element_by_css_selector('#kw')
# element.send_keys("秋水")

# class class_name 可能有重复的 找到很多内容 一般会加s  css选择class属性  .加上值
# elements = driver.find_elements_by_css_selector(".title-content-title")
# for i in elements:
#     print(i.text)


# 标签 <input>  <div></div> <span>  重复的 s
# elements=driver.find_elements_by_css_selector("span")
# for i in elements:
#     print(i.text)

# 层级关系  父子关系
# <div id = 'content' class='box'>
#     <span>你好呀</span>
#     <input type='text' id ='kw'  class='s_tr'  name='wd'>
#     <label>你好呀2</label>
# </div>


# 通过找后代元素 元素 后代元素 可以通过谷歌浏览器的 右击检查  最右边即可看到层级关系
# element=driver.find_element_by_css_selector("#head_wrapper #kw")
# element.send_keys("秋水")
# driver.find_element_by_css_selector("#head_wrapper .s_btn ").click()
# sleep(3)


# css 标签与属性 <input type='text' id ='kw'  class='s_tr'  name='wd'>
#
# element=driver.find_element_by_css_selector("input[id='kw']")
# element.send_keys("selenium")
# driver.find_element_by_css_selector("input[id='su']").click()







# 等待几点在关闭
sleep(3)

# 没有关闭浏览器
driver.quit()



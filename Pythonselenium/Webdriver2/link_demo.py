'''
---------------------------
File Name:link_demo
Author:FENGXIN
date:2022/3/27-20:51

---------------------------

'''
from selenium import webdriver
from time import sleep

# 加载浏览器对象
driver = webdriver.Chrome()
# 打开浏览器
driver.get("http://www.baidu.com")

# 搜索含有百度的字体
driver.find_element_by_partial_link_text("百度").click()

'''
# xpath：目前应用最多的一种行为，基于页面
# xpath 元素定位 绝对路径，相对路径//*[@id='kw']  //表示从跟路径下开始查找 *代表任意元素 []表示筛选
# @表示基于属性来筛选，列如@id='kw'表示基于id属性值为kw条件来进行筛选
# 或者用//input[@name='accounts']  input代表标签，@用后面可以用属性，也可以用其他的都行，比如
# 确定xpath 路径是否正确 :
 1、在开发者工具elements页面使用ctrl+f查找，进行判断
 2、在console中输入$x()进行校验
如果要基于text来定位元素
在[] 中添加text()="文本内容"进行查找：例如：//a[text()='登录']，text是扩号以外的，如果扩号以内看里面
有什么，那就用什么

当你定位元素时，无法直接定位时，可以通过定位子级元素返回父级来获取元素 //a[text()='登录']/..,返回上一级

//input[@id='kw']  另外一种写法 //input[contains(@id,'kw')] contains表示进一步查找，匹配项模糊查找
如果是text的，那就写//input[contains(text(),'内容')]
如果遇到动态的id，可以用//a[text()='登录']/.. 定位上一层路径 # a代表标签，/..代表上一级
'''
'''
css定位元素方法
1、绝对路径：从根标签[html]一级一级找到目标标签，上下级关系可以用空格或者大于号
   1)id选择器符号：#加上id的值 find_element_by_css_selecotr('#kd')
   2)通过class定位：class选择器符号：.加上属性值 例子百度输入框：find_element_by_css_selecotr('.s_ipt')
   3)其他属性定位：find_element_by_css_selecotr[属性名='属性值']
   4)通过多个属性值定位：find_element_by_css_selecotr([属性名='属性值'][属性名='属性值'])
   5)通过部分属性值定位：[属性名='属性值']
     匹配符号  * 包含某个字符
              ^ 以什么开头
              $ 以什么结尾  [属性名*=f] [属性名^=o] [属性名$=o]
              
  6)通过层级定位  一般情况下会跟id/class/属性一起组合来进行定位，以百度搜索框定位：
  find_element_by_css_selecotr('form#form>span>input').send_keys() 层级组合和id定位
  find_element_by_css_selecotr('form.fm>span>input').send_keys() 层级组合和id定位
    上下级符号:>或者空格
  7) 通过兄弟节点定位
     兄弟定位：同一父级标签，下面有多个相同的元素，那么这些元素就是兄弟节点
     定位第一节点：first-child
     定位第2/3/4节点：nth-child(n)  n代表元素的序号
     定位最后一个节点：last-child
     例子：定位百度新闻：find_element_by_css_selecotr(div#u_sp>a:first-child)
'''

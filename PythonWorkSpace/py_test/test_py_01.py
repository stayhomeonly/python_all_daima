# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/12/13-19:19
=============================
"""
# 1、pytest 安装
# pip install -U pytest
# >pytest --version 查看 pytest版本
# pytest测试框架也是主流的一个测试框架，相比于unittest框架来说，
# 其不需要像unittest那样单独创建类继承unittest.TestCase，
# 而只需要创建测试类或者测试文件，pytest可以按照一定的规则找到测试用例并执行。

'''
编写规则：
测试文件以test_开头（以_test结尾也可以）
测试类以Test开头，并且不能带有 init 方法
测试函数以test_开头
断言使用基本的assert即可
'''

import pytest


class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

    def test_three(self):
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == "__main__":
    # -s: 显示程序中的print / logging输出
    # -v: 丰富信息模式, 输出更详细的用例执行信息
    # -q: 安静模式, 不输出环境信息
    # -k：关键字匹配，用and区分：匹配范围（文件名、类名、函数名）\
    pytest.main()
    # pytest.main(['./'])  # 运行./目录下所有（test_*.py  和 *_test.py）
    # pytest.main(['./subpath1'])  # 运行./subpath1 目录下用例
    # pytest.main(['-q','./test_py_01.py'])  # 运行指定模块
    # pytest.main(['./subpath1/test_module1.py::test_m1_1'])  # 运行模块中的指定用例
    # pytest.main(['./subpath2/test_module2.py::TestM2::test_m2_02'])  # 运行类中的指定用例
    # pytest.main(['-k', 'pp'])  # 匹配包含pp的用例(匹配目录名、模块名、类名、用例名)
    # pytest.main(['-k', 'spec', './subpath1/test_module1.py'])  # 匹配test_module1.py模块下包含spec的用例
    # pytest.main(['-k', 'pp', './subpath2/test_module2.py::TestM2'])  # 匹配TestM2类中包含pp的用例

    # -m ：只运行被标记的测试用例；
    # -k：只运行与给定字符串表达式匹配的测试用例；
    # -s ：显示标准输出，例如print()
    # 的语句；
    # -v ：显示详细报告；
    # -q ：显示简洁报告；
    # -x ：用例失败时立即停止测试；
    # -c
    # file ：从
    # file
    # 加载配置文件；
    # -l(--showlocals) ：用例失败信息回溯时显示局部变量及其值；
    # -rsxX ：报告(r)
    # 测试用例被跳过(s)、预计失败(x)、预计失败但实际通过(X)
    # 的原因；
    # -strict：禁止使用未在配置文件(pytest.ini)
    # 注册的
    # mark
    # 标记；
    # --maxfail = n ：失败n后停止运行测试；
    # --lf(
    #     --last - failed) ：仅执行上次失败的用例；                                                                                                                            如果没有失败的用例或者没找到缓存文件，默认是运行所有的用例！
    # --lfnf = [all, none] ：与 - -lf
    # 同时使用，=all
    # 代表找不到用例或缓存文件时执行所有用例，=none
    # 代表找不到用
    # 例或缓存文件时不执行测试用例；
    # pytest.main(['--lf', '--lfnf=none', "xxx.py"])
    # --ff(--failed - first) ：先执行失败的用例，再执行其他用例；
    # --nf(--new - first) ：首先从新文件或新修改的用例开始运行测试；
    # --sw(--stepwise) ：在测试失败时退出，且下一次在测试失败的用例开始测试；
    # --stepwise - skip ：忽略第一个失败的测试，在第二次测试失败时退出；
    # --keep - duplicates ： 不断重复的测试；
    # --durations = n ：显示执行最慢的n条用例；                                                                                                                                注意：除非添加参数 - vv，默认情况下，否则pytest不会显示 < 0.01
    # s的测试时间；
    # --fixtures ：显示所有可用的
    # fixture；
    # --tb = style ：堆栈回溯信息打印模式(auto / long / short / line / native / no])；
    # --setup - show  ：显示fixture执行步骤；
    # --cache - show = [CACHESHOW] ：显示缓存内容，不执行收集或测试；
    # --cache - clear ：运行前清除pytest缓存；
    # --
    # continue
    # -on - collection - errors：即使发生收集(收集用例阶段)
    # 错误，也强制执行测试；
    # --rootdir = ROOTDIR ：定义测试的根目录；
    # --color = color ：终端输出的颜色(yes / no / auto)；
    #
    # --collect - only ：只收集用例，不执行；
    #
    # --
    # assert=MODE ： “plain”不执行任何断言调试，“rewrite”重写测试模块中的assert语句，以提供assert表达式信息；
    # ————————————————
    # 版权声明：本文为CSDN博主「John.liu_Test」的原创文章，遵循CC
    # 4.0
    # BY - SA版权协议，转载请附上原文出处链接及本声明。
    # 原文链接：https: // blog.csdn.net / lystest / article / details / 115637483

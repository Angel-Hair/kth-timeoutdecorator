# th-timeoutdecorator

## 简介

th-timeoutdecorator 是一个用于Python的超时修饰器，目前已在 Windows 和 Linux 下测试过，也经过了异步兼容的测试，目前只是基本实现了要达到的目的。

修改自这份 ![原代码](http://mail.python.org/pipermail/python-list/2004-May/260937.html) 不过它无法正常使用。

## Why

实际上超时修饰有很多，但大多数都有很多问题，一部分只能运行在 Linux 系统上，还有一部分无法异步兼容，使得无法满足我的另一个项目 ![XUN_Bot](https://github.com/Angel-Hair/XUN_Bot) 的需求，直到我找到了这份 ![原代码](http://mail.python.org/pipermail/python-list/2004-May/260937.html)，令人非常惊艳的code，但是由于部分原因使得它无法被正常使用。而本项目是我修改后可以正常使用的版本。

## 安装

From source code:

```bash
python setup.py install
```

From pypi:

```bash
pip install timeoutdecorator
```

## 使用方法

```python
import time
import timeoutdecorator

@timeoutdecorator.timeout(4)
def testmain():
    print("Start")
    for i in range(6):
        time.sleep()
        print("[Test] {} seconds have passed".format(i+1))

def mytest():
    try:
        testmain()
    except TimeoutException as e:
        print("[Test] {}".format(e))

if __name__ == '__main__':
    mytest()
```

## 开源许可证

本项目使用 ![MIT](https://github.com/Angel-Hair/th-timeoutdecorator/blob/master/LICENSE) 许可证。
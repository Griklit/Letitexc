# Letitexc

*let it exception.*

## 规则

- 使用正常一点的python3.11运行，其他版本或许也行
- 仅允许在指定函数`answer`中编写代码
- 除非关卡要求，否则禁止创建文件
- 禁止使用诸如内存溢出、外部软件修改、宇宙高能粒子轰击内存位造成的极端异常
- 禁止修改标准库，也禁止利用代码修改标准库内类方法的行为
- 不得重写`raise_me`函数，全局只能存在唯一一个关卡指定的`raise_me`函数
- 可以随意调用`raise_me`函数，随意传入参数
- 在主线程中在函数`raise_me`内部引发异常即视为胜利，否则视为失败

## 示例

```python3
# level/easy/E-01.py
from src import check


def raise_me(alpha):
    beta = alpha + 1
    return beta


@check
def answer():
    raise_me('')
```
```shell
cd /Your-Path/Leitexc/
python3.11 -m level.easy.E-01
```
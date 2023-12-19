# Letitexc

*let it exception.*

## 规则

- 使用标准python3.11运行
- 仅允许在函数`answer`中编写代码
- 除非关卡要求，否则禁止创建文件
- 禁止使用诸如内存溢出、外部软件修改、宇宙高能粒子轰击内存位造成的极端异常
- 不得重写`raise_me`函数，全局只能存在唯一一个关卡指定的`raise_me`函数
- 可以随意调用`raise_me`函数，随意传入参数
- 在函数`raise_me`内部引发异常即视为胜利，否则视为失败

## 示例

```python3
# level/simple/S-01.py
from src import check


def raise_me(alpha):
    beta = alpha + 1
    return beta


@check
def answer():
    raise_me('')
```
```shell
cd /Your-Path/Leitexc
python3.11 level/simple/S-01.py
```
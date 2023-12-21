import os
import re
import json
from uuid import uuid4

from .container import run_container, CodeRunningError, CodeTimeoutError
from .code_generator import LevelDifficulty, generate_code

RESULT_RE = re.compile(r':::json===(.*?)===result:::')


def run(user_input_code: str, level: tuple[LevelDifficulty, int]) -> dict:
    """
    启动容器运行python代码
    :param user_input_code: 用户输入的代码
    :param level: 关卡信息
    :return: 运行结果
    """
    code = generate_code(user_input_code, level)
    code_file_path = '/tmp/' + str(uuid4()) + '.py'
    with open(code_file_path, 'w', encoding='utf-8') as f:
        f.write(code)
    try:
        ret = run_container(code_file_path).decode()
        return json.loads(RESULT_RE.findall(ret)[-1])

    except CodeRunningError as err:
        ...
    except CodeTimeoutError as err:
        ...
    except RuntimeError as err:
        ...
    except Exception as err:
        ...
    finally:
        os.remove(code_file_path)

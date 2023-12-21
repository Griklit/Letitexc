from pathlib import Path
from enum import Enum

REMAKE_LEVEL_FUNC = """
class __HideSuccess(Exception):
    def __init__(self, exception: Exception, line: str | None, lineno: int | None):
        self.exception = exception
        self.line = line
        self.lineno = lineno

    def serialize(self):
        return {
            'exception_type': type(self.exception).__name__,
            'exception': str(self.exception),
            'line': self.line,
            'lineno': self.lineno
        }

    def json(self):
        import json
        return json.dumps(self.serialize(), ensure_ascii=False)


def __hide_catcher(func):
    from functools import wraps
    from sys import exc_info
    from traceback import extract_tb

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as err:
            *_, traceback = exc_info()
            line = lineno = None
            for tb in reversed(extract_tb(traceback)):
                if tb.name == 'raise_me':
                    line = tb.line
                    lineno = tb.lineno
            raise __HideSuccess(err, line, lineno)
        return result

    return wrapper


raise_me = __hide_catcher(raise_me)
"""

FAKE_GLOBALS = """
def globals():
    return {"NM": "SL"}
"""

LEVEL_PATH = Path(__file__).parent.parent / 'level'


class LevelDifficulty(Enum):
    EASY = 'easy'
    NORMAL = 'normal'
    HARD = 'hard'

    def level_file_name(self, level: int) -> str:
        match self:
            case LevelDifficulty.EASY:
                return f'E-{level:02}.py'
            case LevelDifficulty.NORMAL:
                return f'N-{level:02}.py'
            case LevelDifficulty.HARD:
                return f'H-{level:02}.py'


def get_level(level: tuple[LevelDifficulty, int]) -> str:
    level_path = LEVEL_PATH / level[0].value / level[0].level_file_name(level[1])
    with open(level_path, 'r', encoding='utf-8') as f:
        return f.read()


def generate_code(user_input_code: str, level: tuple[LevelDifficulty, int]) -> str:
    level_code = get_level(level)
    code = [
        'def answer():',
    ]
    for line in user_input_code.splitlines():
        code.append("    " + line)

    code.extend([
        'try:',
        '    answer()',
        '    print("|+|json|-|"+\"null\"+"|-|result|+|")',
        'except __HideSuccess as success:',
        '    print("|+|json|-|"+success.json()+"|-|result|+|")',
    ])
    code = '\n'.join(code)
    return level_code + REMAKE_LEVEL_FUNC + FAKE_GLOBALS + code


if __name__ == '__main__':
    print(generate_code('\n', (LevelDifficulty.EASY, 1)))

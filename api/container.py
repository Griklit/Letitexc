from pathlib import Path
from uuid import uuid4

import docker
from docker.errors import ContainerError

PYTHON_IMAGE = 'python:3.12.1-alpine'
docker_client = docker.DockerClient(base_url='tcp://127.0.0.1:2375', version='auto', timeout=10)


class CodeRunningError(Exception):
    def __init__(self, msg: str):
        self.msg = msg


class CodeTimeoutError(Exception):
    pass


def run_container(code_file_path: str) -> bytes:
    """
    启动容器运行python代码
    :param code_file_path: python代码文件路径（绝对路径）
    :return: 运行结果
    """
    try:
        ret = docker_client.containers.run_container(
            # 执行参数
            PYTHON_IMAGE, 'timeout 10 python /home/letitexc.py', init=True,
            volumes={code_file_path: {'bind': '/home/letitexc.py', 'mode': 'ro'}},

            # 权限控制
            read_only=True, network_mode=None, user='nobody',
            cpu_period=100_000, cpu_quota=12_500, cpu_shares=128, mem_limit='100m',

            # 标签
            labels={'com.docker.compose.project': 'letitexc'},
            name=f'letitexc-{uuid4()}',
        )
    except ContainerError as err:
        if err.exit_status == 1:
            raise CodeRunningError(err.stderr.decode())
        elif err.exit_status == 128 + 15:
            raise CodeTimeoutError('Timeout.')
        else:
            raise RuntimeError('Unknown error.')
    finally:
        docker_client.containers.prune(filters={'label': ['com.docker.compose.project=letitexc']})
    return ret


if __name__ == '__main__':
    try:
        print(run_container('/tmp/test.py'))
    except Exception as e:
        print(e)

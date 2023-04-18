import logging
from subprocess import Popen, PIPE
from time import sleep

import pytest


def pytest_addoption(parser):
    parser.addoption("--pypath", action="store", default="python", help="Path to python interpreter in the venv")


@pytest.fixture(scope='session')
def pypath(request):
    pypath = request.config.getoption("--pypath")
    logging.info(f'Python path is: {pypath}')
    return request.config.getoption("--pypath")


@pytest.fixture(scope='session')
def http_server(pypath):
    logging.info('Starting server...')
    server = Popen([pypath, 'api_server.py'], stdout=PIPE, stderr=PIPE)
    sleep(1)  # Wait for server to start up
    yield
    logging.info('Stopping server...')
    server.kill()

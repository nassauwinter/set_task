import argparse
import logging
import statistics
import time
from datetime import datetime
from subprocess import Popen, PIPE
from time import sleep

import requests


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'performance_log_{datetime.now().strftime("%Y%m%d%H%M%S")}.log'),
        logging.StreamHandler()])


logging.debug('Parse command-line arguments')
parser = argparse.ArgumentParser()
parser.add_argument("--pypath", help="path to Python executable", action='store', default='python')
args = parser.parse_args()


logging.info('Starting server...')
server = Popen([args.pypath, 'api_server.py'], stdout=PIPE, stderr=PIPE)
sleep(1)

server_url = "http://localhost:3000/"
endpoint = "people/1/"
test_duration = 60


response_times = []

logging.info('Starting performance test...')
start_time = time.time()
with requests.Session() as session:
    while time.time() - start_time < test_duration:
        response = session.get(server_url + endpoint)
        response_time = response.elapsed.total_seconds()
        response_times.append(response_time)
        session.close()

mean_response_time = statistics.mean(response_times)
std_dev_response_time = statistics.stdev(response_times)

logging.info('Stopping server...')
server.kill()

logging.info(f"Mean response time: {mean_response_time:.3f} seconds")
logging.info(f"Standard deviation of response time: {std_dev_response_time:.3f} seconds")

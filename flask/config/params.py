import argparse
import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def parse_args():
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--log_path', default=basedir + '/log/log.log', type=str, required=False, help='日志路径')
    parser.add_argument('--num', default=3, type=str, required=False, help='')

    args,unknown = parser.parse_known_args()

    return args
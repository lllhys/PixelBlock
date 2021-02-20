import logging
from logging import handlers
import os


def get_logger():
    return logging.getLogger('PixelBlock')


def logging_init():
    LOG_FORMAT = "[PixelBlock]  %(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    # 路径判断
    if os.path.exists('./logs') is not True:
        os.mkdir("./logs/")
    # 全局日志文件
    logging.basicConfig(filename='./logs/PixelBlock_All.txt', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
    # logger配置
    logger = get_logger()
    format_str = logging.Formatter(LOG_FORMAT,DATE_FORMAT)
    # console stream
    sh = logging.StreamHandler()
    sh.setFormatter(format_str)
    logger.addHandler(sh)
    # log file
    th = handlers.TimedRotatingFileHandler(filename='./logs/PixelBlock', when='D', backupCount=3, encoding='utf-8')
    th.setFormatter(format_str)
    logger.addHandler(th)
    return logger


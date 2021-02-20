import yaml
import os
import logging
from logging import handlers
import urllib3
from  conponent import config,log

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logger = log.logging_init()

def init():

    logger.info('*****************************************')
    logger.info('*              PixelBlock               *')
    logger.info('*            2021 (c) lllhy             *')
    logger.info('*****************************************')
    logger.info('PixelBlock 启动中...')
    config.init()



if __name__ == "__main__":
    init()
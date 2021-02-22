import yaml
import os
import logging
from logging import handlers
import urllib3
from  conponent import config,log
from renderer.pixel_matrix import PixelCanvas

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
    pixel_matrix = PixelCanvas(0xffff1f)
    # print(pixel_matrix.matrix)
    # show_tool.set_all(pixel_matrix.matrix)
    # show_tool.idle()
    pixel_matrix.show()

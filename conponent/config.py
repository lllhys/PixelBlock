# -*- coding: utf-8-*-
import yaml
import os
from conponent import log

logger = log.get_logger()
def init():
    logger.info('init config file.')





def get_base_path():
    return os.getcwd()

def get_effector_path():
    return os.getcwd()+'\\renderer\\effectors'
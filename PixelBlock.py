import yaml
import os
import logging
from logging import handlers
import urllib3
from  conponent import config,log
from renderer import static_font
from renderer.color import *
from renderer.effector_loader import *
from renderer.pixel_canvas import PixelCanvas
from renderer.pixel_element import PixelElement

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logger = log.logging_init()

def init():

    logger.info('*****************************************')
    logger.info('*              PixelBlock               *')
    logger.info('*            2021 (c) lllhy             *')
    logger.info('*****************************************')
    logger.info('PixelBlock 启动中...')
    init_effectors()
    pixel_canvas = PixelCanvas((8,32))
    init_show(pixel_canvas)

def init_show(pixel_canvas):
    color_style_1 = get_color_style((5,5),0xffffff00)
    element_P = PixelElement(0, static_font.P_mask, color_style_1)
    pixel_canvas.put_element('P',element_P,layer=1,position=(1,1))

    element_i = PixelElement(0, static_font.i_mask, color_style_1)
    pixel_canvas.put_element('i',element_i,layer=2,position=(1,5))

    element_x = PixelElement(0, static_font.x_mask, color_style_1)
    pixel_canvas.put_element('x',element_x,layer=3,position=(1,9))

    element_e = PixelElement(0, static_font.e_mask, color_style_1)
    pixel_canvas.put_element('e',element_e,layer=1,position=(1,12))

    element_l = PixelElement(0, static_font.l_mask, color_style_1)
    pixel_canvas.put_element('l',element_l,layer=2,position=(1,16))


if __name__ == "__main__":
    init()
    # pixel_matrix = PixelCanvas(0xffff1f)
    # # print(pixel_matrix.matrix)
    # # show_tool.set_all(pixel_matrix.matrix)
    # # show_tool.idle()
    # pixel_matrix.show()

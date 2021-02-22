from conponent import log
import numpy as np

logger = log.get_logger()

class PixelElement:
    shape = (0,0)
    element_mask = None
    color_matrix = None
    element_style = None

    def __init__(self,element_type, element_mask=None, color_matrix=None):
        if element_type == 0:
            if element_mask is None or color_matrix is None:
                logger.error('element type设为掩膜+颜色时，element_mask或color_matrix不允许为空')
            self.element_mask = element_mask
            self.color_matrix = color_matrix
            self.element_style = self.get_element_style()
            self.shape = element_mask.shape
        elif element_type == 1:
            if color_matrix is None:
                logger.error('element type设为仅颜色时，color_matrix不允许为空')

            self.color_matrix = color_matrix
            self.element_style = color_matrix
            self.shape = color_matrix.shape
            self.element_mask = np.ones(self.shape,dtype='uint8')
        else:
            logger.error('非法的element_type')



    def get_element_style(self):
        if self.element_mask is None:
            return self.color_matrix
        else:
            return self.element_mask*self.color_matrix

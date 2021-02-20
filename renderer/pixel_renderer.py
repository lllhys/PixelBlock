import random
import time
import numpy as np
import static_font
from pixel_matrix import PixelMatrix
from tools.pixel_matrix_show import PixelMatrixShow
from conponent import log

logger = log.get_logger()

class Renderer():
    show_tool = PixelMatrixShow()
    def __init__(self):
        1


    def put_element(self,pixel_matrix,color_matrix,position=(0,0)):
        element_shape = color_matrix.shape
        for i in range(0,element_shape[0]):
            for j in range(0,element_shape[1]):
                pixel_matrix.matrix[position[0]+i][position[1]+j] = color_matrix[i][j]

    def put_element(self,pixel_matrix,mask_matrix,color_matrix,position=(0,0)):
        element_shape = mask_matrix.shape
        for i in range(0,element_shape[0]):
            for j in range(0,element_shape[1]):
                if mask_matrix[i][j] == 0:
                    continue
                pixel_matrix.matrix[position[0]+i][position[1]+j] = color_matrix[i][j]

    def matrix_transition(self,matrix_a,matrix_b,type=0,freq_t=0):
        logger.info('Matrix transition renderer.')
        # type 1 表示横向过渡
        # type 0 表示纵向过渡
        if type == 1:
            # matrix = np.concatenate((matrix_a,matrix_b),axis=1)  #沿着矩阵行拼接
            matrix = np.hstack((matrix_a,matrix_b))
            # print(matrix.shape)
            while matrix.shape[1]!=32:
                matrix = np.delete(matrix,0,axis=1)
                # print(matrix.shape)
                self.show_tool.set_all(matrix)
                time.sleep(freq_t)
        elif type == 0:
            # matrix = np.concatenate((matrix_a,matrix_b),axis=0)  #沿着矩阵行拼接
            matrix = np.vstack((matrix_a,matrix_b))
            # print(matrix.shape)
            while matrix.shape[0]!=8:
                matrix = np.delete(matrix,0,axis=0)
                # print(matrix.shape)
                self.show_tool.set_all(matrix)
                time.sleep(freq_t)


def color(red,green,blue,white=0):
    return (white << 24) | (red << 16) | (green << 8) | blue


if __name__ == '__main__':
    renderer = Renderer()
    pixel_matrix0 = PixelMatrix()
    color_matrix = np.zeros((5,5),'uint32')
    pixel_matrix = PixelMatrix()
    for i in range(0,5):
        for j in range(0,5):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            colors = color(r,g,b)
            color_matrix[i][j] = color(r,g,b)
    renderer.put_element(pixel_matrix0,static_font.num_1_mask,color_matrix,(1,1))
    renderer.put_element(pixel_matrix0,static_font.num_2_mask,color_matrix,(1,5))
    renderer.put_element(pixel_matrix0,static_font.num_3_mask,color_matrix,(1,9))
    renderer.put_element(pixel_matrix0,static_font.num_4_mask,color_matrix,(1,13))
    renderer.put_element(pixel_matrix0,static_font.num_5_mask,color_matrix,(1,17))
    renderer.put_element(pixel_matrix0,static_font.num_6_mask,color_matrix,(1,21))
    renderer.put_element(pixel_matrix0,static_font.num_7_mask,color_matrix,(1,25))

    renderer.put_element(pixel_matrix,static_font.num_8_mask,color_matrix,(1,28))
    renderer.matrix_transition(pixel_matrix0.matrix,pixel_matrix.matrix,freq_t=0,type=0)
    # show_tool = PixelMatrixShow()
    # show_tool.set_all(pixel_matrix.matrix)
    renderer.show_tool.idle()
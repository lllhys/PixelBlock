import math
import random
import time
import numpy as np
import static_font
from pixel_matrix import PixelCanvas
from tools.pixel_matrix_show import PixelMatrixShow
from conponent import log
from pixel_element import PixelElement
from color import *

logger = log.get_logger()


class Renderer():
    show_tool = PixelMatrixShow()

    canvas = None

    def __init__(self, canvas):
        self.canvas = canvas

    def diff_handle(self,diff):
        diff_type = diff['diff_type']
        change = diff['change']
        transition_name = diff['transition']

        # 元素渲染器
        element_renderer = ElementRenderer(diff)

        # 变更类型分为状态变更和位置变更
        if diff_type == 'state':
            # 改变类型分为显示和隐藏
            if change == 'show':
                # 过渡动画类型
                if transition_name == 'fade':
                    # 褪色过渡
                    return element_renderer.element_fade_in()
            elif change == 'hide':
                # 过渡动画类型
                if transition_name == 'fade':
                    # 褪色过渡
                    return element_renderer.element_fade_out()



    def renderer(self):
        diffs = self.canvas.element_diff
        layer_renderer = LayerRenderer(self.canvas.shape, self.canvas.canvas_style,self.canvas.layer_desc_mask)
        for diff in diffs:
            print(diff)
            transition_style = self.diff_handle(diff)
            element = diff['element']
            layer_renderer.put_element(diff['position'],diff['layer'],transition_style,element)
        for i in range(1, 6):
            self.show_tool.set_all(layer_renderer.transition_layer[i])
        # diff 清空
        self.canvas.element_diff.clear()
        # 更新画布最后画面
        self.canvas.canvas_style = layer_renderer.transition_layer[-1]
        self.canvas.layer_desc_mask = layer_renderer.layer_desc_mask


    # def put_element(self, matrix, element_attr,type,speed):
    #     element = element_attr['element']
    #     position = element_attr['position']
    #     level = element_attr['level']
    #     element_shape = element.shape
    #     element_style = element.get_element
    #     for i in range(0, element_shape[0]):
    #         for j in range(0, element_shape[1]):
    #             pixel_matrix.matrix[position[0] + i][position[1] + j] = element_style[i][j]
    #
    # def put_element(self, pixel_matrix, mask_matrix, color_matrix, position=(0, 0)):
    #     element_shape = mask_matrix.shape
    #     for i in range(0, element_shape[0]):
    #         for j in range(0, element_shape[1]):
    #             if mask_matrix[i][j] == 0:
    #                 continue
    #             pixel_matrix.matrix[position[0] + i][position[1] + j] = color_matrix[i][j]



    # def test_show(self):
    #     self.show_tool.set_all_same(0x0)
    #     time.sleep(1)
    #     color_matrix = np.array([[0x00ffff] * 5] * 5, 'uint32')
    #     element = PixelElement(0, static_font.num_3_mask, color_matrix)
    #     time_1 = time.time()
    #     self.element_transition({'level': 0, 'position': (1, 1), 'element': element}, 'fade_in_out')
    #     # for i in range(1,6):
    #     #     self.show_tool.set_all(self.transtion_layer[i])
    #     color_matrix = np.array([[0xff00ff] * 5] * 5, 'uint32')
    #     element = PixelElement(0, static_font.num_5_mask, color_matrix)
    #     self.element_transition({'level': 0, 'position': (1, 6), 'element': element}, 'fade_in_out')
    #     time_2 = time.time()
    #
    #     for i in range(1, 6):
    #         self.show_tool.set_all(self.transtion_layer[i])
    #     time_3 = time.time()
    #     print(time_2 - time_1, time_3 - time_2)
    #     self.show_tool.idle()





    def matrix_transition(self, matrix_a, matrix_b, type=0, freq_t=0):
        logger.info('Matrix transition renderer.')
        # type 1 表示横向过渡
        # type 0 表示纵向过渡
        if type == 1:
            # matrix = np.concatenate((matrix_a,matrix_b),axis=1)  #沿着矩阵行拼接
            matrix = np.hstack((matrix_a, matrix_b))
            # print(matrix.shape)
            while matrix.shape[1] != 32:
                matrix = np.delete(matrix, 0, axis=1)
                # print(matrix.shape)
                self.show_tool.set_all(matrix)
                time.sleep(freq_t)
        elif type == 0:
            # matrix = np.concatenate((matrix_a,matrix_b),axis=0)  #沿着矩阵行拼接
            matrix = np.vstack((matrix_a, matrix_b))
            # print(matrix.shape)
            while matrix.shape[0] != 8:
                matrix = np.delete(matrix, 0, axis=0)
                # print(matrix.shape)
                self.show_tool.set_all(matrix)
                time.sleep(freq_t)


class ElementRenderer:
    element = None
    position = None
    element_shape = None
    element_style = None

    def __init__(self, element_desc):
        self.element = element_desc['element']
        self.position = element_desc['position']
        self.element_shape = self.element.shape
        self.element_style = self.element.get_element_style()

    def color_transition(self, color_before, color_after, layer_sum, layer_id):
        if color_before == color_after:
            return color_after
        red_before, green_before, blue_before = get_RGB_color(color_before)
        red_after, green_after, blue_after = get_RGB_color(color_after)
        red_step = (red_before - red_after) / layer_sum
        green_step = (green_before - green_after) / layer_sum
        blue_step = (blue_before - blue_after) / layer_sum
        return get_hex_color(red_before - red_step * layer_id, green_before - green_step * layer_id,
                             blue_before - blue_step * layer_id)

    def element_fade_in(self, render_layer_sum=5):
        shape_a = self.element_shape[0]
        shape_b = self.element_shape[1]
        render_layer = np.zeros((render_layer_sum, shape_a, shape_b), dtype='uint32')

        for layer_num in range(0, render_layer_sum):
            for i in range(0, shape_a):
                for j in range(0, shape_b):
                    render_layer[layer_num][i][j] = self.color_transition(0x0, self.element_style[i][j],
                                                                          render_layer_sum, layer_num)
        return render_layer

    def element_fade_out(self, render_layer_sum=5):
        shape_a = self.element_shape[0]
        shape_b = self.element_shape[1]
        render_layer = np.zeros((render_layer_sum, shape_a, shape_b), dtype='uint32')

        for layer_num in range(0, render_layer_sum):
            for i in range(0, shape_a):
                for j in range(0, shape_b):
                    render_layer[layer_num][i][j] = self.color_transition(self.element_style[i][j], 0x0,
                                                                          render_layer_sum, layer_num)
        return render_layer


class LayerRenderer():
    shape_a = 0
    shape_b = 0
    transition_layer = None
    layer_desc_mask = None

    def __init__(self, canvas_shape, canvas_style, layer_desc_mask):
        self.shape_a = canvas_shape[0]
        self.shape_b = canvas_shape[1]
        # 层叠渲染最底层样式为当前画布样式
        self.transition_layer = np.zeros((1, self.shape_a, self.shape_b), dtype='uint32')
        self.transition_layer[0] = canvas_style
        # 层叠描述掩膜
        self.layer_desc_mask = layer_desc_mask

    def same_layer_renderer(self, color_before, color_add):
        red_before, green_before, blue_before = get_RGB_color(color_before)
        red_add, green_add, blue_add = get_RGB_color(color_add)
        red = red_before + red_add if red_before + red_add < 256 else 255
        green = green_before + green_add if green_before + green_add < 256 else 255
        blue = blue_before + blue_add if blue_before + blue_add < 256 else 255
        return get_hex_color(red, green, blue)

    def put_element(self, position, layer, renderer_transition,element):
        position_a = position[0]
        position_b = position[1]
        layer_sum = renderer_transition.shape[0]
        element_mask = element.element_mask
        for frame in range(0, layer_sum):
            # 过渡渲染添加层
            if self.transition_layer.shape[0] < layer_sum + 1:
                # self.transition_layer = np.insert(self.transition_layer,frame+1, values=np.zeros((self.shape_a, self.shape_b), dtype='uint32'), axis=0)
                self.transition_layer = np.insert(self.transition_layer,frame+1, values=self.transition_layer[frame], axis=0)

            for i in range(0, renderer_transition.shape[1]):
                for j in range(0, renderer_transition.shape[2]):
                    pixel_position_a = position_a + i
                    pixel_position_b = position_b + j
                    # 像素位置合法性判断
                    if pixel_position_a >= self.shape_a or pixel_position_b>=self.shape_b:
                        continue
                    # 元素掩膜判断是否需要渲染
                    if element_mask[i][j] == 0:
                        continue
                    pixel_layer = self.layer_desc_mask[pixel_position_a][pixel_position_b]
                    if layer < pixel_layer:
                        continue
                    if layer == pixel_layer:
                        # 同层渲染
                        color_before = self.transition_layer[frame + 1][pixel_position_a][pixel_position_b]
                        color_add = renderer_transition[frame][i][j]
                        self.transition_layer[frame + 1][pixel_position_a][pixel_position_b] = self.same_layer_renderer(
                            color_before, color_add)
                    else:
                        # 层级更新
                        self.layer_desc_mask[pixel_position_a][pixel_position_b] = layer
                        # 样式覆盖
                        self.transition_layer[frame + 1][pixel_position_a][pixel_position_b] =  renderer_transition[frame][i][j]


if __name__ == '__main__':
    # pixel_matrix0 = PixelMatrix()
    # color_matrix = np.zeros((5,5),'uint32')
    # pixel_matrix = PixelMatrix()
    # for i in range(0,5):
    #     for j in range(0,5):
    #         r = random.randint(0,255)
    #         g = random.randint(0,255)
    #         b = random.randint(0,255)
    #         colors = color(r,g,b)
    #         color_matrix[i][j] = color(r,g,b)
    # renderer.put_element(pixel_matrix0,static_font.num_1_mask,color_matrix,(1,1))
    # renderer.put_element(pixel_matrix0,static_font.num_2_mask,color_matrix,(1,5))
    # renderer.put_element(pixel_matrix0,static_font.num_3_mask,color_matrix,(1,9))
    # renderer.put_element(pixel_matrix0,static_font.num_4_mask,color_matrix,(1,13))
    # renderer.put_element(pixel_matrix0,static_font.num_5_mask,color_matrix,(1,17))
    # renderer.put_element(pixel_matrix0,static_font.num_6_mask,color_matrix,(1,21))
    # renderer.put_element(pixel_matrix0,static_font.num_7_mask,color_matrix,(1,25))
    #
    # renderer.put_element(pixel_matrix,static_font.num_8_mask,color_matrix,(1,28))
    # renderer.matrix_transition(pixel_matrix0.matrix,pixel_matrix.matrix,freq_t=0,type=0)
    # # show_tool.set_all(pixel_matrix.matrix)
    # renderer.show_tool.idle()
    # pixel_matrix = PixelMatrix(0xffeeff)
    # print(pixel_matrix.matrix)
    # show_tool.set_all(pixel_matrix.matrix)
    # show_tool.idle()
    # pixel_matrix.show()
    pixel_canvas = PixelCanvas((8,32))
    renderer = Renderer(pixel_canvas)

    color_matrix_1 = np.array([[0x00ff00] * 5] * 5, 'uint32')
    element_3 = PixelElement(1, static_font.num_3_mask, color_matrix_1)

    pixel_canvas.put_element('3',element_3,layer=1,position=(1,1))
    renderer.renderer()
    time.sleep(0.5)
    color_matrix_2 = np.array([[0x0000ff] * 5] * 5, 'uint32')
    element_5 = PixelElement(1, static_font.num_5_mask, color_matrix_2)

    pixel_canvas.put_element('5',element_5,layer=2,position=(1,3))

    renderer.renderer()

    renderer.show_tool.idle()



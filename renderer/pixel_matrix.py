import numpy
from tools.pixel_matrix_show import PixelMatrixShow

show_tool = PixelMatrixShow()


class PixelCanvas:
    shape = None
    canvas_style = None
    layer_desc_mask = None
    auto_renderer = True
    elements = {}
    element_diff = []

    def __init__(self, shape, background=0x0):
        self.shape = shape
        self.layer_desc_mask = numpy.zeros(shape, dtype='uint8')
        if background is not 0x0:
            self.canvas_style = numpy.array([[background] * shape[1]] * shape[0], 'uint32')
        else:
            self.canvas_style = numpy.zeros((shape[0], shape[1]), 'uint32')



    def put_element(self, element_name, element, layer=0, position=(0, 0), transition_name='fade'):
        self.elements[element_name] = {'layer': layer, 'position': position, 'element': element}
        self.element_diff.append({
            'element_name': element_name,
            'diff_type': 'state',
            'change': 'show',
            'transition': transition_name,
            'layer': layer,
            'position': position,
            'element': element})
        if self.auto_renderer:
            self.renderer_matrix()

    def remove_element(self, element_name):
        pass

    def change_element_level(self, element_name, level):
        self.elements.get(element_name).update('level', level)

    def change_element_position(self, ):
        pass

    def renderer_matrix(self):
        '''
        渲染
        :return:
        '''
        # 交友渲染器分析差异，分析后有渲染器调度元素渲染器与层叠渲染器进行渲染
        pass

    def show(self):
        # print(self.matrix)
        show_tool.set_all(self.canvas_style)
        show_tool.idle()

    def auto_renderer_open(self):
        '''
        打开自动渲染，并进行渲染
        :return: None
        '''
        self.auto_renderer = True
        self.renderer_matrix()

    def auto_renderer_close(self):
        '''
        关闭自动渲染
        :return: None
        '''
        self.auto_renderer = False

    def auto_renderer_switch(self):
        '''
        切换自动渲染状态
        :return: None
        '''
        if self.auto_renderer:
            self.auto_renderer_close()
        else:
            self.auto_renderer_open()


if __name__ == '__main__':
    pixel_matrix = PixelCanvas(0xffeeff)
    # print(pixel_matrix.matrix)
    # show_tool.set_all(pixel_matrix.matrix)
    # show_tool.idle()
    pixel_matrix.show()

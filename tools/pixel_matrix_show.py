import time
from tkinter import *
import random

class PixelMatrixShow():
    # 建立一个框架对象tk
    tk = Tk()
    # 建立一个画布对象canvas，属于tk对象
    canvas = Canvas(tk, width=640, height=160)
    # 将画布对象更新显示在框架中
    canvas.pack()

    def __init__(self):
        # 初始化像素矩阵
        # 每个像素20*20
        self.rectangle_list = []
        for i in range(0, 8):
            line_list = []
            for j in range(0, 32):
                re = self.canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, outline='white',
                                                  fill='black')
                line_list.append(re)
            self.rectangle_list.append(line_list)

    def get_hex_color(self, color):
        '''
        颜色转换
        :param color: 32bit color
        :return: TK color
        '''
        # return '#%02x%02x%02x'%(color[0],color[1],color[2])
        return '#%06x' % color

    def set_one(self, position, color):
        '''
        设置某一像素颜色
        :param position: tuple 像素位置
        :param color: 32bit color
        :return: None
        '''
        self.canvas.itemconfig(self.rectangle_list[position[0]][position[1]], fill=self.get_hex_color(color))
        self.tk.update()

    def set_all_same(self, color):
        '''
        将所有像素设置为同一颜色
        :param color: 32bit color
        :return: None
        '''
        for i in range(0, 8):
            for j in range(0, 32):
                self.canvas.itemconfig(self.rectangle_list[i][j], fill=self.get_hex_color(color))
        self.tk.update()

    def set_all(self,color_matrix):
        '''
        将所有像素按color matrix设置
        :param color_matrix: 颜色矩阵
        :return: None
        '''
        for i in range(0, 8):
            for j in range(0, 32):
                self.canvas.itemconfig(self.rectangle_list[i][j], fill=self.get_hex_color(color_matrix[i][j]))
        self.tk.update()
    def clear_one(self, position):
        '''
        清除某一像素颜色
        :param position: tuple 像素位置
        :return: None
        '''
        self.canvas.itemconfig(self.rectangle_list[position[0]][position[1]], fill='black')
        self.tk.update()

    def clear_all(self):
        '''
        清除所有像素
        :return: None
        '''
        for i in range(0, 8):
            for j in range(0, 32):
                self.canvas.itemconfig(self.rectangle_list[i][j], fill='black')
        self.tk.update()

    def idle(self):
        self.canvas.mainloop()



if __name__ == '__main__':
    pixel = PixelMatrixShow()
    pixel.set_one(7, 31, (0,255, 0))
    time.sleep(2)


    color_matrix = []
    for i in range(0,8):
        color_matrix_line = []
        for j in range(0,32):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            color_matrix_line.append((r,g,b))
        color_matrix.append(color_matrix_line)
    pixel.set_all(color_matrix)
    time.sleep(4)

    pixel.set_all_same((200, 120, 160))
    time.sleep(2)

    pixel.clear_all()
    pixel.canvas.mainloop()

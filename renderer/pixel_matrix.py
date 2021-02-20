import numpy


class PixelMatrix():
    matrix = numpy.zeros((8,32),'uint32')
    elements = {}

    def put_element(self,element_name,element,level=0,position=(0,0)):
        self.elements[element_name] = element



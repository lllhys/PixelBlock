class PixelElement:
    element_mask = None
    color_matrix = None

    def __init__(self, element_mask=None, color_matrix=None):
        if element_mask is not None:
            self.element_mask = element_mask
        if color_matrix is not None:
            self.color_matrix = color_matrix

    def get_element(self):
        if self.element_mask is None:
            return self.color_matrix
        else:
            return self.element_mask*self.color_matrix

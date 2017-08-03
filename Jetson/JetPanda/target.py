class target:
    sorter = None
    contours = []
    number_of_targets = 1

    def __init__(self, sorter, number_of_targets):
        self.sorter = sorter
        self.number_of_targets = number_of_targets

    def add_contour(self, contour):
        self.contours.append(contour)

class target:
    perimeter_over_area = 0.5
    perimeter_over_area_tolerence = 0.3
    fill_ratio = 0
    find_one = True
    contours = []

    def __init__(self, perimeter_over_area, perimeter_over_area_tolerence, find_one):
        self.perimeter_over_area = perimeter_over_area
        self.perimeter_over_area_tolerence = perimeter_over_area_tolerence
        self.find_one = find_one
        # self.width_to_height = width_to_height
        # self.fill_ratio = fill_ratio
        # self.find_one = find_one

    def set_contours(self, contours):
        self.contours = contours
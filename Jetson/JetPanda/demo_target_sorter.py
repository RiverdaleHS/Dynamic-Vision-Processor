from sorting_util import *



# Determin how good a target is using information about it
def demo_target_fitness(target):
    return target_area(target), 1

sorters = [demo_target_fitness]
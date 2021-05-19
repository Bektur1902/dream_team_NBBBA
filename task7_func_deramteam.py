import random

def random_element(list):
    random_list = []
    for i in range(10):
        random_list.append(list[random.randint(0, len(list)) - 1])
    return random_list




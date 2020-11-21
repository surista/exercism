import random
import string

class UniqueName(object):
    name_list = []

class Robot:

    def __init__(self):
        self.name = self.gen_name()

    def gen_name(self):
        upl = [ch for ch in string.ascii_uppercase]
        dig = [ch for ch in string.digits]
        name = ''.join(random.choices(upl, k=2)) + ''.join(random.choices(dig, k=3))
        if name not in UniqueName.name_list:
            UniqueName.name_list.append(name)
            return name
        else:
            gen_name()
        print(UniqueName.name_list)

    def reset(self):
        UniqueName.name_list.remove(self.name)
        self.name = self.gen_name()

    def __str__(self):
        return f"Robot name: {self.name}"


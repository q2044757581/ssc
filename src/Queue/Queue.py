import queue as Q


class site(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __lt__(self, other):
        return self.value > other.value

    def get_site(self):
        return [self.name + "充电站", self.value]

    def get_site_name(self):
        return str(self.name + "充电站")
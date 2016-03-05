from abc import abstractmethod


class PriceEngine(object):

    def __init__(self):
        pass
    
    @abstractmethod
    def update_price(self, state):
        pass


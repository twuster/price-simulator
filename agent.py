from abc import abstractmethod


class Agent(object):

    def __init__(self):
        pass

    @abstractmethod
    def eval_state(self, state):
        pass

    @abstractmethod
    def consider_exit(self, state):
        pass

    @abstractmethod
    def adjust_preferences(self, state):
        pass

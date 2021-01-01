import abc
from xmind.core.topic import TopicsElement
class TestComponent(metaclass=abc.ABCMeta):
    def __init__(self,):


    @abc.abstractmethod
    def to_dict(self):
        pass

    def has_next(self):
        pass

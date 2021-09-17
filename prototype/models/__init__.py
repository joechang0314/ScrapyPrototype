"""
to modelise the articles
"""
import abc


class BaseModel(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def to_dict(self):
        pass
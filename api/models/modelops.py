from abc import ABCMeta, abstractmethod


class AbstractBaseModel():
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def id(self):
        pass

    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @classmethod
    @abstractmethod
    def update(cls, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def fetch_all(cls):
        pass

    @classmethod
    @abstractmethod
    def get(cls, *args):
        pass

    @classmethod
    @abstractmethod
    def count(cls):
        pass

    @classmethod
    @abstractmethod
    def get_first_item(cls):
        pass

    @classmethod
    @abstractmethod
    def order_by(cls, *args):
        pass

    @classmethod
    @abstractmethod
    def filter_all(cls, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def filter_by(cls, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def find_first(cls, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def filter_and_count(cls, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def filter_and_order(cls, *args, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def paginate(cls, **kwargs):
        pass
